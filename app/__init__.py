from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
load_dotenv()

app=Flask(__name__)
app.config.from_object(config)

db= SQLAlchemy(app)
migrate=Migrate(app, db)

from app.model import user, guru, kelas, siswa, kehadiran, mataPelajaran, nilai, laporan
from app import routes