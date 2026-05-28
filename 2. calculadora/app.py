from flask import Flask, render_template, request
from calculadora import calcular

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    etapas = ""
    resultados = ""
    
    if request.method == 'POST':
        etapas, resultados = calcular()
    
    return render_template('calculadora.html', etapas=etapas, resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)