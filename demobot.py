from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ' Hello, World!'

@app.route('/ncss')
def ncss():
    return '<h1>ncss</h1>'

@app.route('/greet')
def greet_person():
    name = request.values.get('name')
    return f'hi {name}!'

if __name__ == '__main__':
    app.run()


