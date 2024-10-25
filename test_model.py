import pytest
import pandas as pd
from backend.model import cargar_datos, limpiar_texto, entrenar_modelo, predecir_respuesta

def test_cargar_datos():
    preguntas, preguntas_normalizadas, intenciones, categorias, respuestas = cargar_datos('faq12.csv')
    assert isinstance(preguntas, pd.Series)
    assert isinstance(intenciones, pd.Series)
    assert len(preguntas) > 0
    assert len(intenciones) > 0

def test_limpiar_texto():
    texto_sucio = "Hola! ¿Cómo estás?"
    texto_limpio = limpiar_texto(texto_sucio)
    assert texto_limpio == "hola como estas"

def test_entrenar_modelo():
    preguntas_normalizadas = ["hola", "como estas"]
    intenciones = ["saludo", "consulta"]
    categorias = ["general", "personal"]
    respuestas = ["Hola, ¿cómo te puedo ayudar?", "Estoy bien, gracias."]
    
    modelo = entrenar_modelo(preguntas_normalizadas, intenciones, categorias, respuestas)
    assert modelo is not None
    assert hasattr(modelo, "predict")

def test_predecir_respuesta():
    # Crear un pequeño dataset de prueba
    datos = pd.DataFrame({
        "pregunta_normalizada": ["hola como estas", "quiero abrir un ticket"],
        "intención": ["saludo", "soporte"],
        "categoria": ["general", "soporte"],
        "respuesta": ["Hola, ¿cómo te puedo ayudar?", "Puedes abrir un ticket aquí:"]
    })

    # Entrenar el modelo con los datos de prueba
    modelo = entrenar_modelo(datos['pregunta_normalizada'], datos['intención'], datos['categoria'], datos['respuesta'])
    
    # Simular una pregunta y predecir la respuesta
    pregunta = "hola como estas"
    respuesta = predecir_respuesta(modelo, pregunta, datos)
    
    assert "Hola, ¿cómo te puedo ayudar?" in respuesta
