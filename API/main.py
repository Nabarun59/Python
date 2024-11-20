from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/getUser/<user_id>")
def getUser(user_id):
    user_data = {
        "user_id" : user_id,
        "name" : "Nabarun Samaddar",
        "email" : "nabarun.samaddar59@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

# http://127.0.0.1:5000/getUser/123?extra="ns"

@app.route("/createUser", methods=["POST"])
def createUser():
    data = request.get_json()

    return jsonify(data), 201

# http://127.0.0.1:5000/createUser

if __name__ == "__main__":
    app.run(debug=True)