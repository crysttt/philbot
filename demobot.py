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
    if 'bye' in name:
        return('ok good bye then, I hope to never see you again :(')
    else:
        return f'hi {name}!'
    
if __name__ == '__main__':
    app.run()


