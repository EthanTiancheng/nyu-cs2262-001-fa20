from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask is running!"

@app.route("/time")
def get_time():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"time": now}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

