from . import db

class Karyawan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)

class Kriteria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_kriteria = db.Column(db.String(100), nullable=False)
    bobot = db.Column(db.Float, nullable=False, default=0.0)

class Kinerja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    karyawan_id = db.Column(db.Integer, db.ForeignKey('karyawan.id'), nullable=False)
    kriteria_id = db.Column(db.Integer, db.ForeignKey('kriteria.id'), nullable=False)
    nilai = db.Column(db.Float, nullable=False)
