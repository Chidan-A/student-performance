import streamlit as st
import pandas as pd
import pickle

# Load model
with open('model_graduation.pkl', 'rb') as file:
    model = pickle.load(file)

# Judul aplikasi
st.title("Prediksi Kategori Masa Studi Mahasiswa")
st.write("Masukkan data berikut untuk memprediksi apakah mahasiswa akan lulus **tepat waktu** atau **terlambat**.")

# Input dari pengguna
ACT = st.number_input("Masukkan nilai ACT composite score", min_value=0.0, max_value=36.0, step=0.1)
SAT = st.number_input("Masukkan nilai SAT total score", min_value=0.0, max_value=1600.0, step=1.0)
GPA = st.number_input("Masukkan nilai rata-rata SMA (GPA)", min_value=0.0, max_value=4.0, step=0.01)
income = st.number_input("Masukkan pendapatan orang tua", min_value=0.0, step=100.0)
education = st.number_input("Masukkan tingkat pendidikan orang tua (angka)", min_value=0.0, step=1.0)

# Tombol prediksi
if st.button("Prediksi Masa Studi"):
    try:
        # Membuat DataFrame dari input
        input_data = pd.DataFrame(
            [[ACT, SAT, GPA, income, education]],
            columns=['ACT composite score', 'SAT total score', 'high school gpa', 'parental income', 'parent_edu_numerical']
        )

        # Prediksi
        prediction = model.predict(input_data)[0]
        label_mapping = {1: "On Time", 0: "Late"}
        hasil = label_mapping.get(prediction, "Tidak diketahui")

        # Output
        st.success(f"Prediksi kategori masa studi: **{hasil}**")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
