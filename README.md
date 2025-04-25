# IA-Naive-Bayes

## Instalación
1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/proyecto-naive-bayes.git
cd proyecto-naive-bayes
```
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```
3. Ejecuta el servidor:
```bash
python app.py
```

## Uso
- Abre tu navegador y visita: `http://127.0.0.1:5000`
- Ingresa un texto en el área de entrada.
- Presiona **"Enviar"** para obtener el sentimiento del texto.
- Presiona **"Ver métricas del modelo"** para visualizar el desempeño del clasificador.

## Arquitectura del proyecto
proyecto-naive-bayes/
│
├── app.py               # Servidor Flask
├── naive.py             # Implementación del clasificador Naive Bayes y evaluación
├── modelo_naive.pkl     # Modelo entrenado y serializado
├── twitter_training.csv # Dataset con tweets etiquetados
│
├── templates/
│   └── index.html       # Interfaz web (HTML)
│
├── static/
│   ├── css/
│   │   └── style.css    # Estilos de la interfaz
│   └── js/
│       └── script.js
│
└── README.md            # Este documento

## Descripción de Archivos

| Archivo                 | Descripción                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `app.py`                | Define las rutas `/`, `/procesar`, `/metricas`. Renderiza la interfaz.      |
| `naive.py`              | Contiene el modelo Naive Bayes, el entrenamiento y la evaluación.           |
| `modelo_naive.pkl`      | Archivo serializado del modelo entrenado.                                   |
| `twitter_training.csv`  | Dataset con ejemplos de entrenamiento y evaluación.                         |
| `index.html`            | Página web principal con formulario y botones.                              |
| `style.css`             | Estilo visual de la interfaz.                                               |
| `script.js`             | Código que conecta el frontend con el backend vía JavaScript                |

## Tecnologías Utilizadas

- **Python** (v3.10+)
- **Flask**: Framework para servidor web
- **HTML + CSS + JS**: Interfaz web
- **Naive Bayes**: Clasificador probabilístico
- **scikit-learn**: Solo para métricas de evaluación
- **Pickle**: Serialización del modelo entrenado