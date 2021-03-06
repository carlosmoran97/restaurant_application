
    //Variable codigoPlatillo
    var codigoPlatillo;
    var idDetalleGuardado;
    var accion;
    var idDetalle;
    var contadorClick;
    var clickEliminar;

    $(document).ready(function(){
      codigoPlatillo = "";
      accion = "";
      idDetalleGuardado = "";
      idDetalle = "";
      contadorClick = 0;
      clickEliminar = 0;
      llenarCategorias();
      cargarListaDetalles();
    });

    //Agregar platillos
    $(document).on("click", ".platillo-card", function(){
      var codigoPlatillo = $(this).attr("value");
      var validar = false;
      for(var i = 0; i < $(".platillo_select").toArray().length; i++){
        if($(".platillo_select:eq("+i+")").attr("value") == codigoPlatillo){
          var cantidad = parseInt($(".platillo_select #lblCantidad:eq("+i+")").html());
          cantidad++;
          $(".platillo_select #lblCantidad:eq("+i+")").html(cantidad);
          idDetalle = i;
          calcularPrecio();
          validar = true;
          var descuento = 0;
          if($(".platillo_select #porcentajeDescuento:eq("+i+")").html() != ""){
            decuento = $(".platillo_select #porcentajeDescuento:eq("+i+")").html();
          }
          var id = $(".platillo_select .col-12:eq("+i+")").attr("id");
          var precio = $(".platillo_select #lblPrecioUnitario:eq("+i+")").html();
          calcularEntregados();
          var ordenados = $(".platillo_select #ordenados:eq("+idDetalle+")").html();
          var entregados = $(".platillo_select #entregados:eq("+idDetalle+")").html();

          actualizar(id, cantidad, precio, descuento, ordenados, entregados);
        }
      }

      if(!validar){
        $.ajax({
          url : "/restaurant/platillo_detail",
          data : {codigoPlatillo: codigoPlatillo},
          type: "GET",
          dataType: "json",
          success : function (data) {
            var parametros = {
              id: object_id_recibido,
              codigoPlatillo: codigoPlatillo,
              precio: data[0].precioUnitario,
            };

            $.ajax({
              url : "/procesos/create_detalle_orden",
              data : parametros,
              type: "GET",
              dataType: "json",
              success: function(data_create) {
                var cont = $(".platillo_select").toArray().length++;
                var htmlRow = `<div id="${cont}" class="row platillo_select" value="${data[0].codigoPlatillo}">
                                  <div id="${data_create.id}" class="col-12" value="registrado">
                                    <div class="row">
                                      <div class="col-8">
                                        <label id="lblNombrePlatillo">${data[0].nombre}</label>
                                      </div>
                                      <div class="col-4">
                                        <label class="sobre">$&nbsp;<span id="lblPrecio">${(parseFloat(data[0].precioUnitario).toFixed(2))}</span></label>
                                      </div>
                                    </div>
                                    <div class="row">
                                      <div class="col-3">
                                        <label class="sobre">cant: <span id="lblCantidad">1</span></label>
                                      </div>
                                      <div class="col-4">
                                        <label class="sobre">$&nbsp;<span id="lblPrecioUnitario">${data[0].precioUnitario}</span>&nbsp;c/u</label>
                                      </div>
                                      <div class="col-4">
                                        <label class="sobre"><span id="porcentajeDescuento"></span><span id="lblDescuento"></span></label>
                                      </div>
                                    </div>
                                    <div class="row">
                                      <div class="col-7">
                                        <label class="sobre">En espera: <span class="badge badge-success" id="ordenados">1</span></label>
                                      </div>
                                      <div class="col-5">
                                        <label class="sobre">Ordenados: <span class="badge badge-success" id="entregados">0</span></label>
                                      </div>
                                    </div>
                                  </div>
                                 </div>`;
                  $("#agregandoPlatillos").html($("#agregandoPlatillos").html()+htmlRow);
                  idDetalle = cont;
                  calcularPrecio();
              }
            });

          }
        });
      }
    });

    //Actualizar
    function actualizar(id, cantidad, precio, descuento, ordenados, entregados){
      $.ajax({
        url : "/procesos/update_detalle_orden",
        data : {
          id: id,
          cantidad: cantidad,
          precio: precio,
          descuento: descuento,
          ordenados: ordenados,
          entregados: entregados
        },
        type: "GET",
        dataType: "json",
        success: function (data) {
          //alert("Actualizado"+data.respuesta);
        }
      });
    }

    //Cargar la lista de los guardados anteriormente
    function cargarListaDetalles(){
      $("#agregandoPlatillos").html("");
      $.ajax({
        url : "/procesos/detail_detalle_orden",
        data : {id: object_id_recibido},
        type: "GET",
        dataType: "json",
        success : function (data) {
          var htmlRegistrado = "";
          for(var i = 0; i < data.length; i++){
            htmlRegistrado = `<div id="${$(".platillo_select").toArray().length++}" class="row platillo_select" value="${data[i].consumible.codigoPlatillo}">
                                <div id="${data[i].id}" class="col-12" value="registrado">
                                  <div class="row">
                                    <div class="col-8">
                                      <label id="lblNombrePlatillo">${data[i].consumible.nombre}</label>
                                    </div>
                                    <div class="col-4">
                                      <label class="sobre">$&nbsp;<span id="lblPrecio"></span></label>
                                    </div>
                                  </div>
                                  <div class="row">
                                    <div class="col-3">
                                      <label class="sobre">cant: <span id="lblCantidad">${data[i].cantidad}</span></label>
                                    </div>
                                    <div class="col-4">
                                      <label class="sobre">$&nbsp;<span id="lblPrecioUnitario">${data[i].precio_de_venta}</span>&nbsp;c/u</label>
                                    </div>
                                    <div class="col-4">
                                      <label>
                                        <span class="sobre" id="porcentajeDescuento">`;
                                        if(data[i].descuento != 0){
                                          htmlRegistrado += data[i].descuento+`</span><span class="sobre" id="lblDescuento">% desc</span>`;
                                        } else{
                                          htmlRegistrado += `</span><span class="sobre" id="lblDescuento"></span>`;
                                        }

                                        htmlRegistrado += `

                                      </label>
                                    </div>
                                  </div>
                                  <div class="row">
                                    <div class="col-7">
                                      <label class="sobre">En espera: <span class="badge badge-success" id="ordenados">${data[i].ordenados}</span></label>
                                    </div>
                                    <div class="col-5">
                                      <label class="sobre">Ordenados: <span class="badge badge-success" id="entregados">${data[i].entregados}</span></label>
                                    </div>
                                  </div>
                                </div>
                               </div>`;
                               idDetalle = i;
                               $("#agregandoPlatillos").html($("#agregandoPlatillos").html()+htmlRegistrado);
                               calcularPrecio();

          }
        }
      });
    }

    //Seleccionar platillo en detalle orden
    $(document).on("click", ".platillo_select", function(){
      idDetalle = $(this).attr("id");
      idDetalleGuardado = $(".platillo_select .col-12:eq("+idDetalle+")").attr("id");
      $(".platillo_select").removeClass("platillo_select_elegido");
      $(this).addClass("platillo_select_elegido");
      removerClass();
      $("#opcion-cantidad").addClass("opcion-seleccionada");
      accion = "cantidad";
      contadorClick = 1;
    });

    //Cambiar de color en las siguientes opciones
    $(document).on("click", ".opcion", function(){
      removerClass();
      $(this).addClass("opcion-seleccionada");
      accion = $(this).attr("value");
      contadorClick = 1;
    });

    //Agregar Número
    $(document).on("click", ".opcion-numero", function(){
      if(idDetalleGuardado == ""){
        //alert("No se puede");
        noSeleccionado();
      } else{
        if (accion == "cantidad"){
          var cantidad_dom = $(".platillo_select #lblCantidad:eq("+idDetalle+")");
          if(contadorClick == 1){
            if($(this).attr("value") == "."){
              cantidad_dom.html("0");
            } else{
              cantidad_dom.html($(this).attr("value"));
            }
            contadorClick++;
          } else if($(this).attr("value") == "."){
            cantidad_dom.html(cantidad_dom.html()+"");
          } else{
            cantidad_dom.html(cantidad_dom.html()+$(this).attr("value"));
          }

          if(cantidad_dom.html().length > 1){
            if(cantidad_dom.html().charAt(0) == "0" || cantidad_dom.html().charAt(0) == "."){
              cantidad_dom.html(cantidad_dom.html().substr(1, cantidad_dom.html().length));
            }
          }
          clickEliminar = 0;

        } else if (accion == "precio") {
          var precio_dom = $(".platillo_select #lblPrecioUnitario:eq("+idDetalle+")");
          if(contadorClick == 1){
            if($(this).attr("value") == "."){
              precio_dom.html("0.");
            } else{
              precio_dom.html($(this).attr("value"));
            }
            contadorClick++;
          } else if(precio_dom.html().indexOf(".") == -1){
            precio_dom.html(precio_dom.html()+$(this).attr("value"));
          } else{
            if($(this).attr("value") != "."){
              precio_dom.html(precio_dom.html()+$(this).attr("value"));
            }
          }

          if(precio_dom.html().length > 1){
            if(precio_dom.html().charAt(0) == "0"){
              precio_dom.html(precio_dom.html().substr(1, precio_dom.html().length));
            }
          }
          if(precio_dom.html().charAt(0) == "."){
            precio_dom.html("0");
          }
          clickEliminar = 0;
        } else if (accion == "descuento") {
          var descuento_dom = $(".platillo_select #porcentajeDescuento:eq("+idDetalle+")");
          var desc;
          var simbolo_agregado;
          if(contadorClick == 1){
            desc = "";
            if($(this).attr("value") == "."){
              simbolo_agregado = "0.";
            } else{
              simbolo_agregado = $(this).attr("value");
            }
            contadorClick++;
          } else if(descuento_dom.html().indexOf(".") == -1){
            desc = descuento_dom.html();
            simbolo_agregado = $(this).attr("value");
          } else{
            desc = descuento_dom.html();
            if($(this).attr("value") != "."){
              simbolo_agregado = $(this).attr("value");
            } else{
              simbolo_agregado = "";
            }
          }
          descuento_dom.html(desc+simbolo_agregado);
          $(".platillo_select #lblDescuento:eq("+idDetalle+")").html("% desc");
          if(descuento_dom.html().length > 1){
            if(descuento_dom.html().charAt(0) == "0" || descuento_dom.html().charAt(0) == "."){
              descuento_dom.html(descuento_dom.html().substr(1, descuento_dom.html().length));
            }
          }
          if(descuento_dom.html().charAt(0) == "."){
            descuento_dom.html("0");
          }
          clickEliminar = 0;
        }

        guardarCambios();
      }
    });

    function noSeleccionado(){
      $("#cargarForm").html(`
                              <div class="modal-body">
                                  <h3><strong>No se ha seleccionado detalle.</strong></h3>
                              </div>
                              <div class="modal-footer">
                              </div>
                            `);
      $("#labelModal").html("Seleccionar Detalle");
      $("#modal").modal("show");
    }

    //Borrar ultimo caracter
    $(document).on("click", "#borrar", function(){
      if(idDetalleGuardado == ""){
        //alert("No se puede");
        noSeleccionado();
      } else{

        var numero;
        if (accion == "cantidad"){
          var cantidad_dom = $(".platillo_select #lblCantidad:eq("+idDetalle+")");
          numero = cantidad_dom.html().substring(0, cantidad_dom.html().length-1);
          if(numero == ""){
            cantidad_dom.html("0");
          } else{
            cantidad_dom.html(numero);
          }
        } else if (accion == "precio") {
          var precio_dom = $(".platillo_select #lblPrecioUnitario:eq("+idDetalle+")");
          numero = precio_dom.html().substring(0, precio_dom.html().length-1);
          if(numero == ""){
            precio_dom.html("0");
          } else{
            precio_dom.html(numero);
          }
        } else if (accion == "descuento") {
          var descuento_dom = $(".platillo_select #porcentajeDescuento:eq("+idDetalle+")");
          numero = descuento_dom.html().substring(0, descuento_dom.html().length-1);
          if(numero == ""){
            descuento_dom.html("0");
          } else{
            descuento_dom.html(numero);
          }
        }
        guardarCambios();
      }
    });

    //Remover color a los demás opciones de calculadora
    function removerClass(){
      $(".opcion").removeClass("opcion-seleccionada");
      $(".opcion").addClass("opcion-deseleccionada");
    }

    //Calcular total
    function calcularTotal(){
      var total = 0;
      for(var i = 0; i < $(".platillo_select").toArray().length; i++){
        total += parseFloat($(".platillo_select #lblPrecio:eq("+i+")").html());
      }
      //alert(total);
      $("#lblTotal").html(parseFloat(total).toFixed(2));
    }

    //Calcular Precio Unitario al editar
    function calcularPrecio(){
      var cantidad = parseFloat($(".platillo_select #lblCantidad:eq("+idDetalle+")").html()).toFixed(2);
      var preciounitario = parseFloat($(".platillo_select #lblPrecioUnitario:eq("+idDetalle+")").html()).toFixed(2);
      var descuento;
      if($(".platillo_select #porcentajeDescuento:eq("+idDetalle+")").html() == ""){
        descuento = 0;
      } else{
        descuento = parseFloat($(".platillo_select #porcentajeDescuento:eq("+idDetalle+")").html()).toFixed(2)/100;
      }
      var total = parseFloat(cantidad*preciounitario).toFixed(2)
      var diferencia = parseFloat(descuento*total).toFixed(2);
      $(".platillo_select #lblPrecio:eq("+idDetalle+")").html(parseFloat(total-diferencia).toFixed(2));

      if(cantidad == 0){
        clickEliminar++;
      }
      if(clickEliminar >= 2){
        $(".platillo_select:eq("+idDetalle+")").remove();
        $.ajax({
          url : "/procesos/delete_detalle_orden",
          data : {id: idDetalleGuardado},
          type: "GET",
          dataType: "json",
          success : function (data) {
            //console.log("Eliminado"+data.respuesta);
            idDetalleGuardado = "";
          }
        });
        for(var i = 0; i < $(".platillo_select").toArray().length; i++){
          $(".platillo_select:eq("+i+")").attr("id",i);
        }
        clickEliminar = 0;
      }
      calcularTotal();
    }

    //Hacer efecto al borrar caracter o agregar caracter
    function guardarCambios(){
      var id = $(".platillo_select .col-12:eq("+idDetalle+")").attr("id");
      //alert($(".platillo_select .col-12:eq("+idDetalle+")").attr("id"));
      var cantidad = $(".platillo_select #lblCantidad:eq("+idDetalle+")").html();
      var precio = $(".platillo_select #lblPrecioUnitario:eq("+idDetalle+")").html();
      var descuento = 0;
      if($(".platillo_select #porcentajeDescuento:eq("+idDetalle+")").html() != ""){
        descuento = $(".platillo_select #porcentajeDescuento:eq("+idDetalle+")").html();
      }

      calcularEntregados();

      var ordenados = $(".platillo_select #ordenados:eq("+idDetalle+")").html();
      var entregados = $(".platillo_select #entregados:eq("+idDetalle+")").html();

      actualizar(id, cantidad, precio, descuento, ordenados, entregados);
      calcularPrecio();
    }

    //Calcular la cantidad de ordenes que quedán pendientes de entregar de acuerdo a las ya entregadas
    function calcularEntregados(){
      var cantidad = parseInt($(".platillo_select #lblCantidad:eq("+idDetalle+")").html());
      var ordenados = parseInt($(".platillo_select #ordenados:eq("+idDetalle+")").html());
      var entregados = parseInt($(".platillo_select #entregados:eq("+idDetalle+")").html());
      var resultado = cantidad-entregados;
      if(resultado >= 0){
        $(".platillo_select #ordenados:eq("+idDetalle+")").html(resultado);
      } else{
        $(".platillo_select #ordenados:eq("+idDetalle+")").html(cantidad);
      }
      if(cantidad < entregados){
        $(".platillo_select #entregados:eq("+idDetalle+")").html(cantidad);
      }
    }

    $(document).on("click", "#btn-entregados-todos", function(){
      for(var i = 0; i < $(".platillo_select").toArray().length; i++){
        idDetalle = i;
        modificarEntregados();
      }
    });

    function modificarEntregados(){
      var ordenados = parseInt($(".platillo_select #ordenados:eq("+idDetalle+")").html());
      var entregados = parseInt($(".platillo_select #entregados:eq("+idDetalle+")").html());
      entregados += ordenados;
      $(".platillo_select #ordenados:eq("+idDetalle+")").html("0");
      $(".platillo_select #entregados:eq("+idDetalle+")").html(entregados);
      guardarCambios();
    }

    // Simular click para minimizar el nav
    $("#sidenavToggler > i").click();

    function llenarCategorias()
    {
      let ul = $("#tabCategorias"), htmlUL = ``;
      let div = $("#tabPlatillos"), htmlDIV = ``;
      $.ajax({
        url: "/restaurant/lista_categoria_platillos_con_platillos",
        type: 'get',
        dataType: 'json',
        success: (data) => {
          //console.log(data);
          for(let i = 0; i < data.length; i++)
          {
            if(i == 0){
              htmlUL += `<li class="nav-item">
                          <a class="nav-link active" id="${data[i].idCategoriaPlatillo}-tab" data-toggle="tab" href="#${data[i].idCategoriaPlatillo}" role="tab" aria-controls="${data[i].idCategoriaPlatillo}" aria-selected="true">${data[i].categoria}</a>
                        </li>`;
              htmlDIV += `<div class="tab-pane fade show active" id="${data[i].idCategoriaPlatillo}" role="tabpanel" aria-labelledby="${data[i].idCategoriaPlatillo}-tab">`;
              for(let j = 0; j < data[i].platillos.length; j++){
                htmlDIV +=`
                <div class="card bg-light mb-3 text-center platillo-card" value="${data[i].platillos[j].codigoPlatillo}" style="width: 9rem;">
                  <div class="card-body card-body-platillo">
                    <p class="card-text">
                        <small>${data[i].platillos[j].nombre}</small>
                    </p>
                    <div class="card-footer bg-transparent">
                        ${accounting.formatMoney(data[i].platillos[j].precioUnitario)}
                    </div>
                  </div>
                </div>
                `;
              }
              htmlDIV += `</div>`;
            }
            else{
              htmlUL +=  `
              <li class="nav-item">
                <a class="nav-link" id="${data[i].idCategoriaPlatillo}-tab" data-toggle="tab" href="#${data[i].idCategoriaPlatillo}" role="tab" aria-controls="${data[i].idCategoriaPlatillo}" aria-selected="false">${data[i].categoria}</a>
              </li>`;
              htmlDIV += `<div class="tab-pane fade" id="${data[i].idCategoriaPlatillo}" role="tabpanel" aria-labelledby="${data[i].idCategoriaPlatillo}-tab">`;
              for(let j = 0; j < data[i].platillos.length; j++){
                htmlDIV +=`
                <div class="card bg-light mb-3 text-center platillo-card" value="${data[i].platillos[j].codigoPlatillo}" style="width: 9rem;">
                  <div class="card-body card-body-platillo">
                    <p class="card-text">
                        <small>${data[i].platillos[j].nombre}</small>
                    </p>
                    <div class="card-footer bg-transparent">
                        ${accounting.formatMoney(data[i].platillos[j].precioUnitario)}
                    </div>
                  </div>
                </div>
                `;
              }
              htmlDIV += `</div>`;

            }

          }
          ul.html(htmlUL);
          div.html(htmlDIV);
        }
      });
    }
