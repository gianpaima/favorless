 var socket = io('http://127.0.0.1:3000');
        socket.on('connected', function () {
              console.log('Conectado!');
              
            });


       //$("body").delegate(".js-megusta","click",
        $('.panel-default').on("click", ".js-megusta",
        function()
         {  
            var bot  =   $(this);
            socket.emit('addPre',{ id : bot.prop("id") });
         });



       //$("body").delegate(".js-no-megusta","click",
         $('.panel-default').on("click", ".js-no-megusta",
        function()
         {  
             var bot  = $(this);
            socket.emit('removePre',{ id : bot.prop("id") });
        });



       socket.on('update',function(data){

            if(data[0]=="add")
            {
                console.log("ADD...")
                 switch  (data[2]) {
                    case "0":
                        $('#alerta').html("error")
                        break;
                    case "1":
                        $('#'+data[1]).removeClass( "js-megusta btn btn-primary" ).addClass("js-no-megusta btn btn-danger");
                        var no_gusta = "No me Gusta";
                        $('#'+data[1]).text(no_gusta);
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
            }
            else
            {
                if(data[0]=="rv")
                {
                    console.log("rvvv...");
                     switch  (data[2]) {
                    case "0":
                        $('#alerta').html("error")
                        break;
                    case "1":
                        $('#'+data[1]).removeClass( "js-no-megusta btn btn-danger" ).addClass("js-megusta btn btn-primary");
                        var gusta = " me Gusta";
                        $('#'+data[1]).text(gusta);
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
                }
            }

                });