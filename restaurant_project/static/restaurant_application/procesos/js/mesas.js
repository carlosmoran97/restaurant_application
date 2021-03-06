var codigo_mesa;
var orden_id;
$(document).ready(() => {
    codigo_mesa = "";
    orden_id = "";
    $.ajax({
        url: "/restaurant/lista_mesas",
        type: 'GET',
        dataType: 'json',
        success: (data) => {
            let html = ``;
            for(let i = 0; i < data.length; i++)
            {
                html += `<div class="card text-white `;

                if(!data[i].ocupado){
                    html += `bg-success mb-3 mesa-card" style="max-width: 18rem;" id="${data[i].codigo_mesa}" value="desocupada">`;
                }
                else{
                    html += `bg-danger mb-3 mesa-card" style="max-width: 18rem;" id="${data[i].codigo_mesa}" value="ocupada">`;
                }

                html +=`      <div class="card-header">Mesa ${data[i].numero_mesa}</div>
                                <div class="card-body">
                                    <div class="card-text">
                                        <i class="fa fa-cutlery fa-4x" aria-hidden="true"></i>
                                    </div>
                                </div>
                            </div>`;
                $('#mesas').html(html);
            }
        }
    });
});

$(document).on("click", ".mesa-card", function(){
  codigo_mesa = $(this).attr("id");
  if($(this).attr("value") == "ocupada"){
    $.ajax({
      url: "/procesos/detail_orden_mesa",
      data: {codigo_mesa: codigo_mesa},
      type: 'GET',
      dataType: 'json',
      success: function(data){
        orden_id = data[0].id;
      }
    });

    $("#cargarForm").html(`
                            <div class="modal-body">
                                <h3>Está mesa se encuentra ocupada, <strong>¿Desea ver la orden de está mesa?</strong></h3>
                            </div>
                            <div class="modal-footer">
                              <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
                              <button id="btn-ver" type="button" class="btn btn-primary">Ver</button>
                            </div>
                          `);
    $("#labelModal").html("Mesa Ocupada");
  }else{
    $("#cargarForm").html($("#contenidoHTML1").html());
    $("#labelModal").html("Abrir Orden");
  }
  $.ajax({
    url: "/restaurant/lista_empleados",
    type: "get",
    dataType: "json",
    success: function(data)
    {
      html = `<option value="" selected>-------</option>`;
      for(let i = 0; i < data.length; i++)
      {
        if(data[i].puesto.puesto.toLowerCase() == "mesero"){
          html += `<option value="${data[i].empleado.idEmpleado}">${data[i].empleado.nombre} ${data[i].empleado.apellido}</option>`;
        }
      }
      $("#selectMesero").html(html);
    }
  });
  $("#modal").modal("show");
});

$(document).on("click", "#btn-guardar", function(){
  $.ajax({
    url : "/procesos/abrir_orden",
    data : {
      idEmpleado: $("#selectMesero").val(),
      codigo_mesa: codigo_mesa,
      cliente: $("#txtNombreCliente").val(),
      comentario: $("#txtComentario").val()},
    type: "GET",
    dataType: "json",
    success : function (data) {
      window.location.href = "/procesos/detalle_orden/"+data.respuesta+"/";
    }
  });
});
$(document).on("click", "#btn-ver", function(){
  window.location.href = "/procesos/detalle_orden/"+orden_id+"/";
});
