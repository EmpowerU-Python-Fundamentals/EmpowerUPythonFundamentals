import os
import sqlite3
import datetime
from flask import Flask, request, jsonify, abort
from functools import wraps
from logger import log_and_redirect

app = Flask(__name__)

APP_LOGIN = os.getenv("APP_LOGIN", "admin")
APP_PASSWORD = os.getenv("APP_PASSWORD", "admin")
DB_FILE = "urls.db"

def init_db():
    """Ініціалізація БД (якщо ще не існує)."""
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS urls_mapping (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slug TEXT UNIQUE NOT NULL,
                target_url TEXT NOT NULL
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ip_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slug TEXT NOT NULL,
                ip_address TEXT NOT NULL,
                user_agent TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def check_auth(username, password):
    return username == APP_LOGIN and password == APP_PASSWORD

def require_auth(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return abort(401)
        return f(*args, **kwargs)
    return decorated

@app.route("/admin/create", methods=["POST"])
@require_auth
def admin_create_url():
    data = request.get_json()
    if not data or "slug" not in data or "target_url" not in data:
        return jsonify({"error": "slug and target_url required"}), 400

    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO urls_mapping (slug, target_url) VALUES (?, ?)",
                (data["slug"], data["target_url"])
            )
            conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({"error": "Slug already exists"}), 400

    return jsonify({"message": "URL mapping created"}), 201

@app.route("/admin/list", methods=["GET"])
@require_auth
def admin_list_urls():
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT slug, target_url FROM urls_mapping")
        rows = cur.fetchall()
    return jsonify([{"slug": r[0], "target_url": r[1]} for r in rows])

@app.route("/admin/logs", methods=["GET"])
@require_auth
def admin_read_url_logs():
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT slug, ip_address, user_agent, timestamp FROM ip_logs ORDER BY id DESC")
        rows = cur.fetchall()
    return jsonify([{"slug": r[0], "ip_address": r[1], "user_agent": r[2], "timestamp": r[3]} for r in rows])

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5001)