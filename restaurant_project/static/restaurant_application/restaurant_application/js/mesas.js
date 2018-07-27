//Variable global para Editar y Eliminar
var codigo_mesa;

$(document).ready(function(){
  //Inicializar variables
  codigo_mesa = "";
  //alert('Funciona JQuery!');
  cargarDatos();
});

//FILTROS
$(document).on("keyup", "#txtBuscarNumeroMesa", function(){
  $("#tableMesas").DataTable().column(0).search($(this).val()).draw();
});
$(document).on("keyup", "#txtBuscarAsientos", function(){
  $("#tableMesas").DataTable().column(1).search($(this).val()).draw();
});

//Abrir Modal de Formulario de Registro de Categoría
$(document).on("click", "#btn-registrar-mesa", function(){
  codigo_mesa = "";
  $("#cargarForm").html($("#contenidoHTML1").html());
  $("#btn-guardar").attr({value:"/restaurant/create_mesas"});
  $("#labelModal").html("Registrar Mesa");
  $("#modal").modal("show");
});

//Abrir Ventana Modal Editar
$(document).on("click", ".editar", function(){
  codigo_mesa = $(this).attr("value");
  $("#cargarForm").html($("#contenidoHTML1").html());
  $("#txtNumeroMesa").val($(this).parents("tr").find("td")[0].innerHTML);
  $("#txtAsientos").val($(this).parents("tr").find("td")[1].innerHTML);
  $("#btn-guardar").attr({value:"/restaurant/editar_mesas"});
  $("#labelModal").html("Editar Mesa");
  $("#modal").modal("show");
});

//Función para guardar el formulario
$(document).on("click", "#btn-guardar", function(){

  var parametros;
  if(codigo_mesa == ""){
    //En caso que sea Guardar
    parametros = {'numero_mesa': $("#txtNumeroMesa").val(), 'asientos':parseFloat($("#txtAsientos").val())};
  } else{
    //En caso que sea Editar
    parametros = {'codigo_mesa':codigo_mesa,'numero_mesa': $("#txtNumeroMesa").val(), 'asientos':parseFloat($("#txtAsientos").val())};
  }

  $.ajax({
    url : $(this).attr("value"),
    data : parametros,
    type: "GET",
    dataType: "json",
    success : function (data) {
      //alert('Registrado '+data.respuesta);
      $("#modal").modal("hide");
      cargarDatos();
    }
  });
});

//Abrir ventana eliminar
$(document).on("click", ".eliminar", function(){
  codigo_mesa = $(this).attr("value");
  $("#cargarForm").html($("#contenidoHTML2").html());
  $("#numeroMesa").html($(this).parents("tr").find("td")[0].innerHTML);
  $("#labelModal").html("Eliminar Mesa");
  $("#modal").modal("show");
});

//Confirmar eliminar
$(document).on("click", "#btn-eliminar", function(){
  $.ajax({
    url : "/restaurant/eliminar_mesas",
    data : {'codigo_mesa': codigo_mesa},
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
    url : "/restaurant/lista_mesas",
    type: 'GET',
    dataType: "json",
    success : function (data) {
      $("#tableMesas").DataTable({
        destroy: true,
        data : data,
        ordering: false,
        columns: [
          { "data": "numero_mesa" },
          { "data": "asientos" },
          { sortable: false,
            "render": function ( data, type, full, meta ) {
              var id = full.codigo_mesa;
              var htmlButton = '<button type=\"button\" class=\"btn btn-outline-success btn-sm editar\" value='+id+'><i class=\"fa fa-pencil\" aria-hidden=\"true\"></i></button>&nbsp;&nbsp;&nbsp';
              htmlButton += '<button type=\"button\" class=\"btn btn-outline-danger btn-sm eliminar\"  value='+id+'><i class="fa fa-times" aria-hidden="true"></i></button>';
                return htmlButton;
          }},
        ]
      });
      $("#tableMesas_filter").hide();
    }
  });
}
