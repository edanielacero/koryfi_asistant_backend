import unittest
from backend.model import app  # Importa la aplicación Flask desde server.js

class TestFlaskApp(unittest.TestCase):
    # Configura el cliente de pruebas antes de cada prueba
    def setUp(self):
        self.app = app.test_client()  # Crea un cliente de pruebas
        self.app.testing = True

    # Prueba de POST a la ruta /api/chatbot
    def test_chatbot_response(self):
        response = self.app.post('/api/chatbot', json={'pregunta': '¿Qué tal?'})
        self.assertEqual(response.status_code, 200)  # Verifica que el código de estado sea 200
        self.assertIn('respuesta', response.get_json())  # Verifica que la respuesta tenga la clave "respuesta"

if __name__ == '__main__':
    unittest.main()
