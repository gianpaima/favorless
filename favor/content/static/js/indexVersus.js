$(document).ready(function(){

 var socket = io.connect('http://127.0.0.1:3000');

//KeyUp, onblur y click



$(".search").focus(function(){
    buscar = $(this);
    buscar.keyup(enviar_data);
    // var voyair =  dondeEstoy();
    // console.log("tenog que ir :" + voyair);
    console.log(buscar);    
})

$(".search2").focus(function(){
    buscar = $(this);
    buscar.keyup(enviar_data);
    //var voyair =  dondeEstoy();
    console.log(buscar);
})


// var buscar = $('#search');

// var buscar2 = $('#search2');

// buscar.keyup(enviar_data);


// buscar2.keyup(enviar_data);




function enviar_data()
{
	 socket.emit('search', { text: buscar.val()});
}

//socket.emit('programa', { post: 'numero' });

 socket.on('dataSend',function(data)
 {


 	var result =  dondeEstoy();
    //console.log("me Voyyyyyyy a : " + result);


 	if(data !="0" && data !="")
 	{
 		var lista = $.parseJSON(data);
 		if(lista.length)
 		{
 			var pr="";

 			$.each(lista, function(clave,valor){

<<<<<<< HEAD
                if(valor.programa_p)
                {
                    pr+='<li><a class="target" id="'+valor.id+'-'+valor.programa_p+'" href="#">'+valor.nombres+' '+valor.apellido_paterno+' '+valor.apellido_materno+'</a></li>';
=======
                if(valor.programa)
                {
                    pr+='<li><a class="target" id="'+valor.id+'-'+valor.programa+'" href="#">'+valor.nombres+' '+valor.apellido_paterno+' '+valor.apellido_materno+'</a></li>';
>>>>>>> 47c5084d275da9e1a9c31541981746dce5e7e91e
                }
                else
                {
 				   pr+='<li><a class = "target" id="'+valor.id+'" href="#">'+valor.nombre+'</a></li>';
                }
 			});

 			//console.log("Programas: "+pr);
 			//console.log(resultados);
 			result.html(pr);
 		}
 		else
 		{
 			result.html("No se ha encontrado el elemento buscado");
 		}
 	}
 	else if(data == ""){
<<<<<<< HEAD
 		result.html( "No se ha encontrado ninguna coincidencia");
=======
 		result.html( "buscar elemento");
>>>>>>> 47c5084d275da9e1a9c31541981746dce5e7e91e

 	}
 	else{
 		result.html("Ha ocurrido un error, espere un momento");
 	}
 });
 // socket.on('enviar mensaje', function (data) {
   //     $('form').after('<p>' + data.text + '</p>');
     // });


function dondeEstoy(){
    var tengoqueir;
        if($('.search').is(':focus')){
            tengoqueir= $("#resultados");
        }

        if  ($('.search2').is(':focus')){
            tengoqueir= $("#resultadosPart2");
        }
               
        return tengoqueir;
    }


$("form").submit(
    function(){
        var datos_form = [];

    });


   $("body").delegate(".target","click",
 
        function(){
            var  elem  = $(this); 
            elemId=elem.prop("id");
            console.log(elemId);
            elemText = elem.text();
            console.log(elemText);

             var padre  =  elem.parent();
 
             var Abuelo =  padre.parent().attr('id');

             if ("resultados" === Abuelo){
                   $(".search").val(elemText).attr('id',elemId);
             }

             if("resultadosPart2" === Abuelo) {
                 $(".search2").val(elemText).attr('id',elemId);
             }

        }
    )







     // var programas = ['Combate', 'Esto Es Guerra', 'Bienvenida La Tarde', 'Yo Soy', 'La Voz',
     // 'Yo Soy Kids', 'Futbol En America', 'America Noticias', 'La Noche Es Mia', 'Enemigos Publicos', 'Hola a Todos',
     // '90 Segundos', 'Perú Tiene Talento', 'Fabrica de sueños', 'La Maquina Del Millon', 'El Valor De La Verdad', 'Amor, Amor, Amor'];

     // // constructs the suggestion engine
     // var programas = new Bloodhound({
     //     datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
     //     queryTokenizer: Bloodhound.tokenizers.whitespace,
     //     // `states` is an array of state names defined in "The Basics"
     //     local: $.map(programas, function(state) { return { value: state }; })
     // });

     // // kicks off the loading/processing of `local` and `prefetch`
     // programas.initialize();

     // $('#bloodhound .typeahead').typeahead({
     //     hint: true,
     //     highlight: true,
     //     minLength: 1
     // },
     // {
     //     name: 'programas',
     //     displayKey: 'value',
     //     // `ttAdapter` wraps the suggestion engine in an adapter that
     //     // is compatible with the typeahead jQuery plugin
     //     source: programas.ttAdapter()
     // });
});