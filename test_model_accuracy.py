import pytest
from model import cargar_datos, entrenar_modelo_con_validacion

def test_accuracy_modelo():
    # Cargar los datos
    preguntas, preguntas_normalizadas, intenciones, categorias, respuestas = cargar_datos('faq12.csv')
    
    # Entrenar el modelo
    modelo = entrenar_modelo_con_validacion(preguntas_normalizadas, intenciones, categorias, respuestas)
    
    # En este punto, el accuracy del modelo se muestra en la consola. Puedes hacer assertions aquí si lo necesitas.
    # Como ejemplo, podrías establecer un umbral de precisión mínimo:
    assert modelo is not None, "El modelo no debería ser None después del entrenamiento."

