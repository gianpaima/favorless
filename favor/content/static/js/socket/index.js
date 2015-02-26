$(document).ready(function(){

 var socket = io.connect('http://127.0.0.1:3000');

//KeyUp, onblur y click
var buscar = $('#search');
var busca2 = $('#search2')

buscar.keyup(enviar_data);
buscar2.keyup(enviar_data);

function enviar_data()
{
	 socket.emit('search', { text: buscar.val()});
}

socket.emit('programa', { post: 'numero' });

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
 			console.log(resultados);
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


     var programas = ['Combate', 'Esto Es Guerra', 'Bienvenida La Tarde', 'Yo Soy', 'La Voz',
     'Yo Soy Kids', 'Futbol En America', 'America Noticias', 'La Noche Es Mia', 'Enemigos Publicos', 'Hola a Todos',
     '90 Segundos', 'Perú Tiene Talento', 'Fabrica de sueños', 'La Maquina Del Millon', 'El Valor De La Verdad', 'Amor, Amor, Amor'];

     // constructs the suggestion engine
     var programas = new Bloodhound({
         datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
         queryTokenizer: Bloodhound.tokenizers.whitespace,
         // `states` is an array of state names defined in "The Basics"
         local: $.map(programas, function(state) { return { value: state }; })
     });

     // kicks off the loading/processing of `local` and `prefetch`
     programas.initialize();

     $('#bloodhound .typeahead').typeahead({
         hint: true,
         highlight: true,
         minLength: 1
     },
     {
         name: 'programas',
         displayKey: 'value',
         // `ttAdapter` wraps the suggestion engine in an adapter that
         // is compatible with the typeahead jQuery plugin
         source: programas.ttAdapter()
     });
});
