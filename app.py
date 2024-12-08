import numpy as np
import pickle
import streamlit as st

model_path = "stunting_model.sav" 
with open(model_path, "rb") as file:
    model = pickle.load(file)

st.title("Prediksi Status Stunting pada Bayi")

age = st.number_input("Umur bayi (bulan)", min_value=0, max_value=60, step=1, help="Masukkan umur bayi dalam bulan")
gender = st.radio("Jenis kelamin bayi", options=[0, 1], format_func=lambda x: "Laki-laki" if x == 0 else "Perempuan", help="Pilih jenis kelamin bayi")
height = st.number_input("Tinggi badan bayi (cm)", min_value=0.000000, max_value=150.00000, step=0.1, help="Masukkan tinggi badan bayi dalam sentimeter")

if st.button("Prediksi Status Gizi"):
    # Validasi input
    if age == 0 or height == 0.0:
        st.error("Semua input harus diisi dengan nilai yang valid.")
    else:
        # Siapkan data untuk prediksi
        input_data = np.array([[age, gender, height]])
        
        # Prediksi status gizi
        prediction = model.predict(input_data)
        
        # Interpretasi hasil prediksi
        if prediction[0] == 0:
            st.success("Hasil Prediksi: Severely stunted")
        elif prediction[0] == 1:
            st.success("Hasil Prediksi: Stunted")
        elif prediction[0] == 2:
            st.success("Hasil Prediksi: normal")
        elif prediction[0] == 3:
            st.success("Hasil Prediksi: Tinggi")
        else:
            st.warning("Hasil prediksi tidak diketahui.")
