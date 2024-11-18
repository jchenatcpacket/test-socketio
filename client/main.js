const { io } = require("socket.io-client");

const socket = io("http://server:8000")
// const socket = io("http://sanic:8003")

socket.on("connect", () => {
    console.log(`[${new Date().toISOString()}]`, socket.id);
});

socket.on("disconnect", () => {
    console.log(`[${new Date().toISOString()}]`,socket.id);
});


socket.on('my event', (data) => {
    console.log(`[${new Date().toISOString()}]`, 'Received message:', data);
});

socket.io.on("error", (error) => {
    console.log(`[${new Date().toISOString()}]`, error)
});

socket.on("connect_error", (error) => {
    if (socket.active) {
        console.log(`[${new Date().toISOString()}]`, "active connection");
    } else {
      console.log(`[${new Date().toISOString()}]`, error.message);
    }
});