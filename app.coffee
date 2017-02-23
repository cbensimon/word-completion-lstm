zerorpc = require 'zerorpc'
client = new zerorpc.Client()
client.connect 'tcp://127.0.0.1:4242'

express = require 'express'
app = express()
server = require('http').Server app
io = require('socket.io') server

app.use express.static 'public'

io.on 'connection', (socket) ->

	socket.on 'predict', (seed) ->

		client.invoke 'predict', seed, (err, res) ->
			console.log err if err
			console.log res
			socket.emit 'predicted', res

server.listen 8080