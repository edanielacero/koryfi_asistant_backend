const express = require('express');
const cors = require('cors');
const app = express();
const port = process.env.PORT || 5003;
const axios = require('axios');

app.use(cors({
  origin: 'https://koryfiasistant-production.up.railway.app',
  methods: ['GET', 'POST', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'],
}));

app.use(express.json());



// Ruta para mostrar algo en el navegador
app.get('/', (req, res) => {
  res.send('Bienvenido al servidor del chatbot');
});

app.listen(port, () => {
  console.log(`Servidor Node.js corriendo en el puerto ${port}`);
});