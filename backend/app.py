import os
from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from dotenv import load_dotenv

# Load konfigurasi dari .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# Koneksi ke MySQL (XAMPP)
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
    database=os.getenv("DB_NAME", "WISATA")
)

# Endpoint untuk mengambil data wisatawan
@app.route('/wisatawan', methods=['GET'])
def get_wisatawan():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM WISATAWAN")
    data = cursor.fetchall()
    cursor.close()
    return jsonify({"wisatawan": data})

# Endpoint untuk mengambil data kategori
@app.route('/kategori', methods=['GET'])
def get_kategori():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM KATEGORI")
    data = cursor.fetchall()
    cursor.close()
    return jsonify({"kategori": data})

# Endpoint untuk mengambil data tempat wisata
@app.route('/tempat_wisata', methods=['GET'])
def get_tempat_wisata():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT TEMPAT_WISATA.*, KATEGORI.NamaKategori 
        FROM TEMPAT_WISATA 
        JOIN KATEGORI ON TEMPAT_WISATA.KategoriID = KATEGORI.KategoriID
    """)
    data = cursor.fetchall()
    cursor.close()
    return jsonify({"tempat_wisata": data})

# Endpoint untuk mengambil data review
@app.route('/review', methods=['GET'])
def get_review():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT REVIEW.*, WISATAWAN.Nama AS NamaWisatawan, TEMPAT_WISATA.NamaTempat 
        FROM REVIEW 
        JOIN WISATAWAN ON REVIEW.WisatawanID = WISATAWAN.WisatawanID
        JOIN TEMPAT_WISATA ON REVIEW.TempatID = TEMPAT_WISATA.TempatID
    """)
    data = cursor.fetchall()
    cursor.close()
    return jsonify({"review": data})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
