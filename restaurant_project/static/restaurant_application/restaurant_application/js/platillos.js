//Variable global para Editar y Eliminar
var codigoPlatillo;

$(document).ready(function(){
  //Inicializar variables
  codigoPlatillo = "";
  //alert('Funciona JQuery!');
  cargarDatos();
});

//FILTROS
$(document).on("keyup", "#txtBuscarCodigo", function(){
  $("#tablePlatillos").DataTable().column(0).search($(this).val()).draw();
});
$(document).on("keyup", "#txtBuscarNombre", function(){
  $("#tablePlatillos").DataTable().column(1).search($(this).val()).draw();
});
$(document).on("keyup", "#txtBuscarPrecioUnitario", function(){
  $("#tablePlatillos").DataTable().column(2).search($(this).val()).draw();
});
$(document).on("change", "#selectCategoriaPlatilloBuscar", function(){
  if($(this).val() == ""){
    cargarDatos();
  } else{
    $("#tablePlatillos").DataTable().column(3).search($("#selectCategoriaPlatilloBuscar option:selected").text()).draw();
  }
});

//Abrir Modal de Formulario de Registro de Platillo
$(document).on("click", "#btn-registrar-platillo", function(){
  codigoPlatillo = "";
  $("#cargarForm").html($("#contenidoHTML1").html());
  $("#btn-guardar").attr({value:"/restaurant/create_platillos"});
  $("#btn-guardar-otro").attr({value:"/restaurant/create_platillos"});
  $("#labelModal").html("Registrar Platillo");
  $("#modal").modal("show");
});

//Abrir Ventana Modal Editar
$(document).on("click", ".editar", function(){
  codigoPlatillo = $(this).attr("value");
  $("#cargarForm").html($("#contenidoHTML1").html());
  $("#txtNombre").val($(this).parents("tr").find("td")[1].innerHTML);
  $("#txtPrecioUnitario").val($(this).parents("tr").find("td")[2].innerHTML);
  //$("#selectCategoriaPlatillo").val($(this).parents("tr").attr("value"));
  $("#selectCategoriaPlatillo").val($(this).attr("id"));
  $("#btn-guardar").attr({value:"/restaurant/editar_platillos"});
  $("#btn-guardar-otro").attr({value:"/restaurant/editar_platillos"});
  $("#labelModal").html("Editar Platillo");
  $("#modal").modal("show");
});

//Función para guardar el formulario
$(document).on("click", "#btn-guardar", function(){
  var parametros;
  if(codigoPlatillo == ""){
    //En caso que sea Guardar
    parametros = {'nombre': $("#txtNombre").val(), 'precioUnitario':parseFloat($("#txtPrecioUnitario").val()).toFixed(2), 'categoria_platillo':$("#selectCategoriaPlatillo").val()};
  } else{
    //En caso que sea Editar
    parametros = {'codigoPlatillo':codigoPlatillo, 'nombre': $("#txtNombre").val(), 'precioUnitario':parseFloat($("#txtPrecioUnitario").val()).toFixed(2), 'categoria_platillo':$("#selectCategoriaPlatillo").val()};
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
// funcion para guardar y añadir otro
$(document).on("click", "#btn-guardar-otro", function(){
  var parametros;
  if(codigoPlatillo == ""){
    //En caso que sea Guardar
    parametros = {'nombre': $("#txtNombre").val(), 'precioUnitario':parseFloat($("#txtPrecioUnitario").val()).toFixed(2), 'categoria_platillo':$("#selectCategoriaPlatillo").val()};
  } else{
    //En caso que sea Editar
    parametros = {'codigoPlatillo':codigoPlatillo, 'nombre': $("#txtNombre").val(), 'precioUnitario':parseFloat($("#txtPrecioUnitario").val()).toFixed(2), 'categoria_platillo':$("#selectCategoriaPlatillo").val()};
  }

  $.ajax({
    url : $(this).attr("value"),
    data : parametros,
    type: "GET",
    dataType: "json",
    success : function (data) {
      cargarDatos();

      codigoPlatillo = "";
      $("#cargarForm").html($("#contenidoHTML1").html());
      $("#btn-guardar-otro").attr({value:"/restaurant/create_platillos"});
    }
  });
});

//Abrir ventana eliminar
$(document).on("click", ".eliminar", function(){
  codigoPlatillo = $(this).attr("value");
  $("#cargarForm").html($("#contenidoHTML2").html());
  $("#nombrePlatillo").html($(this).parents("tr").find("td")[1].innerHTML);
  $("#labelModal").html("Eliminar Platillo");
  $("#modal").modal("show");
});

//Confirmar eliminar
$(document).on("click", "#btn-eliminar", function(){
  $.ajax({
    url : "/restaurant/eliminar_platillos",
    data : {'codigoPlatillo': codigoPlatillo},
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
    url : "/restaurant/lista_platillos",
    type: 'GET',
    dataType: "json",
    success : function (data) {
      $("#tablePlatillos").DataTable({
        destroy: true,
        data : data,
        ordering: false,
        columns: [
          { "data": "codigoPlatillo" },
          { "data": "nombre" },
          { "data": "precioUnitario" },
          { "data": "categoria_platillo.categoria" },
          { sortable: false,
            "render": function ( data, type, full, meta ) {
              var id = full.codigoPlatillo;
              var categoria = full.categoria_platillo.idCategoriaPlatillo;
              var htmlButton = '<button type=\"button\" class=\"btn btn-outline-success btn-sm editar\" value='+id+' id='+categoria+'><i class=\"fa fa-pencil\" aria-hidden=\"true\"></i></button>&nbsp;&nbsp;&nbsp';
              htmlButton += '<button type=\"button\" class=\"btn btn-outline-danger btn-sm eliminar\"  value='+id+'><i class="fa fa-times" aria-hidden="true"></i></button>';
                return htmlButton;
          }},
        ]
      });
      $("#tablePlatillos_filter").hide();
    }
  });
}
