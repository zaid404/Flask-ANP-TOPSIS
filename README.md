# Flask-ANP-TOPSIS
###cari kariawan terbaik
## Tangkapan Layar

### Halaman Utama
![Halaman Utama](https://github.com/zaid404/Flask-ANP-TOPSIS/raw/main/index.png)

### Halaman Kinerja
![Halaman Kinerja](https://github.com/zaid404/Flask-ANP-TOPSIS/raw/main/kinerja.png)

### Halaman Matrix ANP
![Halaman Matrix ANP](https://github.com/zaid404/Flask-ANP-TOPSIS/raw/main/matrix.png)

### Penjelasan:
1. **Alur Proses**: Langkah-langkah dari input data hingga peringkat karyawan terbaik dijelaskan secara berurutan.
2. **Instalasi**: Langkah-langkah instalasi dan penggunaan aplikasi Flask disertakan untuk memudahkan setup.



# Kombinasi ANP dan TOPSIS untuk Mencari Karyawan Terbaik

Sistem ini menggunakan kombinasi metode **ANP (Analytic Network Process)** dan **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** untuk memilih karyawan terbaik berdasarkan kriteria yang ditentukan.

## Alur Proses

1. **Input Data Karyawan dan Kriteria Seleksi**
   - Pengguna menginputkan data karyawan beserta kriteria yang digunakan untuk menilai kinerja karyawan.

2. **Penyusunan Supermatrix ANP**
   - Metode ANP digunakan untuk menghitung bobot antar kriteria yang saling terkait, dan membangun supermatrix.

3. **Input Data Kinerja Karyawan**
   - Data kinerja karyawan diinputkan untuk dievaluasi berdasarkan kriteria yang telah ditentukan.

4. **Normalisasi Data Kinerja Karyawan**
   - Data kinerja yang telah dimasukkan dinormalisasi agar dapat digunakan untuk perhitungan lebih lanjut.

5. **Menghitung Nilai Normalisasi Kinerja Dikali Bobot**
   - Data kinerja yang telah dinormalisasi kemudian dikalikan dengan bobot yang diperoleh dari hasil ANP.

6. **Menghitung Jarak Ideal Positif dan Negatif (TOPSIS)**
   - Menggunakan metode TOPSIS untuk menghitung jarak setiap alternatif (karyawan) terhadap solusi ideal positif dan negatif.

7. **Menghitung Nilai Preferensi**
   - Nilai preferensi dihitung berdasarkan jarak yang diperoleh, untuk menentukan karyawan terbaik.

8. **Hasil Peringkat Karyawan**
   - Berdasarkan nilai preferensi, sistem menghasilkan peringkat karyawan terbaik.

## Instalasi

Untuk menjalankan aplikasi ini, ikuti langkah-langkah berikut:

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/zaid404/Flask-ANP-TOPSIS.git
   cd Flask-ANP-TOPSIS
   pip install -r requirements.txt
   flask run
    

