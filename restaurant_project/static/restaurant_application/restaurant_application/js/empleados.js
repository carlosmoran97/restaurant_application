//Variable global para Editar y Eliminar
var idAsignacion;
var empleado;

$(document).ready(function(){
  //Inicializar variables
  idAsignacion = "";
  empleado = {};
  //alert('Funciona JQuery!');
  cargarDatos();
});

//FILTROS
$(document).on("keyup", "#txtBuscarCodigo", function(){
  $("#tableEmpleados").DataTable().column(0).search($(this).val()).draw();
});
$(document).on("keyup", "#txtBuscarNombre", function(){
  $("#tableEmpleados").DataTable().column(1).search($(this).val()).draw();
});
$(document).on("keyup", "#txtBuscarApellido", function(){
  $("#tableEmpleados").DataTable().column(2).search($(this).val()).draw();
});
$(document).on("change", "#selectPuestoBuscar", function(){
  if($(this).val() == ""){
    cargarDatos();
  } else{
    $("#tableEmpleados").DataTable().column(3).search($("#selectPuestoBuscar option:selected").text()).draw();
  }
});

//Abrir Modal de Formulario de Registro de Empleado
$(document).on("click", "#btn-registrar-empleado", function(){
  idAsignacion = "";
  $("#cargarForm").html($("#contenidoHTML1").html());
  $(".modal-dialog").attr("class", "modal-dialog modal-lg");
  $(".cancelar").attr("data-dismiss", "modal");
  $("#btn-guardar").attr({value:"/restaurant/create_empleado"});
  $("#fecha_nacimiento").datepicker({dateFormat: 'dd/mm/yy'});
  $("#fecha_contratacion").datepicker({dateFormat: 'dd/mm/yy'});
  $("#labelModal").html("Registrar Empleado");
  $("#modal").modal("show");
});

function verDetalleEmpleado(){
  $("#cargarForm").html($("#contenidoHTML2").html());
  $(".modal-dialog").attr("class", "modal-dialog modal-lg");
  $("#labelModal").html("Detalle de Empleado");
  $.ajax({
    url : "/restaurant/detalle_empleado",
    data : {'id': idAsignacion},
    type: "GET",
    dataType: "json",
    success : function (data) {
      $("#lblNombre").html(data[0].empleado.nombre);
      $("#lblApellido").html(data[0].empleado.apellido);
      var fecha_nacimiento = data[0].empleado.fecha_nacimiento;
      data[0].empleado.fecha_nacimiento = fecha_nacimiento.substr(8,2)+"/"+fecha_nacimiento.substr(5,2)+"/"+fecha_nacimiento.substr(0,4);
      $("#lblFechaNacimiento").html(data[0].empleado.fecha_nacimiento);
      $("#lblDUI").html(data[0].empleado.dui.substr(0, 8)+'-'+data[0].empleado.dui.substr(8, 1));
      $("#lblNIT").html(data[0].empleado.nit.substr(0, 4)+'-'+data[0].empleado.nit.substr(4, 6)+'-'+data[0].empleado.nit.substr(10, 3)+'-'+data[0].empleado.nit.substr(13, 1));
      $("#lblAFP").html(data[0].empleado.afp);
      $("#lblPuesto").html(data[0].puesto.puesto);
      $("#lblSalario").html(data[0].salario);
      var fecha_contratacion = data[0].fecha_contratacion;
      data[0].fecha_contratacion = fecha_contratacion.substr(8,2)+"/"+fecha_contratacion.substr(5,2)+"/"+fecha_contratacion.substr(0,4);
      $("#lblFechaContratacion").html(data[0].fecha_contratacion);
      empleado = data;
      $("#modal").modal("show");
    }
  });
}

//Abrir Ventana Modal Ver
$(document).on("click", ".ver", function(){
  idAsignacion = $(this).attr("value");
  verDetalleEmpleado();
})

$(document).on("click", '.cancelar', function(){
  verDetalleEmpleado();
});

//Mostrar Formulario Editar
$(document).on("click", "#btn-editar", function(){
  $("#labelModal").html("Editar Empleado");
  $("#cargarForm").html($("#contenidoHTML1").html());
  $("#labelModal").html("Editar Empleado");
  $("#btn-guardar").attr({value:"/restaurant/editar_empleado"});
  $("#txtNombre").val(empleado[0].empleado.nombre);
  $("#txtApellido").val(empleado[0].empleado.apellido);
  $("#fecha_nacimiento").datepicker({dateFormat: 'dd/mm/yy'});
  $("#fecha_nacimiento").val(empleado[0].empleado.fecha_nacimiento);
  $("#txtDUI").val(empleado[0].empleado.dui);
  $("#txtNIT").val(empleado[0].empleado.nit);
  $("#txtAFP").val(empleado[0].empleado.afp);
  $("#selectPuesto").val(empleado[0].puesto.idPuesto);
  $("#txtSalario").val(empleado[0].salario);
  $("#fecha_contratacion").datepicker({dateFormat: 'dd/mm/yy'});
  $("#fecha_contratacion").val(empleado[0].fecha_contratacion);
});

//Función para guardar el formulario
$(document).on("click", "#btn-guardar", function(){
  var fecha_nacimiento = formatFecha($("#fecha_nacimiento").datepicker('getDate'));
  var fecha_contratacion = formatFecha($("#fecha_contratacion").datepicker('getDate'));
  var nombre = $("#txtNombre").val();
  var apellido = $("#txtApellido").val();
  var dui = $("#txtDUI").val();
  var nit = $("#txtNIT").val();
  var afp = $("#txtAFP").val();
  var idPuesto = $("#selectPuesto").val();
  var salario = $("#txtSalario").val();
  var parametros;
  if(idAsignacion == ""){
    //En caso que sea Guardar
    parametros = {'nombre': nombre,
      'apellido': apellido,
      'fecha_nacimiento': fecha_nacimiento,
      'dui': dui,
      'nit': nit,
      'afp': afp,
      'idPuesto': idPuesto,
      'salario': salario,
      'fecha_contratacion': fecha_contratacion
    };

  } else{
    //En caso que sea Editar
    parametros = {
      'id': empleado[0].id,
      'idEmpleado': empleado[0].empleado.idEmpleado,
      'nombre': nombre,
      'apellido': apellido,
      'fecha_nacimiento': fecha_nacimiento,
      'dui': dui,
      'nit': nit,
      'afp': afp,
      'idPuesto': idPuesto,
      'salario': salario,
      'fecha_contratacion': fecha_contratacion
    };
  }

  $.ajax({
    url : $(this).attr("value"),
    data : parametros,
    type: "GET",
    dataType: "json",
    success : function (data) {
      //alert('Registrado '+data.respuesta);
      if(idAsignacion == ""){
        $("#modal").modal("hide");
      } else{
        verDetalleEmpleado();
      }
      cargarDatos();
    }
  });
});

//Abrir ventana eliminar
$(document).on("click", "#btn-ver-eliminar", function(){
  $("#cargarForm").html($("#contenidoHTML3").html());
  $("#labelModal").html("Eliminar Empleado");
  $("#nombreEmpleado").html(empleado[0].empleado.nombre+" "+empleado[0].empleado.apellido);
});

//Confirmar eliminar
$(document).on("click", "#btn-eliminar", function(){
  $.ajax({
    url : "/restaurant/eliminar_empleado",
    data : {'idEmpleado': empleado[0].empleado.idEmpleado, 'id':empleado[0].id},
    type: "GET",
    dataType: "json",
    success : function (data) {
      //alert('Eliminar '+data.respuesta);
      $("#modal").modal("hide");
      cargarDatos();
    }
  });
});

//Funcion cargar lista
function cargarDatos(){
  $.ajax({
    url : "/restaurant/lista_empleados",
    type: 'GET',
    dataType: "json",
    success : function (data) {
      dataE = data;
      $("#tableEmpleados").DataTable({
        destroy: true,
        data : data,
        ordering: false,
        columns: [
          { "data": "empleado.idEmpleado" },
          { "data": "empleado.nombre" },
          { "data": "empleado.apellido" },
          { "data": "puesto.puesto" },
          { sortable: false,
            "render": function ( data, type, full, meta ) {
              var id = full.id;
              var htmlButton = '<button type=\"button\" class=\"btn btn-outline-info btn-sm ver\" value='+id+'><i class="fa fa-eye" aria-hidden="true"></i></button>';
                return htmlButton;
          }},
        ]
      });
      $("#tableEmpleados_filter").hide();
    }
  });
}

//Dar formato a fecha
function formatFecha(fecha){
  return fecha.getFullYear()+"-"+(fecha.getMonth()+1)+"-"+fecha.getDate();
}
