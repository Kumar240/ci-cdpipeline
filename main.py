 
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>' 
app.run(host="3.109.5.147" , port=5000, debug=True)
