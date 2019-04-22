from flask import Flask
import init_nfc

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><body><h1>sample</h1></body></html>'

if __name__ == '__main__':
    init_nfc.init()
    app.run()
