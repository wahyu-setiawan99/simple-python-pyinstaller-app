'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

from flask import Flask, request, render_template_string
from calc import add2
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    result = None

    if request.method == 'POST':
        first_argument = request.form['first-argument']
        second_argument = request.form['second-argument']
        try:
            # Ensure no spaced word enter and argument is only 2
            first_argument = str(first_argument).strip()
            second_argument = str(second_argument).strip()
            arguments = len(first_argument.split()) + \
                len(second_argument.split())
            if arguments != 2:
                raise ValueError(
                    "Invalid input. Please enter two arguments without spaces.")

            result = add2(first_argument, second_argument)
        except ValueError as e:
            error_message = str(e)

    return render_template_string("""
    <style>
        body {
            background-color: #333;
            color: white;
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        
        h1 {
            margin-bottom: 20px;
        }
        
        form {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 10px;
        }
        
        input[type="text"] {
            width: 200px;
            padding: 5px;
            margin-bottom: 10px;
        }
        
        input[type="submit"] {
            padding: 10px 20px;
            background-color: #4caf50;
            color: white;
            border: none;
            cursor: pointer;
        }
        
        #result {
            font-size: 18px;
            font-weight: bold;
        }
        
        .error {
            color: red;
        }
    </style>
    
    <h1>Add2vals App</h1>
    <form method="post">
        <label for="first-argument">First Argument:</label>
        <input type="text" name="first-argument" id="first-argument" required>
        <br>
        <label for="second-argument">Second Argument:</label>
        <input type="text" name="second-argument" id="second-argument" required>
        <br>
        <input type="submit" value="Calculate">
    </form>

    {% if error_message %}
    <div class="error">
        {{ error_message }}
    </div>
    {% endif %}
    
    <div id="result">
        {% if result %}
        The result is {{ result }}
        {% endif %}
    </div>
    """, error_message=error_message, result=result)


if __name__ == "__main__":
    app.run()

# if __name__ == "__main__":
#     port = int(os.environ.get('PORT', 5001))
#     app.run(debug=True, host='0.0.0.0', port=port)
