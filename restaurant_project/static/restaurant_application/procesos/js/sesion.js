//Variable global para Editar y Eliminar
var idSesion;
$(document).ready(function(){
  //Inicializar variables
  idSesion = "";
  //alert('Funciona JQuery!');
  cargarDatos();

});

//Abrir Modal de Formulario de Registro de Sesión Caja
$(document).on("click", "#btn-registrar-sesión", function(){
  $("#cargarForm").html($("#contenidoHTML1").html());
  $("#btn-guardar").attr({value:"/procesos/create_sesion_caja"});
  $("#labelModal").html("Iniciar Sesión Caja");
  // cargando los cajeros
  $.ajax({
    url: "/restaurant/lista_empleados",
    type: "get",
    dataType: "json",
    success: function(data)
    {
      html = '<option value="" selected>-------</option>';
      for(var i=0; i < data.length; i++)
      {
        if(data[i].puesto.puesto.toLowerCase() == "cajero"){
          html += '<option value=\"'+data[i].empleado.idEmpleado+'\">'+data[i].empleado.nombre+' '+data[i].empleado.apellido+'</option>';
        }
      }
      $("#selectCajero").html(html);
    }
  });
  $("#modal").modal("show");
});


//Función para guardar el formulario
$(document).on("click", "#btn-guardar", function(){
  $.ajax({
    url : $(this).attr("value"),
    data : {numero_caja: $("#selectCaja").val(), idEmpleado: $("#selectCajero").val(), monto_apertura: $("#txtMontoApertura").val()},
    type: "GET",
    dataType: "json",
    success : function (data) {
      //alert('Registrado '+data.respuesta);
      $("#modal").modal("hide");
      cargarDatos();
    },
    error: function (xhr, ajaxOptions, thrownError) {
      if(xhr.responseText.includes("sesión activa"))
      {
        alert("El cajero seleccionado ya tiene una sesión activa");
      }
      else{
        alert(xhr.responseText);
      }
    }
  });
});

$(document).on("click", ".ver", function(){
  idSesion = $(this).attr("value");
  $("#cargarForm").html($("#contenidoHTML2").html());
  $(".modal-dialog").attr("class", "modal-dialog modal-lg");
  $("#labelModal").html("Detalle de Caja");

  $.ajax({
    url : "/procesos/detalle_sesion_caja",
    data: {id: idSesion},
    type: 'GET',
    dataType: "json",
    success : function (data) {
      //console.log(data);
      $("#lblEmpleado").html(data[0].cajero.nombre+" "+data[0].cajero.apellido);
      $("#lblCaja").html(data[0].caja.numero_caja);
      $("#lblApertura").html(formatFecha(new Date(data[0].fecha_apertura)));
      if(data[0].fecha_cierre == null){
        $("#lblCierre").html("");
      } else{
        $("#lblCierre").html(formatFecha(new Date(data[0].fecha_cierre)));
      }
      $("#lblMontoApertura").html("$ "+data[0].monto_apertura);
      $("#lblMontoEstimado").html("$ "+data[0].monto_estimado);
      $("#lblMontoReal").html("$ "+data[0].monto_real);
      $("#lblDiferencia").html("$ "+data[0].diferencia);
      $("#lblEstado").html(data[0].estado);
    }
  });

  $("#modal").modal("show");
});

//Abrir ventana para calcular cerrar
$(document).on("click", ".cerrar", function(){
  idSesion = $(this).attr("value");
  $("#cargarForm").html($("#contenidoHTML3").html());
  $("#labelModal").html("Cerrar Sesión Caja");
  $("#modal").modal("show");
});

$(document).on("click", "#btn-confirmar-cerrar", function(){
  $.ajax({
    url : "/procesos/cerrar_sesion_caja",
    data : {id: idSesion, monto_real: $("#txtMontoReal").val()},
    type: "GET",
    dataType: "json",
    success : function (data) {
      //alert('Registrado '+data.respuesta);
      $("#modal").modal("hide");
      cargarDatos();
    }
  });
});

//Funcion cargar lista
function cargarDatos(){
  $.ajax({
    url : "/procesos/lista_sesion_caja",
    type: 'GET',
    dataType: "json",
    success : function (data) {
      //console.log(data);
      $("#tableSesion").DataTable({
        destroy: true,
        data : data,
        ordering: false,
        columns: [
          { "data": "id" },
          { "data": "caja.numero_caja" },
          { sortable: false,
            "render": function ( data, type, full, meta ) {
              var nombre = full.cajero.nombre;
              var apellido = full.cajero.apellido;
              var nombre_completo = nombre+' '+apellido;
                return nombre_completo;
          }},
          { sortable: false,
            "render": function ( data, type, full, meta ) {
                return formatFecha(new Date(full.fecha_apertura));
          }},
          { sortable: false,
            "render": function ( data, type, full, meta ) {
                if(full.fecha_cierre == null){
                  return "";
                } else{
                  return formatFecha(new Date(full.fecha_cierre));
                }
          }},
          { "data": "estado" },
          { sortable: false,
            "render": function ( data, type, full, meta ) {
              var id = full.id;
              var htmlButton = '<button type=\"button\" class=\"btn btn-outline-info btn-sm ver\" value='+id+'><i class="fa fa-eye" aria-hidden="true"></i></button>&nbsp;&nbsp;&nbsp;';
              if(full.estado == "Abierta"){
                htmlButton += '<button type=\"button\" class=\"btn btn-outline-danger btn-sm cerrar\" value='+id+'><i class="fa fa-lock" aria-hidden="true"></i></button>';
              }
                return htmlButton;
          }},
        ]
      });
      $("#tableSesion_filter").hide();
    }
  });
}

//Dar formato a fecha
function formatFecha(fecha){
  return fecha.getFullYear()+"-"+(fecha.getMonth()+1)+"-"+fecha.getDate()+" "+fecha.getHours()+":"+fecha.getMinutes()+":"+fecha.getSeconds();
}
