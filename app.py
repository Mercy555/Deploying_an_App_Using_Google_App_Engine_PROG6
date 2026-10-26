
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Google App Engine!</h1>" \
           "<p>Cloud Computing Lab application.</p>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
