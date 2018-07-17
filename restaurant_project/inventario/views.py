from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from inventario.models import Producto, ReporteDeExistencia, Existencia
from inventario.serializers import ProductoSerializer, ExistenciaSerializer, ReporteDeExistenciaSerializer
from django.http import JsonResponse, HttpResponse
from inventario.forms import ProductoForm, ExistenciaForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from io import BytesIO
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, SimpleDocTemplate
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors

class Get_producto_Create(APIView):
    def get(self, request):
        producto = Producto.objects.create(nombre=request.GET['nombre'], unidad_de_medida=request.GET['unidad_de_medida'])
        producto.save()
        return JsonResponse({'respuesta':'ok'})

class Get_producto_Update(APIView):
    def get(self, request):
        producto = Producto.objects.filter(id=request.GET['id']).update(nombre=request.GET['nombre'], unidad_de_medida=request.GET['unidad_de_medida'])
        return JsonResponse({'respuesta':'ok'})


class Get_producto_Delete(APIView):
    def get(self, request):
        producto = Producto.objects.filter(id=request.GET['id']).delete()
        return JsonResponse({'respuesta':'ok'})

class Get_producto_List(APIView):
    def get(self, request):
        productos = Producto.objects.all().order_by("id")
        serialized = ProductoSerializer(productos, many=True)
        return Response(serialized.data)

class Get_producto_ListFilter(APIView):
    def get(self, request):
        productos = Producto.objects.filter(nombre__startswith=request.GET['nombre']).order_by('id')
        serialized = ProductoSerializer(productos, many=True)
        return Response(serialized.data)
@login_required
def productos(request):
    form = ProductoForm()
    context = {'form':form}
    return render(request, 'inventario/productos.html', context)

class ReporteDeExistenciaList(ListView):
    model = ReporteDeExistencia
    context_object_name = 'reportes'

class ReporteDeExistenciaDetail(DetailView):
    model = ReporteDeExistencia
    context_object_name = 'reporte'
    template_name = 'inventario/reportedeexistencia_detail.html'
    existenciaForm = ExistenciaForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.existenciaForm
        return context

class ReporteDeExistenciaCreateView(CreateView):
    model = ReporteDeExistencia
    fields = ['fecha_reporte','observaciones']

class ReporteDeExistenciaUpdateView(UpdateView):
    model = ReporteDeExistencia
    fields = ['fecha_reporte', 'observaciones']

class ReporteDeExistenciaDeleteView(DeleteView):
    model = ReporteDeExistencia
    success_url = reverse_lazy("inventario:reportes")

class GetExistenciasList(APIView):
    def get(self, request):
        existencias = Existencia.objects.filter(reporte_de_existencia=request.GET['id_reporte']).order_by('id')
        serialized = ExistenciaSerializer(existencias, many=True)
        return Response(serialized.data)

class GetExistenciasCreate(APIView):
    def get(self, request):
        id_producto = int(request.GET['id_producto'])
        producto = Producto.objects.filter(id=id_producto).get()
        id_reporte = int(request.GET['id_reporte'])
        reporte = ReporteDeExistencia.objects.filter(id=id_reporte).get()
        existencia = Existencia.objects.create(reporte_de_existencia=reporte, producto=producto ,existencias=request.GET['existencias'])
        existencia.save()

        existencias = Existencia.objects.filter(reporte_de_existencia=id_reporte).order_by('id')
        serialized = ExistenciaSerializer(existencias, many=True)
        return Response(serialized.data)

class GetExistenciasUpdate(APIView):
    def get(self, request):
        id_producto = int(request.GET['id_producto'])
        producto = Producto.objects.filter(id=id_producto).get()
        existencia = Existencia.objects.filter(id=request.GET['id']).update(producto=producto ,existencias=request.GET['existencias'])
        
        id_reporte = int(request.GET['id_reporte'])
        existencias = Existencia.objects.filter(reporte_de_existencia=id_reporte).order_by('id')
        serialized = ExistenciaSerializer(existencias, many=True)
        return Response(serialized.data)

class GetExistenciasDelete(APIView):
    def get(self, request):
        existencia = Existencia.objects.filter(id=request.GET['id']).delete()
        existencias = Existencia.objects.filter(reporte_de_existencia=request.GET['id_reporte']).order_by('id')
        serialized = ExistenciaSerializer(existencias, many=True)
        return Response(serialized.data)

class pdf_view(View):
    def get(self, request, pk):
        reporte = ReporteDeExistencia.objects.get(id=pk)

        reporte_serialized = ReporteDeExistenciaSerializer(reporte, many=False)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(reporte.__str__())

        buffer = BytesIO()

        styles = getSampleStyleSheet()
        styleN = styles["BodyText"]
        styleN.alignment = TA_LEFT
        styleBH = styles["Normal"]
        styleBH.alignment = TA_CENTER

        doc = SimpleDocTemplate(buffer, pagesize=letter)
        
        elements = []


        #Encabezado
        encabezado = Paragraph('''<b>HOTEL Y RESTAURANTE PUNTA ROCA OLAS</b>''', styleBH)
        subtitulo = Paragraph('''Reporte de existencias a la fecha 16/07/2018.<br/><br/>''', styleBH)

        # Headers
        hcod = Paragraph('''<b>Cod.</b>''', styleN)
        hdesc = Paragraph('''<b>Descripción</b>''', styleN)
        hcant = Paragraph('''<b>Cantidad</b>''', styleN)
        huni = Paragraph('''<b>Unidad</b>''', styleN)
        obs = Paragraph('''<br/><b>Observaciones:</b><br/>{}'''.format(reporte_serialized.data['observaciones']),styleN)

        data= [[hcod, hdesc, hcant, huni]]

        for i in range(len(reporte_serialized.data['existencias'])):
            e = reporte_serialized.data['existencias'][i]
            unidad_de_medida_producto = ''
            for unidad_de_medida in Producto.UNIDAD_DE_MEDIDA_CHOICES:
                if(unidad_de_medida[0] == e['producto']['unidad_de_medida'] ):
                    unidad_de_medida_producto = unidad_de_medida[1]
            
            data.append([e['producto']['id'], e['producto']['nombre'], e['existencias'], unidad_de_medida_producto])

        t = Table(data)
        t.setStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                    ('BOX', (0,0), (-1,-1), 0.25, colors.black)])

        elements.append(encabezado)
        elements.append(subtitulo)
        elements.append(t)
        elements.append(obs)
        doc.build(elements)
        response.write(buffer.getvalue())
        buffer.close()

        return response
