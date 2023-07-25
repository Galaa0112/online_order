$(function ($) {


    // LINK IIG OORCHILSON HESEG START
    var pLink = $('.field-link').find( "p" );
    var urlInput =  $('.field-link').find( "input" )
    var link =urlInput.val()
    pLink.text('')
    pLink.append(urlInput)
    pLink.append("<a style='margin-left:5px;' href='"+link+"' target='blank'><img src='/media/picture/link-icon.png' width='20' /></a>")
    // LINK IIG OORCHILSON HESEG END
    
    // STATUS ZAHIALSAN BOLOH UYED READ ONLY BOLGOH HESEG START
    if('D'== $('#id_status').val() || 'O'== $('#id_status').val()){
        $('input').attr('readonly', 'readonly').css('border','none');
    }
    // STATUS ZAHIALSAN BOLOH UYED READ ONLY BOLGOH HESEG END

    total()


    var cost = $('#id_cost').val()
    if (isNaN(cost) || cost == undefined || cost == "") {
        cost = 0;
    }
    
    $('#id_cost').on('input', function() {
        total()
    })
    
    $('#id_shipping_cost').on('input', function() {
        total()
    })
      
    $('#id_delivery_cost').on('input', function() {
        total()
    })

    $('#id_service_fee').on('input', function() {
        total()
    })

    $('#id_ub_shipping_cost').on('input', function() {
        total()
    })
    function total() {
        var cost = $('#id_cost').val()
        var shippingCost = $('#id_shipping_cost').val()
        var deliveryCost = $('#id_delivery_cost').val()
        var serviceCost = $('#id_service_fee').val()
        var ubCost = $('#id_ub_shipping_cost').val()
        var hansh = parseFloat($('.field-hansh').find( "div:last-child" ).find( "div:last-child" ).text());
        if (isNaN(cost) || cost == undefined || cost == "") { cost= 0;}
        if (isNaN(shippingCost) || shippingCost == undefined || shippingCost == "") { shippingCost= 0;}
        if (isNaN(deliveryCost) || deliveryCost == undefined || deliveryCost == "") { deliveryCost= 0;}
        if (isNaN(serviceCost) || serviceCost == undefined || serviceCost == "") { serviceCost= 0;}
        var total = parseFloat(cost.toString()) + parseFloat(shippingCost.toString())+parseFloat(deliveryCost.toString())+parseFloat(serviceCost.toString())+parseFloat(ubCost.toString())
        var tugrik  = total * hansh
        $('.field-status').before("<div class='form-row field-total'><div><label id='id_total_cost' for='id_total_cost'>Нийт:</label></div></div>");
        $('#id_total_cost').after("<span>"+Intl.NumberFormat().format(tugrik)+"₮</span>");
        $('#id_total_cost').after("<p>"+Intl.NumberFormat().format(total)+"¥</p>");

      }
      
 })
 