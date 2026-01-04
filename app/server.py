from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": "1234"
}

@auth.verify_password
def verify(username, password):
    if username in users and users[username] == password:
        return username

@app.route("/")
@auth.login_required
def home():
    return "Server is working with Basic Auth"

if __name__ == "__main__":
    app.run(port=8000, debug=True)
