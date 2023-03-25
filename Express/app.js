const express = require("express")

const app = express()

app.get("/", (req, res) => {
    res.json({result:"Hello world!".repeat(10000)})
})

app.listen(3000, ()=> console.log("Server started on port 3000"))

// const cluster = require('cluster');
// const numCPUs = require('os').cpus().length;

// if (cluster.isMaster) {
//   console.log(`Master ${process.pid} is running`);

//   // Fork workers
//   for (let i = 0; i < numCPUs; i++) {
//     cluster.fork();
//   }

//   cluster.on('exit', (worker, code, signal) => {
//     console.log(`worker ${worker.process.pid} died`);
//   });
// } else {
//   const express = require('express');
//   const app = express();

//   app.get('/', (req, res) => {
//     res.json({result:"Hello world!".repeat(10000)})
//   });

//   app.listen(3000, () => {
//     console.log(`Worker ${process.pid} started and listening on port 3000`);
//   });
// }
