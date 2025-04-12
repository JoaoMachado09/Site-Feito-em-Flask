from flask import Flask, render_template
from data import atracoes

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', atracoes=atracoes)

@app.route('/detalhes/<int:id>')
def detalhes(id):
    atracao = next((a for a in atracoes if a["id"] == id), None)
    return render_template('detalhes.html', atracao=atracao)

if __name__ == '__main__':
    app.run(debug=True)