from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'
from flask import Flask, request, jsonify

app = Flask(__name__)

def sum_of_digits(number):
    try:
        # Ensure the number is an integer
        num = int(number)
        # Convert number to string and sum its digits
        return sum(int(digit) for digit in str(abs(num)))
    except ValueError:
        return None

@app.route('/sum_of_digits', methods=['GET'])
def get_sum_of_digits():
    number = request.args.get('number')
    if number is None:
        return jsonify({'error': 'Number parameter is required'}), 400

    result = sum_of_digits(number)
    if result is None:
        return jsonify({'error': 'Invalid number format'}), 400

    return jsonify({'sum_of_digits': result})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/about')
def about():
    return 'About'
