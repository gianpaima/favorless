var request = require("request");


request('http://127.0.0.1:8000/pruebarealtime/', function (error, response, body) {
  if (!error && response.statusCode == 200) {
    console.log(body) // Show the HTML for the Google homepage. 
  }
})