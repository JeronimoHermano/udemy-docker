const express = require('express')
const restful = require('node-restful')
const bodyParser = require('body-parser')
const cors = require('cors')

const server = express()
const mongoose = restful.mongoose


// Database
mongoose.Promisse = global.Promise
mongoose.connect('mongodb://db/mydb') //:27017

// Teste
server.get('/', (req, res, next) => {
    res.send('backend')
})

// Middlewares
server.use(bodyParser.urlencoded({ extended: true }))
server.use(bodyParser.json())
server.use(cors())

// ODM
const Client = restful.model('Cliente', {
    name: {
        type: String,
        required: true
    }
})

// Rest API
Client.methods(['get', 'post', 'put', 'delete'])
Client.updateOptions({ new: true, runValidators: true })

// Routes
Client.register(server, '/clients')

// Start server
server.listen(3000)
