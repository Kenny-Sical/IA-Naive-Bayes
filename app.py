from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    data = request.get_json()
    texto = data.get('texto', '')
    resultado = f"Texto recibido: {texto[:50]}"
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
