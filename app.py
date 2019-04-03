import os

from flask import Flask, jsonify

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def hello_world():
    recipient = os.getenv("RECEIVER", "Goodbye my friend")

    return jsonify({"message": "Hello", "recipient": recipient, "result": "OK"})

if __name__ == "__main__":
    app.run()
