from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Lab Work №3 - done! Smikh Maxym, IPZ-42"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)