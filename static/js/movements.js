$(document).ready(function(){
	
	var home = 0;	//Variable que identifica si la punta está en home (0 = no está en home)
	

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
				rotate();
				home = 0;
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
				rotate();
				home = 0;
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
				rotate();
				home = 0;
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
				rotate();
				home = 0;
			});
		}
	});
	
	
	//Mover la punta a un lado para dejar espacio para calibrar la cama
	$("#calibrate").on("click", function(){
		
		if(home == 1){	//Si la punta está en home cuando se presiona 'Mover para calibrar':
			$("#bottom_left").addClass("clicked");	//Añade opacidad a la esquina inferior izquierda
			home = 0;	//Declara que la punta no está en home
		}
		
		$.ajax({
			url:'/calibrate',
			type:'GET'
		})
		.done(function(){
			rotate();
		});
	});
	
	
	//Mover la punta a home
	$("#home").on("click", function(){
		home = 1;	//Declara que la punta Sí está en home
		
		$.ajax({
			url:'/home',
			type:'get'
		})
		.done(function(){
			rotate();
			rmClass();
		});
	});
	
	
	//Gira la flecha hacia arriba (posición original)
	function rotate(){
		$("#up_down").removeClass("rotate");
	}
	
	
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