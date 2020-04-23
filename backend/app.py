from flask import Flask
from api import helloworld

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


app.register_blueprint(helloworld.bluePrint)

if __name__ == '__main__':
    app.run()
