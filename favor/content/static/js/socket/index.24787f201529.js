$(document).ready(function(){
 var socket = io.connect('http://127.0.0.1:3000');

//KeyUp, onblur y click
var buscar = $('#search');

buscar.keyup(enviar_data);


function enviar_data()
{
	 socket.emit('search', { text: buscar.val()});
}

socket.emit('programa',{ post: 'numero' });

 socket.on('dataSend',function(data)
 {
 	var result = $('#resultados');
 	if(data !="0" && data !="")
 	{
 		var lista = $.parseJSON(data);
 		if(lista.length)
 		{
 			var pr="";

 			$.each(lista, function(clave,valor){
 				pr+='<li><a href="#">'+valor.nombre+'</a></li>';
 			});

 			console.log("Programas: "+pr);
 			console.log(result);
 			result.html(pr);
 		}
 		else
 		{
 			result.html("No se ha encontrado el elemento buscado");
 		}	
 	}
 	else if(data == ""){
 		result.html( "buscar elemento");

 	}
 	else{
 		result.html("Ha ocurrido un error, espere un momento");
 	}
 });
 // socket.on('enviar mensaje', function (data) {
   //     $('form').after('<p>' + data.text + '</p>');
     // });

});

