$(document).ready(function(){

	//Mover arriba a la izquierdda
	$("#top_left").on("click", function(){
		if($("#top_left").attr('class') || "clicked"){
			$.ajax({
				url: '/topLeft',
				type: 'GET'
			})					//<--- !!!!!NO USAR PUNTO Y COMA (MAGIA POKÉMON)
			.done(function(){
				rmClass();
				$("#top_left").addClass("clicked");
			});
		}
	});
	
	//Mover arriba a la derecha
	$("#top_right").on("click", function(){
		if($("#top_right").attr('class') || "clicked"){
			$.ajax({
				url:'/topRight',
				type:'GET'
			})
			.done(function(){
				rmClass();
				$("#top_right").addClass("clicked");
			});
		}
	});
	
	//Mover abajo a la izquierda
	$("#bottom_left").on("click", function(){
		if($("#bottom_left").attr('class') || "clicked"){
			$.ajax({
				url:'/bottomLeft',
				type:'GET'
			})
			.done(function(){
				rmClass();
				$("#bottom_left").addClass("clicked");
			});
		}
	});
	
	
	//Mover abajo a la derecha
	$("#bottom_right").on("click", function(){
		if($("#bottom_right").attr('class') || "clicked"){
			$.ajax({
				url:'/bottomRight',
				type:'GET'
			})
			.done(function(){
				rmClass();
				$("#bottom_right").addClass("clicked");
			});
		}
	});
	
	
	//Mover la punta a un lado para dejar espacio para calibrar la cama
	$("#calibrate").on("click", function(){
		var value = {corner:1}
		
		
		$.ajax({
			url:'/calibrate',
			type:'GET'
		})
		.done(function(){

		});
	});
	
	
	//Mover la punta a home
	$("#home").on("click", function(){
		$.ajax({
			url:'/home',
			type:'get'
		})
	});
	
	
	//Subir y bajar la punta
	$("#up_down").on("click", function(){
		$("#up_down").toggleClass("rotate");	//Agrega/remueve la clase para girar la flecha con cada click
		
		$.ajax({
			url:'/up_down',
			type:'get'
		})
	});
	
	
	//Remueve el nombre de la clase de todos los botones
	function rmClass(){
		$("#top_left").removeClass("clicked");
		$("#top_right").removeClass("clicked");
		$("#bottom_left").removeClass("clicked");
		$("#bottom_right").removeClass("clicked");
	}
});