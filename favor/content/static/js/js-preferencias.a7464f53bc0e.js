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



       /*  $(".js-megusta").click(function(){
            var bot= $(this);
            var id = $(this).prop("id");
            console.log("le diste me gusta  a " +  id);
           
            $.ajax({

              data : {'id' : id },
              url :'/addpreference/',
              type : 'post',
              success: function(data){

              bot.removeClass( "js-megusta btn btn-primary" ).addClass("js-no-megusta btn btn-danger");
              var no_gusta = "No me Gusta";
              bot.text(no_gusta);
              console.log("el post manda esto :" + data);

              },

            });

          });*/

          //-----------------------------------

        /*  $(".js-megusta").bind("click",function(){

            var bot= $(this);
            var id = $(this).prop("id");
            console.log("le diste me gusta  a " +  id);
           
            $.ajax({

              data : {'id' : id },
              url :'/addpreference/',
              type : 'post',
              success: function(data){

              bot.removeClass( "js-megusta btn btn-primary" ).addClass("js-no-megusta btn btn-danger");
              var no_gusta = "No me Gusta";
              bot.text(no_gusta);
              console.log("el post manda esto :" + data);

              },

            });

          });

          */
        

        //....................................................................................

         /* $(".js-no-megusta").click(function(){

           var bot_no_gusta = $(this);
           var id = $(this).prop("id");
           console.log("ya no me gusta " +  id);

           $.ajax({
                 data : {'id':id},
                 url : '/removepreference/',
                 type : 'post',
                 success : function(data){

                  bot_no_gusta.removeClass("js-no-megusta btn btn-danger").addClass("js-megusta btn btn-primary");
                  var gusta = "Me Gusta";
                  bot_no_gusta.text(gusta);

    
                },

              });

          
          }); */

//.................................................................................

        
      /*   $(".js-no-megusta").bind("click",function(){
           var bot_no_gusta = $(this);
           var id = $(this).prop("id");
           console.log("ya no me gusta " +  id);

           $.ajax({
                 data : {'id':id},
                 url : '/removepreference/',
                 type : 'post',
                 success : function(data){

                  bot_no_gusta.removeClass("js-no-megusta btn btn-danger").addClass("js-megusta btn btn-primary");
                  var gusta = "Me Gusta";
                  bot_no_gusta.text(gusta);
              },

            });

          });  */

//------------------------------------------------------------------------------------


    /*
          $( ".js-no-megusta" ).on( "click", function() {
            console.log( $( this ).text() );

          var bot_no_gusta = $(this);
          var id = $(this).prop("id");
          console.log("ya no me gusta " +  id);

          $.ajax({
              data : {'id':id},
              url : '/removepreference/',
              type : 'post',
              success : function(data){
                bot_no_gusta.removeClass("js-no-megusta btn btn-danger").addClass("js-megusta btn btn-primary");
                var gusta = "Me Gusta";
                bot_no_gusta.text(gusta);
              },

            });

          });


          $( ".js-megusta" ).on( "click", function() {
            var bot= $(this);
            var id = $(this).prop("id");
            console.log("le diste me gusta  a " +  id);
           
            $.ajax({

              data : {'id' : id },
              url :'/addpreference/',
              type : 'post',
              success: function(data){

                bot.removeClass( "js-megusta btn btn-primary" ).addClass("js-no-megusta btn btn-danger");
                var no_gusta = "No me Gusta";
                bot.text(no_gusta);
                console.log("el post manda esto :" + data);

              },

            });
          });


      */


        $("body").delegate(".js-megusta","click",function(){

          console.log( $( this ).text() );


          var bot= $(this);
          var id = $(this).prop("id");
          console.log("le diste me gusta  a " +  id);
           
          $.ajax({

              data : {'id' : id },
              url :'/addpreference/',
              type : 'post',
              success: function(data){

                bot.removeClass( "js-megusta btn btn-primary" ).addClass("js-no-megusta btn btn-danger");
                var no_gusta = "No me Gusta";
                bot.text(no_gusta);
                console.log("el post manda esto :" + data);

              },

           });

        });




        $("body").delegate(".js-no-megusta","click",function(){

          console.log( $( this ).text() );

          var bot_no_gusta = $(this);
          var id = $(this).prop("id");
          console.log("ya no me gusta " +  id);

          $.ajax({
              data : {'id':id},
              url : '/removepreference/',
              type : 'post',
              success : function(data){
                bot_no_gusta.removeClass("js-no-megusta btn btn-danger").addClass("js-megusta btn btn-primary");

                var gusta = "Me Gusta";
                
                bot_no_gusta.text(gusta);
              },

            });

        });



         

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
