from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class KaryawanForm(FlaskForm):
    nama = StringField('Nama Karyawan', validators=[DataRequired()])
    submit = SubmitField('Simpan')

class KriteriaForm(FlaskForm):
    nama_kriteria = StringField('Nama Kriteria', validators=[DataRequired()])
    bobot = FloatField('Bobot', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Simpan')
