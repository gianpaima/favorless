var io = require('socket.io')(3000);
var request = require('request');
/*request('http://127.0.0.1:8000/test', function (error, response, body) {
 if (!error && response.statusCode == 200) {
   console.log("hola mundo: "+body);
  }
 });

*/
io.sockets.on('connection', function (socket)
{
    console.log("Cookisssse" +socket.request.headers.cookie)

  socket.on('post', function(data){
request.post();


  });



  socket.on('search', function (data) {

  //request a Django
/*
  request({ url: 'http://127.0.0.1:8000/test?hola=kalena', method: 'GET', json: {foo: "bar", woo: "car",hola: "mundo"}}, function (error, response, body) {
 if (!error && response.statusCode == 200) {
   console.log("hola mundo: "+body);
   console.log("response: "+response);
  }
 }).form({hola:'kalena'});
*/
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


  console.log('Usuario conectado');
  socket.on('disconnect', function () {
    console.log('Usuario desconectado');
  });
});
