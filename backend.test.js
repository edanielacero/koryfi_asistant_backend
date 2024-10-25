const request = require('supertest');
const app = require('../app'); // Asegúrate de que 'app' sea el archivo que contiene la configuración de tu servidor backend

describe('POST /api/chatbot', () => {
  it('Debe responder con un estado 200 y devolver una respuesta JSON', async () => {
    const res = await request(app)
      .post('/api/chatbot')
      .send({ pregunta: '¿Cómo estás?' }); // Simula enviar una pregunta al chatbot
    
    expect(res.statusCode).toBe(200); // Verifica que el status sea 200 OK
    expect(res.body).toHaveProperty('respuesta'); // Verifica que el JSON contenga la propiedad "respuesta"
  });
});
