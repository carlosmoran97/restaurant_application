$(document).ready(function(){
  $("#tableOrdenes").DataTable({
    destroy: true,
  });
  $("#tableOrdenes_filter").hide();
  var fecha = new Date();
  $("#txtAnio").val(fecha.getFullYear());
  $("#tableOrdenes").DataTable().column(1).search($("#txtAnio").val()).draw();
});

//FILTROS
$(document).on("change", "#selectMes", function(){
  $("#tableOrdenes").DataTable().column(1).search($("#selectMes option:selected").text()).draw();
});
$(document).on("keyup", "#txtAnio", function(){
  $("#tableOrdenes").DataTable().column(1).search($("#txtAnio").val()).draw();
});
