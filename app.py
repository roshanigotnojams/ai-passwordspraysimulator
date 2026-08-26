from flask import Flask, render_template, Response
from simulator import password_spray
from detector import detect_password_spray
import json
import time

app = Flask(__name__)


# Home page
@app.route("/")
def dashboard():
    return render_template("dashboard.html")


# Live simulation stream
@app.route("/stream")
def stream():

    def generate():

        logs = []

        for log in password_spray(delay=0):

            logs.append(log)

            detection = detect_password_spray(logs)

            event = {
                "log": log,
                "detection": detection
            }

            yield f"data: {json.dumps(event)}\n\n"

            time.sleep(0.5)

    return Response(
        generate(),
        mimetype="text/event-stream"
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        threaded=True
    )