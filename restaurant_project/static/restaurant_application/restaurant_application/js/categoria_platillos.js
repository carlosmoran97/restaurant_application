//Variable global para Editar y Eliminar
var idCategoriaPlatillo;

$(document).ready(function(){
  //Inicializar variables
  idCategoriaPlatillo = "";
  //alert('Funciona JQuery!');
  cargarDatos();
});

//FILTROS
$(document).on("keyup", "#txtBuscarCategoria", function(){
  $("#tableCategoria").DataTable().column(0).search($(this).val()).draw();
});

//Abrir Modal de Formulario de Registro de Categoría
$(document).on("click", "#btn-registrar-categoria", function(){
  idCategoriaPlatillo = "";
  $("#cargarForm").html($("#contenidoHTML1").html());
  $("#btn-guardar").attr({value:"/restaurant/create_categoria_platillos"});
  $("#labelModal").html("Registrar Categoría");
  $("#modal").modal("show");
});

//Abrir Ventana Modal Editar
$(document).on("click", ".editar", function(){
  idCategoriaPlatillo = $(this).attr("value");
  $("#cargarForm").html($("#contenidoHTML1").html());
  $("#txtCategoria").val($(this).parents("tr").find("td")[0].innerHTML);
  $("#btn-guardar").attr({value:"/restaurant/editar_categoria_platillos"});
  $("#labelModal").html("Editar Categoría");
  $("#modal").modal("show");
});

//Función para guardar el formulario
$(document).on("click", "#btn-guardar", function(){

  var parametros;
  if(idCategoriaPlatillo == ""){
    //En caso que sea Guardar
    parametros = {'categoria': $("#txtCategoria").val()};
  } else{
    //En caso que sea Editar
    parametros = {'idCategoriaPlatillo': idCategoriaPlatillo, 'categoria': $("#txtCategoria").val()};
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
  idCategoriaPlatillo = $(this).attr("value");
  $("#cargarForm").html($("#contenidoHTML2").html());
  $("#nombreCategoriaPlatillo").html($(this).parents("tr").find("td")[0].innerHTML);
  $("#labelModal").html("Eliminar Categoría");
  $("#modal").modal("show");
});

//Confirmar eliminar
$(document).on("click", "#btn-eliminar", function(){
  $.ajax({
    url : "/restaurant/eliminar_categoria_platillos",
    data : {'idCategoriaPlatillo': idCategoriaPlatillo},
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
    url : "/restaurant/lista_categoria_platillos",
    type: 'GET',
    dataType: "json",
    success : function (data) {
      $("#tableCategoria").DataTable({
        searching: true,
        destroy: true,
        data : data,
        ordering: false,
        columns: [
          { "data": "categoria"},
          { sortable: false,
            "render": function ( data, type, full, meta ) {
              var id = full.idCategoriaPlatillo;
              var htmlButton = '<button type=\"button\" class=\"btn btn-outline-success btn-sm editar\" value='+id+'><i class=\"fa fa-pencil\" aria-hidden=\"true\"></i></button>&nbsp;&nbsp;&nbsp';
              htmlButton += '<button type=\"button\" class=\"btn btn-outline-danger btn-sm eliminar\"  value='+id+'><i class="fa fa-times" aria-hidden="true"></i></button>';
                return htmlButton;
          }},
        ]
      });
      $("#tableCategoria_filter").hide();
    }
  });
};
