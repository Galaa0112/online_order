(function($) {
	"use strict";

    // var slideArray = []

    // setTimeout(function() {  
    //     // var sliders = document.getElementsByClassName('owl-item');
       

    //     // for(let i=0;i<  sliders.length; i++){
    //     //     var obj = sliders[i];
    //     //     console.log(i," ", obj.classList.contains('cloned') ==false, "--- ",obj)
    //     //     if(obj.classList.contains('cloned') ==false){
    //     //         slideArray.push(obj);
    //     //     }
    //     // }
    //     // for(var s in slideArray){
    //     //     console.log(" -*- ",s);
    //     // }

    //     $( ".owl-item" ).each(function( i,obj ) {
    //         var isActive =false;
    //         if(obj.classList.contains('cloned') == false){
    //             if(obj.classList.contains('active') == true ){
    //                 isActive = true;
    //                 console.log( i + ": asdsa" ,obj );
    //                 obj.classList.remove('active');
    //                 console.log( i + ": " ,obj, isActive );
    //             }
    //             else if(isActive==true){
    //                 console.log( i + ":TRUE: " ,obj );
    //                 // obj.classList.add('active');
    //                 // console.log( i + ": " ,obj );
    //                 // isActive=false;
    //             }
    //         }
    //       });
        
    // }, 3000);
   
    setTimeout(function() {
            $( ".slider-img" ).first().addClass( "active" );
        }, 1000);
	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	var owl = $('.featured-carousel');

  $('.featured-carousel').owlCarousel({
  		animateOut: 'fadeOut',
      center: false,
      items: 1,
      loop: true,
      stagePadding: 0,
      margin: 0,
      smartSpeed: 1500,
      autoplay: false,
      dots: false,
      nav: false,
      navText: ['<span class="icon-keyboard_arrow_left">', '<span class="icon-keyboard_arrow_right">']
  });

  $('.thumbnail li').each(function(slide_index){
      $(this).click(function(e) {
          owl.trigger('to.owl.carousel',[slide_index,1500]);
          e.preventDefault();
      })
  })

  owl.on('changed.owl.carousel', function(event) {
      $('.thumbnail li').removeClass('active');
      $('.thumbnail li').eq(event.item.index - 2).addClass('active');
  })

})(jQuery);