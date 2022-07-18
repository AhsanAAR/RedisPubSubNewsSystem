var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io')(server);

app.use(express.static(__dirname + '/bower_components'));
app.get('/', function(req, res,next) {
    res.sendFile(__dirname + '/index_test.html');
});

io.on('connection', function(client) {
    console.log('Client connected...');
    
    client.on('join', function(data) {
    	console.log(data);
        client.emit('messages', 'Hello from server!');
    });

});

server.listen(4200);