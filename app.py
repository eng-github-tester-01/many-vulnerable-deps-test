from flask import Flask
import requests
import yaml
import PIL
import cryptography

app = Flask(__name__)

@app.route('/')
def home():
    return "Vulnerable test app for security scanning"

if __name__ == '__main__':
    app.run(debug=True)
