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
@app.route('/isMess', methods=['GET'])
def isMess():
    name = request.args.get('mname')
    if name is None:
        return jsonify({'error': 'Scan again'}), 400

    result = ''
    if name == "BH6M02":
        result = "Mess-2 BH-6"
    if result is None:
        return jsonify({'error': 'Invalid Mess'}), 400

    return jsonify({'Acess granted to': result})
@app.route('/getData', methods=['GET'])
def getData():
    id = request.args.get('id')
    token = "9daacfb1e97a628660431de6c9442481"
    url = "https://lpulive.lpu.in/fugu-api/api/chat/groupChatSearch?en_user_id={}&search_text={}&user_role=USER".format(
        token, id
    )
    try:
        res = requests.get(
            url, headers={"app_version": "1.0.0", "device_type": "WEB"}
        ).json()
        users = res["data"]["users"]
        if len(users) == 0:
            return {"detail": "No user found."}

        return(users[0])
    except:
        return "error"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/about')
def about():
    return 'About'
