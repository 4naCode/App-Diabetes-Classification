zimport streamlit as st
import numpy as np
import joblib

# Load model
def load_model():
    model = joblib.load('diabetes_model.pkl')
    return model
# Fungsi untuk prediksi diabetes
def predict_diabetes(model, input_data):
    prediction = model.predict([input_data])
    return prediction[0]

# Fungsi untuk membaca file CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Panggil fungsi load_css untuk memuat file style.css
load_css("style/style.css")

#load animation
animation_symbol="❄"
#❄❋
st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>

    """,
    unsafe_allow_html=True
)
# Judul aplikasi
#st.title("🚑 Diabetes Classification App")
# Membuat judul dan menerapkan class CSS yang telah dibuat
st.markdown('<p class="centered-title">🚑 Diabetes Prediction App</p>', unsafe_allow_html=True)

# Deskripsi
#st.write("""
# Input the following data for Diabetes Classification
#""")

st.markdown('<p class="centered-text">Aplikasi Prediksi Diabetes adalah sebuah platform interaktif yang dirancang untuk membantu pengguna dalam memprediksi kemungkinan risiko diabetes berdasarkan informasi kesehatan pribadi mereka. Dengan menggunakan algoritma machine learning yang canggih, aplikasi ini menganalisis data yang dimasukkan oleh pengguna untuk memberikan prediksi akurat</p>', unsafe_allow_html=True)

# Membagi form menjadi dua kolom
col1, col2 = st.columns(2)

# Kolom kiri
with col1:
    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, value=0)
    glucose = st.number_input('Glucose', min_value=0, max_value=200, value=120)
    blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=180, value=80)
    skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=99, value=20)

# Kolom kanan
with col2:
    insulin = st.number_input('Insulin', min_value=0, max_value=800, value=85)
    bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, value=25.0)
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, value=0.5)
    age = st.number_input('Age', min_value=1, max_value=120, value=25)

# Menggabungkan input menjadi array
input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]

# Ketika tombol diklik
if st.button('🚨 Predict Diabetes'):
    model = load_model()
    prediction = predict_diabetes(model, input_data)
    
    if prediction == 1:
        st.markdown("<h2 style='color: #ff4d4d;'>Pasien diprediksi menderita Diabetes.</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='color: #76c893;'>Pasien diprediksi tidak menderita Diabetes.</h2>", unsafe_allow_html=True)

# Menampilkan data input
st.write(f'**Data yang diinput:** {input_data}')

# Tambahkan footer
st.markdown("""
            <div class="footer">
                <p>Copyright by <a href="https://noerilagians.blogspot.com/" target="_blank">agian</a></p>
            </div>
            """, unsafe_allow_html=True)


hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
