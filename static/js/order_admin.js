$(function ($) {
    $('.url').find( "a" ).attr('target', 'blank');

    var cost = $('#id_cost').val()
    if (isNaN(cost) || cost == undefined || cost == "") {
        cost = 0;
    }
    var shippingCost = $('#id_shipping_cost').val()
    var deliveryCost = $('#id_delivery_cost').val()
    var serviceCost = $('#id_service_fee').val()
    var ubCost = $('#id_ub_shipping_cost').val()
    var hansh = parseFloat($('.field-hansh').find( "div:last-child" ).find( "div:last-child" ).text());
    
    $('#id_cost').after("<span id='yCost' style='margin-left: 10px;'>"+Intl.NumberFormat().format(cost*hansh)+"¥</span>")
    $('#id_shipping_cost').after("<span id='yShippingCost' style='margin-left: 10px;'>"+Intl.NumberFormat().format(shippingCost*hansh)+"¥</span>")
    $('#id_delivery_cost').after("<span id='yDeliveryCost' style='margin-left: 10px;'>"+Intl.NumberFormat().format(deliveryCost*hansh)+"¥</span>")
    $('#id_service_fee').after("<span id='yServiceCost' style='margin-left: 10px;'>"+Intl.NumberFormat().format(serviceCost*hansh)+"¥</span>")
    $('#id_ub_shipping_cost').after("<span id='yUbCost' style='margin-left: 10px;'>"+Intl.NumberFormat().format(ubCost*hansh)+"¥</span>")
    
    $('#id_cost').on('input', function() {
        var c = $('#id_cost').val()
        if (isNaN(c) || c == undefined || c == "") { c = 0;}
        var h = parseFloat($('.field-hansh').find( "div:last-child" ).find( "div:last-child" ).text());
        $('#yCost').text(Intl.NumberFormat().format(c*h)+"¥")
    })
    
    $('#id_shipping_cost').on('input', function() {
        var c = $('#id_shipping_cost').val()
        if (isNaN(c) || c == undefined || c == "") { c = 0;}
        var h = parseFloat($('.field-hansh').find( "div:last-child" ).find( "div:last-child" ).text());
        $('#yShippingCost').text(Intl.NumberFormat().format(c*h)+"¥")
    })
      
    $('#id_delivery_cost').on('input', function() {
        var c = $('#id_delivery_cost').val()
        if (isNaN(c) || c == undefined || c == "") { c = 0;}
        var h = parseFloat($('.field-hansh').find( "div:last-child" ).find( "div:last-child" ).text());
        $('#yDeliveryCost').text(Intl.NumberFormat().format(c*h)+"¥")
    })

    $('#id_service_fee').on('input', function() {
        var c = $('#id_service_fee').val()
        if (isNaN(c) || c == undefined || c == "") { c = 0;}
        var h = parseFloat($('.field-hansh').find( "div:last-child" ).find( "div:last-child" ).text());
        $('#yServiceCost').text(Intl.NumberFormat().format(c*h)+"¥")
    })

    $('#id_ub_shipping_cost').on('input', function() {
        var c = $('#id_ub_shipping_cost').val()
        if (isNaN(c) || c == undefined || c == "") { c = 0;}
        var h = parseFloat($('.field-hansh').find( "div:last-child" ).find( "div:last-child" ).text());
        $('#yUbCost').text(Intl.NumberFormat().format(c*h)+"¥")
    })
 })
