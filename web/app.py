from flask import Flask, request, redirect
import os
import time
import psycopg2

app = Flask(__name__)

def connect_db():
    for i in range(30):
        try:
            return psycopg2.connect(
                host=os.getenv("DB_HOST", "db"),
                dbname=os.getenv("POSTGRES_DB", "bookstore"),
                user=os.getenv("POSTGRES_USER", "bookuser"),
                password=os.getenv("POSTGRES_PASSWORD", "bookpass")
            )
        except psycopg2.OperationalError:
            time.sleep(2)
    raise Exception("Database connection failed")

def query(sql, values=(), one=False):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(sql, values)
    result = cur.fetchone() if one else cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return result

def query(sql, values=(), one=False):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(sql, values)

    if cur.description is None:
        result = None
    else:
        result = cur.fetchone() if one else cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()
    return result
@app.route("/")
def home():
    books = query("SELECT id,title,author,price FROM books ORDER BY id")
    html = """
    <h1>Online Bookstore</h1>
    <h2>Danh sach sach</h2>
    <a href='/add'>+ Them sach</a><hr>
    """
    for b in books:
        html += f"""
        <p><b>{b[1]}</b> - {b[2]} - {b[3]} VND
        <a href='/book/{b[0]}'>Chi tiet</a>
        <a href='/edit/{b[0]}'>Sua</a>
        <a href='/delete/{b[0]}'>Xoa</a></p>
        """
    return html

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        query("INSERT INTO books(title,author,price) VALUES(%s,%s,%s)",
              (request.form["title"], request.form["author"],
               float(request.form["price"])))
        return redirect("/")
    return """
    <h1>Them sach</h1>
    <form method='post'>
    Ten sach: <input name='title' required><br>
    Tac gia: <input name='author' required><br>
    Gia: <input name='price' type='number' step='0.01' required><br>
    <button>Luu sach</button></form><a href='/'>Quay lai</a>
    """

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    b = query("SELECT * FROM books WHERE id=%s", (id,), True)
    if not b:
        return "Khong tim thay sach", 404
    if request.method == "POST":
        query("UPDATE books SET title=%s,author=%s,price=%s WHERE id=%s",
              (request.form["title"], request.form["author"],
               float(request.form["price"]), id))
        return redirect("/")
    return f"""
    <h1>Sua sach</h1><form method='post'>
    Ten sach: <input name='title' value='{b[1]}' required><br>
    Tac gia: <input name='author' value='{b[2]}' required><br>
    Gia: <input name='price' type='number' step='0.01'
    value='{b[3]}' required><br>
    <button>Cap nhat</button></form><a href='/'>Quay lai</a>
    """

@app.route("/delete/<int:id>")
def delete(id):
    query("DELETE FROM books WHERE id=%s", (id,))
    return redirect("/")

@app.route("/book/<int:id>")
def detail(id):
    b = query("SELECT * FROM books WHERE id=%s", (id,), True)
    if not b:
        return "Khong tim thay sach", 404
    return f"<h1>{b[1]}</h1><p>Tac gia: {b[2]}</p><p>Gia: {b[3]} VND</p><a href='/'>Quay lai</a>"

@app.route("/health")
def health():
    query("SELECT 1")
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
