from flask import Flask, request
import foods

app = Flask(__name__)


@app.route('/safe_foods', methods = ['GET', 'POST'])
def safe_foods():
    state = 'NO_QUERY'
    context = {}

    output = foods.ON_ENTER_STATE[state](context)
    print(output)
    
    while True:
    
        line = request.values.get('text')
        ret = foods.ON_INPUT[state](line, context)
        state, context, optional_output = ret
        if optional_output:
            print(optional_output)

        output = foods.ON_ENTER_STATE[state](context)
        print(output)