var express = require('express');
var app = express();
var http = require('http').Server(app);
var redis = require('redis');

var io = require('socket.io')(http)
app.use('/', express.static('www'));

io.on("connection", (socket) => {
    console.log("user conntected");
    (async () => {
        const client = redis.createClient();
        const subscriber = client.duplicate();
        await subscriber.connect();
        await subscriber.subscribe('article', (message) => {
            console.log(message); // 'message'
            io.emit('article', message);
        });
    })();
})

http.listen(8000, function(){
    console.log('listening on *:8000');
    console.log('Hello g how are you!');
});