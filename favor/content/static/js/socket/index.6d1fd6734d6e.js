$(document).ready(function(){

    var substringMatcher = function(strs) {
        return function findMatches(q, cb) {
            var matches, substrRegex;

            // an array that will be populated with substring matches
            matches = [];

            // regex used to determine if a string contains the substring `q`
            substrRegex = new RegExp(q, 'i');

            // iterate through the pool of strings and for any string that
            // contains the substring `q`, add it to the `matches` array
            $.each(strs, function(i, str) {
                if (substrRegex.test(str)) {
                    // the typeahead jQuery plugin expects suggestions to a
                    // JavaScript object, refer to typeahead docs for more info
                    matches.push({ value: str });
                }
            });

            cb(matches);
        };
    };

    var states = ['Combate', 'Esto Es Guerra', 'Bienvenida La Tarde', 'Yo Soy', 'La Voz',
    'Yo Soy Kids', 'Futbol En America', 'America Noticias', 'La Noche Es Mia', 'Enemigos Publicos', 'Hola a Todos',
    '90 Segundos', 'Perú Tiene Talento', 'Fabrica de sueños', 'La Maquina Del Millon', 'El Valor De La Verdad', 'Amor, Amor, Amor'
    ];

    $('#the-basics .typeahead').typeahead({
        hint: true,
        highlight: true,
        minLength: 1
    },
    {
        name: 'states',
        displayKey: 'value',
        source: substringMatcher(states)
    });

/*
$(document).on("click" , ".opt" , function(){
    console.log("Asdasdasda");
    alert('Hola');
});

*/
 var socket = io.connect('http://127.0.0.1:3000');


$('.cajaun').click(send_poll);

function send_poll(event)
{
    event.preventDefault();
    socket.emit('poll',{'vote':$(this).attr('data-poll'),
    'opcion':$(this).attr('data-choice')});
}

socket.on('pollOut',function(data){

console.log("pollOut",data);
    if(data!= "0")
    {
        console.log('Todo esta bien!!!');
    }
    else
    {
        console.log('Todo esta mal!!!');
    }

    var d = $.parseJSON(data)



    switch (d[0]){

        case "0" :
            console.log("todo esta mal");
            break;
            case "1" :
                console.log("este es D" , d[1][0] +" "+d[1][1] );

                $(".ri"+d[2]).text(d[1][0]);
                $(".rd"+d[2]).text(d[1][1]);

                //console.log(typeof d[1] );
                //var result = d[1].split('')
                //console.log("result",result)

                console.log("todo esta bien");


                $.

                break;
                case "2" :
                    console.log("Su voto ya ha sido Registrado");
                    break;
                }
});






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
 	var result = $('#resultadoss');
   console.log("DATA",data);
 	if(data !="0" && data !="")
 	{
 		var lista = $.parseJSON(data);
 		if(lista.length)
 		{
 			var pr="";

 			$.each(lista, function(clave,valor){

                if(valor.programa_p)
                {
                    pr+='<li><a href="/pages/'+valor.id+'-'+valor.programa_p+'">'+valor.nombres+' '+valor.apellido_paterno+' '+valor.apellido_materno+'</a></li>';
                }
                else
                {
                    pr+='<li><a href="/pages/'+valor.id+'">'+valor.nombre+'</a></li>';
                }

 			});

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
