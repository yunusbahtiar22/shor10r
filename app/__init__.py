from flask import Flask, jsonify


# instanciate the app
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
        "message": "Hello from shor10r",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)
