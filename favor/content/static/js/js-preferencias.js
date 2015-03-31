$("a").click(function(){
            var atributos = $(this).prop("class");
            console.log(atributos);
          });
      //-------------------------------


      $('select').on('change', buscar);

            function buscar() {

               var id  = $(this).val();
               console.log(id);
               todos_programas = $(".programa")
               if( isNaN(id) || id === "0" || id === ""){

                 for(i = 0 ;i<todos_programas.length ;i++){
                    programa = todos_programas[i]
                    $(programa).show("slow");

                    }
                  }

                else{
                
                  for(i = 0 ;i<todos_programas.length ;i++){

                    programa = todos_programas[i]
                    valor =   $(programa).hasClass("categ"+id)

                        if(valor === false){
                            $(programa).hide("slow");
                          }

                        else{
                             $(programa).show("slow");
                         }
            
                    }
                  }
              }

        $("body").delegate(".js-megusta","click",function(event){
          event.preventDefault();

          var bot= $(this);
          var id = $(this).prop("id");
           
          $.ajax({

              data : {'id' : id },
              url :'/addpreference/',
              type : 'post',
              success: function(data){
                var resultados = $.parseJSON(data);
                console.log("ADD: ",data);
                switch  (resultados[0]) {
                    case "0":
                        $('#alerta').html("error")
                        break;
                    case "1":
                        bot.removeClass( "js-megusta btn btn-primary" ).addClass("js-no-megusta btn btn-danger");
                        var no_gusta = "No me Gusta";
                        bot.text(no_gusta);
                        $('#alerta').html("")
                        break;
                    case "2":
                        $('#alerta').html("no existes")
                        break;
                    case "3":
                        $('#alerta').html("error de SERVER")
                        break;
                    default:
                        $('#alerta').html("error")
                        
                    }

                 cantidad(resultados[1]);
              },

           });

        });




        $("body").delegate(".js-no-megusta","click",function(event){
          event.preventDefault();
          
          var bot= $(this);
          var id = $(this).prop("id");

          $.ajax({
              data : {'id':id},
              url : '/removepreference/',
              type : 'post',
              success : function(data){
                console.log("RV",data);
                var resultados = $.parseJSON(data);
                 switch  (resultados[0]) {
                    case "0":
                        $('#alerta').html("error")
                        break;
                    case "1":
                        bot.removeClass( "js-no-megusta btn btn-danger" ).addClass("js-megusta btn btn-primary");
                        var gusta = " me Gusta";
                        bot.text(gusta);
                        $('#alerta').html("")
                        break;
                    case "2":
                        $('#alerta').html("no existes")
                        break;
                    case "3":
                        $('#alerta').html("error de SERVER")
                        break;
                    default:
                        $('#alerta').html("error")
                        
                }

                cantidad(resultados[1]);

              },

            });

        });

function cantidad(resultados)
{
  console.log("resultados",resultados);
   if(resultados || resultados == 0)
      {
        if(resultados>=5)
          {
            $('#informacion').html('Usted ha seleccionado el minimo de programas requeridos');
            $('#siguiente').removeAttr('disabled');
          }
        else
          {
            $('#informacion').html('Usted debe seleccionar :'+ (5-resultados) +' más');
            $('#siguiente').attr('disabled','disabled');
          }
          console.log("resultados:"+resultados)
      }
    else
    {
      console.log("Hubo un error");
    }
}


         

          // This function gets cookie with a given name
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }


            var csrftoken = getCookie('csrftoken');
            /*
            The functions below will create a header with csrftoken
            */

            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            function sameOrigin(url) {
                // test that a given url is a same-origin URL
                // url could be relative or scheme relative or absolute
                var host = document.location.host; // host + port
                var protocol = document.location.protocol;
                var sr_origin = '//' + host;
                var origin = protocol + sr_origin;
                // Allow absolute or scheme relative URLs to same origin
                return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                    (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                    // or any other URL that isn't scheme relative or absolute i.e relative.
                    !(/^(\/\/|http:|https:).*/.test(url));
            }

            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                        // Send the token to same-origin, relative URLs only.
                        // Send the token only if the method warrants CSRF protection
                        // Using the CSRFToken value acquired earlier
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });
