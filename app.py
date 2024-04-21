from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Home Page"

@app.route('/about', methods=['GET'])
def about():
    return "About KT - RH Media Api"


if __name__ == '__main__':
    app.run()