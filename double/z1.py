from flask import Flask

app = Flask(__name__)


@app.route('/z1')
def hello_world1():
    return 'Hello, World1!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=51, debug=True)

