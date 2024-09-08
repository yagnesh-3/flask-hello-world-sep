from flask import Flask, jsonify
import requests

app = Flask(_name_)


@app.route('/get_data', methods=['GET'])
def get_data():
    """
    API endpoint to get user details from LPU Live.
    """
    id = "12223854"
    token = "9daacfb1e97a628660431de6c9442481"
    url = "https://lpulive.lpu.in/fugu-api/api/chat/groupChatSearch?en_user_id={}&search_text={}&user_role=USER".format(
        token, id
    )
    try:
        res = requests.get(
            url, headers={"app_version": "1.0.0", "device_type": "WEB"}
        ).json()

        users = res.get("data", {}).get("users", [])

        if not users:
            return jsonify({"detail": "No user found."}), 404

        return jsonify({"users": users}), 200

    except Exception as e:
        return jsonify({"error": "error-2", "message": str(e)}), 500


if _name_ == '_main_':
    app.run(debug=True)
