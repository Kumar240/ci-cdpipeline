from flask import Flask

app = Flask(__name__)

@app.route(“3.109.5.147/”)

def home():

return “<h1>Hello World!</h1>”
