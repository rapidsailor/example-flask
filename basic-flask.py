from flask import Flask
app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return 'reply from koyeb'


if __name__ == "__main__":
    app.run()
