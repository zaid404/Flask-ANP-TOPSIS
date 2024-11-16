import pandas as pd
import numpy as np

def proses_hitung():
    # Step 1: Input Data Karyawan dan Kriteria
    karyawan_df = pd.read_csv('data/karyawan.csv')
    #kriteria_df = pd.read_csv('data/kriteria.csv')

    # Step 2: Penyusunan Supermatrix ANP
    df_matrix_a = pd.read_csv('data/Matrix_A.csv', index_col=0)
    Matrix_A = df_matrix_a.to_numpy()
    column_sums = Matrix_A.sum(axis=0)
    normalized_matrix = Matrix_A / column_sums
    normalized_matrix_df = pd.DataFrame(normalized_matrix)
    normalized_matrix_df.to_csv('data/normalized_matrix.csv', index=False)
    bobot_prioritas = normalized_matrix.mean(axis=1)
    kriteria_df['Bobot'] = bobot_prioritas
    kriteria_df.to_csv('data/kriteria.csv', index=False)

    # Step 3: Input Data Kinerja Karyawan
    kinerja_df = pd.read_csv('data/kinerja.csv')

    # Step 4: Normalisasi Data Kinerja Karyawan
    kinerja_normalized = kinerja_df.iloc[:, 1:].apply(lambda x: (x - x.min()) / (x.max() - x.min()), axis=0)
    kinerja_normalized['Nama Karyawan'] = kinerja_df['Nama Karyawan']
    kinerja_normalized.to_csv('data/normalisasi_kinerja.csv', index=False)

    # Step 5: Menghitung Nilai Terbobot
    nilai_terbobot = kinerja_normalized.iloc[:, :-1].values * bobot_prioritas.reshape(1, -1)
    terbobot_df = pd.DataFrame(nilai_terbobot, columns=kriteria_df['Nama Kriteria'])
    terbobot_df['Nama Karyawan'] = kinerja_normalized['Nama Karyawan']
    terbobot_df.to_csv('data/terbobot.csv', index=False)

    # Step 6: Menghitung Jarak Ideal Positif dan Negatif (TOPSIS)
    A_plus = terbobot_df.iloc[:, :-1].max().values
    A_minus = terbobot_df.iloc[:, :-1].min().values
    D_plus = np.sqrt(((terbobot_df.iloc[:, :-1].values - A_plus) ** 2).sum(axis=1))
    D_minus = np.sqrt(((terbobot_df.iloc[:, :-1].values - A_minus) ** 2).sum(axis=1))
    jarak_ideal_df = pd.DataFrame({'Nama Karyawan': terbobot_df['Nama Karyawan'], 'D+': D_plus, 'D-': D_minus})
    jarak_ideal_df.to_csv('data/jarak_ideal.csv', index=False)

    # Step 7: Menghitung Nilai Preferensi
    C_i = D_minus / (D_plus + D_minus)
    preferensi_df = pd.DataFrame({'Nama Karyawan': terbobot_df['Nama Karyawan'], 'Preferensi': C_i})
    preferensi_df = preferensi_df.sort_values(by='Preferensi', ascending=False).reset_index(drop=True)
    preferensi_df.to_csv('data/preferensi.csv', index=False)

    return preferensi_df
