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

// Ruta para manejar las preguntas del chatbot
app.post('/api/chatbot', async (req, res) => {
  const { pregunta } = req.body;

  try {
    // Realiza la petición al servidor Flask en el puerto 5001
    const response = await axios.post('https://model3-production.up.railway.app/api/chatbot', { pregunta });
    const respuestaChatbot = response.data.respuesta;

    res.json({ respuesta: respuestaChatbot });
  } catch (error) {
    console.error('Error al conectar con el chatbot:', error);
    res.status(500).json({ mensaje: 'Error al conectar con el chatbot.' });
  }
});

// Ruta para mostrar algo en el navegador
app.get('/', (req, res) => {
  res.send('Bienvenido al servidor del chatbot');
});

app.listen(port, () => {
  console.log(`Servidor Node.js corriendo en el puerto ${port}`);
});