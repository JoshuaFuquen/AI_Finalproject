# AI Text Classification with xAI Grok LLM

Un proyecto de clasificación de sentimientos usando un LLM (Large Language Model) como el "cerebro" para analizar y clasificar reseñas de texto.

## 📋 Descripción del Proyecto

Este proyecto utiliza **xAI Grok**, un modelo de lenguaje avanzado, para clasificar automáticamente reseñas cortas como **positivas** o **negativas**. En lugar de usar algoritmos tradicionales de machine learning, el LLM actúa como el cerebro inteligente que entiende el contexto y el sentimiento del texto.

### ¿Cómo funciona?

1. El programa proporciona ejemplos de entrenamiento al LLM (20 reseñas etiquetadas como positivas o negativas)
2. El LLM aprende el patrón de clasificación basado en estos ejemplos
3. El modelo clasifica nuevas reseñas que nunca ha visto antes
4. Retorna la clasificación: "positive" o "negative"

## 📁 Estructura de Archivos

```
ai_classifier_llm/
├── main.py                  # Archivo principal del proyecto
├── requirements.txt         # Dependencias de Python
├── .gitignore              # Protege archivos sensibles (credenciales)
├── API_KEY_SETUP.txt       # Instrucciones para configurar la clave API
└── README.md               # Este archivo
```

### Descripción de cada archivo:

- **main.py**: El programa principal que contiene:
  - Dataset de entrenamiento (20 reseñas con etiquetas)
  - Función para crear el prompt del sistema (enseña al LLM cómo clasificar)
  - Función para llamar a la API de xAI
  - Clasificación de 5 nuevas reseñas usando el LLM

- **requirements.txt**: Lista de librerías necesarias:
  - `requests`: Para hacer peticiones HTTP a la API de xAI
  - `python-dotenv`: Para cargar variables de entorno desde .env

- **.gitignore**: Protege tus credenciales evitando que se suban a GitHub:
  - Archivos `.env` y `.env.local` (nunca se enviarán a git)
  - Archivos de caché de Python
  - Archivos de IDE

- **API_KEY_SETUP.txt**: Instrucciones detalladas para obtener y configurar tu clave API de xAI

## 🚀 Cómo Usar

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar tu clave API de xAI

Lee el archivo **API_KEY_SETUP.txt** para obtener instrucciones detalladas.

Opción rápida:
```bash
# Crear archivo .env
echo "XAI_API_KEY=tu-clave-api-aqui" > .env
```

### 3. Ejecutar el programa

```bash
python main.py
```

## 🔐 Seguridad - Proteger tus Credenciales

**IMPORTANTE**: Tu clave API es sensible y debe protegerse.

✅ **Lo que debes hacer:**
- Usar `.env` o `.env.local` para guardar tu clave API
- Nunca compartir tu clave API
- El `.gitignore` ya previene que se suban a GitHub

❌ **Nunca hagas esto:**
- Escribir la clave directamente en el código
- Compartir archivos `.env` públicamente
- Subir la clave a GitHub

## 📊 Entrada y Salida

### Entrada:
- 20 ejemplos de reseñas etiquetadas (en el código)
- 5 nuevas reseñas para clasificar (en el código)

### Salida:
```
Review 1: "This is the best thing I ever bought!"
Predicted Sentiment: ✓ POSITIVE

Review 2: "Complete garbage, do not buy."
Predicted Sentiment: ✗ NEGATIVE

...
```

## 🧠 ¿Cómo el LLM es el "Cerebro"?

El LLM (Grok) es el cerebro porque:

1. **Entiende contexto**: Analiza no solo palabras individuales, sino el significado completo
2. **Aprende patrones**: De los 20 ejemplos de entrenamiento aprende cómo identificar sentimientos
3. **Generaliza**: Puede clasificar reseñas que nunca ha visto antes
4. **Flexible**: Entiende variaciones del lenguaje, sarcasmo, y matices de sentimiento

## 🔧 Requisitos

- Python 3.8+
- Conexión a Internet (para llamar a la API de xAI)
- Clave API válida de xAI

## 📝 Notas

- La temperatura está configurada a 0 para resultados consistentes
- El modelo usa `grok-beta` como nombre del modelo
- La respuesta se limita a 10 tokens (solo necesitamos una palabra)
- Los ejemplos de entrenamiento están incluidos en el código

## 🤝 Próximos Pasos

Puedes modificar este proyecto:
- Agregar más ejemplos de entrenamiento
- Cambiar el prompt del sistema para diferentes tipos de clasificación
- Usar diferentes parámetros de temperatura
- Integrar una base de datos para guardar resultados

---

**Autor**: AI 100 Final Project  
**Fecha**: 2026  
**Versión**: 1.0
