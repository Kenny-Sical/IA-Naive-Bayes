from flask import Flask, render_template, request, jsonify
from naive import predict_from_text

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
    
    prediccion = predict_from_text(texto)
    resultado = f'Sentimiento predicho: {prediccion.capitalize()}'
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
