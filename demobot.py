from flask import Flask, request

#https://docs.google.com/document/d/1802LEUy39LOEYrRhZpHqVZPBKNEAmNBVL7Rxhbl3fCs/edit#

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ' Hello, World!'

@app.route('/ncss')
def ncss():
    return '<h1>ncss</h1>'

@app.route('/greet', methods=['GET', 'POST'])
def greet_person():
    name = request.values.get('text')
    return f'hi {name}!'
    if 'bye' in name:
        print('ok good bye then, I hope to never see you again :(')
    
if __name__ == '__main__':
    app.run()


