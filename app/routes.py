from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Karyawan, Kriteria, Kinerja
from .forms import KaryawanForm, KriteriaForm
from flask import current_app as app
from .hitung import proses_hitung
import pandas as pd
# Define the blueprint for the main routes
main = Blueprint('main', __name__)
# Halaman Utama
@main.route('/')
def index():
    preferensi_file = 'data/preferensi.csv'
    df = pd.read_csv(preferensi_file)
    df.insert(0, 'Nomor', range(1, len(df) + 1))
    return render_template('base.html', tabel=df)

@main.route('/proses', methods=['POST'])
def proses():
    try:
        hasil = proses_hitung()
        data = hasil.to_dict(orient='records')
        return render_template('hasil.html', data=data)
    except Exception as e:
        flash(f"Terjadi kesalahan: {str(e)}", "danger")
        return redirect(url_for('main.index'))

@main.route('/edit_matrix', methods=['GET', 'POST'])
def edit_matrix():
    matrix_file = 'data/Matrix_A.csv'
    
    if request.method == 'POST':
        # Ambil data dari form dan update Matrix_A.csv
        try:
            data = request.form.to_dict(flat=False)
            criteria = list(pd.read_csv(matrix_file, index_col=0).columns)
            
            # Konversi form data menjadi DataFrame
            updated_data = []
            for i in criteria:
                row = [float(data[f"{i}-{j}"][0]) for j in criteria]
                updated_data.append(row)
            
            updated_df = pd.DataFrame(updated_data, index=criteria, columns=criteria)
            updated_df.to_csv(matrix_file)
            
            flash("Matrix_A.csv berhasil diperbarui!", "success")
            return redirect(url_for('main.edit_matrix'))
        except Exception as e:
            flash(f"Terjadi kesalahan: {e}", "danger")
            return redirect(url_for('main.edit_matrix'))
    
    # Metode GET: Tampilkan form edit
    df_matrix = pd.read_csv(matrix_file, index_col=0)
    return render_template('edit_matrix.html', criteria=df_matrix.index, matrix=df_matrix)
@main.route('/kinerja', methods=['GET', 'POST'])
def kinerja():
    matrix_file = 'data/kinerja.csv'
    
    if request.method == 'POST':
        action = request.form.get('action')
        df = pd.read_csv(matrix_file, index_col=0)

        if action == 'update':
            # Update data
            try:
                data = request.form.to_dict(flat=False)
                for name in df.index:
                    for column in df.columns:
                        key = f"{name}-{column}"
                        if key in data:
                            df.loc[name, column] = float(data[key][0])
                df.to_csv(matrix_file)
                flash("Data kinerja berhasil diperbarui!", "success")
            except Exception as e:
                flash(f"Terjadi kesalahan saat memperbarui data: {e}", "danger")

        elif action == 'add':
            # Tambah data
            try:
                new_name = request.form.get('new_name')
                new_values = [float(request.form.get(f'new_{col}', 0)) for col in df.columns]
                if new_name and new_name not in df.index:
                    df.loc[new_name] = new_values
                    df.to_csv(matrix_file)
                    flash("Data baru berhasil ditambahkan!", "success")
                else:
                    flash("Nama karyawan sudah ada atau kosong!", "danger")
            except Exception as e:
                flash(f"Terjadi kesalahan saat menambah data: {e}", "danger")

        elif action == 'delete':
            # Hapus data
            try:
                names_to_delete = request.form.getlist('delete_names')
                df = df.drop(index=names_to_delete, errors='ignore')
                df.to_csv(matrix_file)
                flash("Data karyawan berhasil dihapus!", "success")
            except Exception as e:
                flash(f"Terjadi kesalahan saat menghapus data: {e}", "danger")

        return redirect(url_for('main.kinerja'))

    # Metode GET: Tampilkan form edit
    df_matrix = pd.read_csv(matrix_file, index_col=0)
    return render_template(
        'edit_kinerja.html',
        rows=df_matrix.index,
        columns=df_matrix.columns,
        matrix=df_matrix
    )
