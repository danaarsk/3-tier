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
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# API Endpoint untuk mengambil data mahasiswa
@app.route('/mahasiswa', methods=['GET'])
def get_mahasiswa():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM MAHASISWA")
    data = cursor.fetchall()
    cursor.close()
    return jsonify({"mahasiswa": data})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
