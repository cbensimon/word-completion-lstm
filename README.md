# LSTM based word completion

- Trained two stacked LSTM using Keras on my peronal sent text messages
- The produced Keras model is run as a Python service using zerorpc
- A Node.js server makes use of the service
- and communicate with the front using web sockets