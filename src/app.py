from dotenv import load_dotenv
from flask import Flask

from src import Config

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
