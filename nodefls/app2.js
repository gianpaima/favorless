
var request = require("request");
/*var http = require('http');
var server = http.createServer( function(request, response) {
    response.writeHead(200, {'Content-type': 'text/plain'});
    response.end('Hello World!');
    server.listen(8888);
    console.log('Server running on port 8000');
});*/
var io = require("socket.io")(3000);
console.log("Running........");

/*io.sockets.on('connection', function (socket) {
  socket.emit('news', { hello: 'world' });
  
});*/

var clicks = 0;

/*io.use(function(socket, next) {
  var handshakeData = socket.request;
  console.log("llega a esta waa")
  // make sure the handshake data looks good as before
  // if error do this:
    // next(new Error('not authorized');
  // else just call next
  //next();
});*/

//io.of('/namespace').use(function(socket, next) {
  //var handshakeData = socket.request;
  //next();
//});
/*
io.configure(function () {
    io.set('authorization', function (data, accept) {
        if (data.headers.cookie) {
            data.cookie = cookie_reader.parse(data.headers.cookie);
            return accept(null, true);
        }
        return accept('error', false);
    });
    io.set('log level', 1);
});
*/




io.sockets.on('connection', function(socket){
  //Emitimos nuestro evento connected
 console.log("before")
  socket.emit('connected');
 console.log("after");
  //Permanecemos a la escucha del evento click
  socket.on('click', function(data){

values = querystring.stringify({
            word: data,
            sessionid: socket.handshake.cookie['sessionid']
        });
 var options = {
            host: 'localhost',
            port: 8000,
            path: '/pruebarealtime/',
            method: 'POST',
            headers: {
             'Cookie': 'csrftoken=' + socket.handshake.cookie['csrftoken'],
              'Content-Type': 'application/x-www-form-urlencoded',
              'Content-Length': values.length
            }
        };

   
    });

    //Sumamos el click
    clicks++;
    console.log(clicks);

/*    request.post({
      method : 'POST',
      preambleCRLF: true ,
      postambleCRLF:true ,
      uri : 'http://127.0.0.1:8000/pruebarealtime',


    })*/

var postData={
    a:1,
    b:2
};
console.log(data.token);

    // request.post('http://127.0.0.1:8000/pruebarealtime/', {form:{key:'value'}})
options={
  body:require('querystring').stringify(postData),
  headers: {"X-CSRFToken": data.token}
};    
request=request.defaults({
  headers: {'content-type': 'application/x-www-form-urlencoded',
"X-CSRFToken":data.token
},
  jar: true
  
});
request.cookie("X-CSRFToken="+data.token);
/*request.post('http://localhost:8000/pruebarealtime/',options,

  function(error, response, body){
  console.log(body);
  console.log("xxxxxxxxxxxxxxxDDD");
  console.log('Authorization: '+ request)
});*/




 
    //Emitimos el evento que dirá al cliente que hemos recibido el click
    //y el número de clicks que llevamos
    socket.emit('otherClick', clicks);
  });



/*io.sockets.on('connection', function(socket){
  //Emitimos nuestro evento connected
  socket.emit('connected');


//Permanecemos a la escucha del evento click
 io.sockets.on('click', function(){
    //Sumamos el click
    console.log("llegue a click");
    clicks++;
 
    //Emitimos el evento que dirá al cliente que hemos recibido el click
    //y el número de clicks que llevamos
    io.socket.emit('otherClick', clicks);
  });

/*request('http://127.0.0.1:8000/', function (error, response, body) {
 if (!error && response.statusCode == 200) {
  
  }
 });*/
