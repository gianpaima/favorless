var io = require('socket.io').listen(3000, {
  'authorization' : function(data, accept) {

    // authorization logic

     if (data.headers.cookie) {
            data.cookie = cookie_reader.parse(data.headers.cookie);
            console.log("autoriza");
            return accept(null, true);
        }
        console.log("SIN autoriza");
        return accept('error', false);

  }});

io.use(function(socket, next){
 console.log("Socket ssssssssssssssss  xD: ",socket.request.headers.cookie);
   if (socket.request.headers.cookie)
    return next();
   next(new Error('Authentication error'));
 });

var request = require('request');
var querystring = require('querystring');

io.use(function(socket, next) {
  var handshakeData = socket.request;
  // make sure the handshake data looks good as before
  // if error do this:
    // next(new Error('not authorized');
  // else just call next
  //console.log("Usuario Usess:"+handshakeData.headers.cookie);

  next();
});

io.sockets.on('connection', function (socket) 
{
var handshakeData = socket.request;
//console.log("hand: "+handshakeData.headers.cookie);
//console.log("Tipo: "+typeof handshakeData.headers.cookie);


//arreglar esto...el 1) es io="cadena" 
//2)sessionid="asdasdsa" 
//3)csrftoken="sdsdsd"

//console.log("Usuario UsessxDdxD:"+handshakeData.headers.cookie);
socket.on('prueba',function(data){
console.log("xxxxxxxx:",handshakeData.headers.cookie);
var arreglo = handshakeData.headers.cookie.split(';') || [];


if(arreglo)
{
  var csrfcookie, sessionid;
  for (var i = 0; i < arreglo.length; i++) {
    arreglo[i]=arreglo[i].trim();
    console.log("arreglo",arreglo[i]);
    if(arreglo[i].toLowerCase().indexOf("csrftoken=")===0)
    {
     
      csrfcookie=arreglo[i].substring(arreglo[i].indexOf("=")+1);
    }
    else
    {
      if(arreglo[i].toLowerCase().indexOf("sessionid=")===0)
      {
        sessionid =arreglo[i].substring(arreglo[i].indexOf("=")+1);

      }
     
    }
  }

  //Consultar si las variables, estan vacias o undefined
  if(!csrfcookie)
  {
    //Es vacia o undefined...
    console.log("Devuelve Soctet!!!")
  }

}
else
{
  console.log("Devuelve Soctet!!!")
}

 var values = querystring.stringify({
            id: data.id,
            sessionid: sessionid
        });

var cookieString='csrftoken='+csrfcookie+' , sessionid='+sessionid;

var cookie = request.cookie(cookieString);
var options = {
        url:'http://127.0.0.1:8000/addpreference/',
        headers: {
        'X-CSRFToken': csrfcookie,
      //'csrftoken=' + arreglo[2].split('csrftoken=')[1]
        'Cookie':  'csrftoken=' +csrfcookie ,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': values.length
            },
        method: 'POST',
        body:values
           
          
        };

function callback(error, response, body) {
    if (!error && response.statusCode == 200) {
       // var info = JSON.parse(body);
       // console.log(info.stargazers_count + " Stars");
       // console.log(info.forks_count + " Forks");
       
       console.log(body);
       socket.emit("update",body)


    }
    console.log("Error: "+error);
   // console.log("respose : "+response);
    console.log('body: '+body);
}


request(options,callback);

});

  socket.on('search', function (data) {


console.log("Dato: "+data.text);
request.get('http://127.0.0.1:8000/search?search='+data.text,
 {headers:
  {
        'User-Agent': 'request'
    }
  ,
  todo: {
    'bearer': 'bearerToken'
  }
}, function (error, response, body) {
   
   enviar_emit(body);
}).on('response', function(response) {
  console.log("respuesta");
  //console.log(response);
}).on('error',function(err)
{
  enviar_emit('0')
});


    //console.log("Datas:"+data.text);
    //socket.broadcast.emit('enviar mensaje', data);
    //socket.emit('enviar mensaje', data);
  });


  function enviar_emit(data)
  {
    socket.emit('dataSend',data)    
  }
  
//--------------------------------------------------------------------------------------------


socket.on('prueba2',function(data){
console.log("xxxxxxxx:",handshakeData.headers.cookie);
var arreglo = handshakeData.headers.cookie.split(';') || [];


    if(arreglo)
    {
      var csrfcookie, sessionid;
      for (var i = 0; i < arreglo.length; i++) {
        arreglo[i]=arreglo[i].trim();
        console.log("arreglo",arreglo[i]);
        if(arreglo[i].toLowerCase().indexOf("csrftoken=")===0)
        {
          csrfcookie=arreglo[i].substring(arreglo[i].indexOf("=")+1);
        }
        else
        {
          if(arreglo[i].toLowerCase().indexOf("sessionid=")===0)
          {
            sessionid =arreglo[i].substring(arreglo[i].indexOf("=")+1);
          }
        }
      }

      //Consultar si las variables, estan vacias o undefined
      if(!csrfcookie)
      {
        //Es vacia o undefined...
        console.log("Devuelve Soctet!!!")
      }

    }
else
{
  console.log("Devuelve Soctet!!!")
}

 var values = querystring.stringify({
            id: data.id,
            sessionid: sessionid
        });

var cookieString='csrftoken='+csrfcookie+' , sessionid='+sessionid;

var cookie = request.cookie(cookieString);
var options = {
        url:'http://127.0.0.1:8000/removepreference/',
        headers: {
        'X-CSRFToken': csrfcookie,
      //'csrftoken=' + arreglo[2].split('csrftoken=')[1]
        'Cookie':  'csrftoken=' +csrfcookie ,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': values.length
            },
        method: 'POST',
        body:values
           
          
        };

function callback(error, response, body) {
    if (!error && response.statusCode == 200) {
       // var info = JSON.parse(body);
       // console.log(info.stargazers_count + " Stars");
       // console.log(info.forks_count + " Forks");
       
       console.log(body);
       socket.emit("update",body)


    }
    console.log("Error: "+error);
   // console.log("respose : "+response);
    console.log('body: '+body);
}


request(options,callback);

});






  console.log('Usuario conectado');
  socket.on('disconnect', function () {
    console.log('Usuario desconectado');
  });
});


