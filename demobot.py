from flask import Flask, request

#https://docs.google.com/document/d/1802LEUy39LOEYrRhZpHqVZPBKNEAmNBVL7Rxhbl3fCs/edit#
    
foods = {
    'chocolate' : 'no, only humans can enjoy the joy of chocolates',
    'fish' : 'animals can get salmonella too! Sashimi and cooked fish is usually okay',
    'grapes': 'Cats can, dogs cannot, therefore cats > dogs!'
}


app = Flask(__name__)


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


