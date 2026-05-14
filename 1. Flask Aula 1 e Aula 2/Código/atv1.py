from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ""

@app.route('/decorator')
def decorator():
    return "Decorators em Python são funções especiais que permitem modificar, estender ou envolver o comportamento de outras funções ou métodos sem alterar seu código-fonte original."

if __name__ == "__main__":
    app.run(debug=True)