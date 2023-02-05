var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io')(server);
var redis = require('redis');

app.use(express.static(__dirname + '/bower_components'));
app.get('/', function(req, res,next) {
    res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(client) {
    console.log('Client connected...');

    const redis_client = redis.createClient();
    redis_client.connect();
    
    client.on('sub', function(data){
        console.log('sub request for topic ' + data);
        redis_client.subscribe(data, (message) => {
            console.log(message);
            client.emit("article", message)
        });
    });

    client.on('unsub', function(data){
        console.log('unsub request for topic ' + data);
        redis_client.unsubscribe(data);
    })
});

server.listen(4200, function(){
    console.log('listening on *:4200');
});
