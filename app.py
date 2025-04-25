from flask import Flask, render_template, request, jsonify
from naive import predict_from_text, evaluar_modelo
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    data = request.get_json()
    texto = data.get('texto', '')
    
    if texto.strip() == '':
        return jsonify({'resultado': 'Por favor, ingrese texto válido.'})
    
    inicio = time.time()
    prediccion = predict_from_text(texto)
    fin = time.time()
    tiempo_ejecucion = int((fin - inicio) * 1000)
    
    resultado = f'Sentimiento predicho: {prediccion.capitalize()}. Tiempo de ejecución: {tiempo_ejecucion} ms'
    return jsonify({'resultado': resultado})

@app.route('/metricas', methods=['GET'])
def metricas():
    reporte = evaluar_modelo()
    return jsonify({'reporte': reporte})

if __name__ == '__main__':
    app.run(debug=True)
