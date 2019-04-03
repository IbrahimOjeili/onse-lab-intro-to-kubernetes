import os

from flask import Flask, jsonify

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def hello_world():
    recipient = os.getenv("RECIPIENT", "Goodbye my friend")

    return jsonify({"message": "Goodbye my lover", "recipient": recipient})

if __name__ == "__main__":
    app.run()
