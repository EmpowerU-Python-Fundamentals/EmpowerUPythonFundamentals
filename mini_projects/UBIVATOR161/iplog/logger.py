import sqlite3
import datetime
from flask import redirect

DB_FILE = "urls.db"

def log_and_redirect(slug: str, request):
    """Логує IP, User-Agent та робить редірект на цільовий URL."""
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT target_url FROM urls_mapping WHERE slug=?", (slug,))
        row = cur.fetchone()
        if not row:
            return {"error": "not found"}, 404
        target_url = row[0]

        ip_address = request.remote_addr
        user_agent = request.headers.get("User-Agent")
        timestamp = datetime.datetime.utcnow().isoformat()

        cur.execute(
            "INSERT INTO ip_logs (slug, ip_address, user_agent, timestamp) VALUES (?, ?, ?, ?)",
            (slug, ip_address, user_agent, timestamp)
        )
        conn.commit()

    return redirect(target_url, code=302)