from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import sqlite3

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS messages (username TEXT, message TEXT)")
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handle_message(data):
    username = data["username"]
    message = data["message"]

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO messages VALUES (?, ?)", (username, message))
    conn.commit()
    conn.close()

    send(f"{username}: {message}", broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5001, allow_unsafe_werkzeug=True)