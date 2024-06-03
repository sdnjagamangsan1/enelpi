import streamlit as st
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk

# Download NLTK data if not already downloaded
nltk.download('punkt')

def calculate_word_frequency(text):
    # Tokenisasi teks
    tokens = word_tokenize(text.lower())
    
    # Hitung frekuensi kemunculan kata
    word_freq = Counter(tokens)
    
    return word_freq

def main():
    st.title('Aplikasi Praktikum NLP Ida Hafizah')
    st.write('Selamat datang di aplikasi praktikum berbasis Streamlit!')

    # Contoh input dan output
    name = st.text_input('Masukkan nama Anda:')
    if name:
        st.write(f'Halo, {name}!')
    
    st.write("## Analisis Frekuensi Kata dengan NLTK")
    st.write("Aplikasi ini akan menghitung frekuensi kemunculan kata dalam teks yang Anda masukkan.")
    
    # Masukkan teks
    text_input = st.text_area("Masukkan teks di sini:")
    
    if st.button("Hitung Frekuensi Kata"):
        if text_input:
            # Hitung frekuensi kata
            word_freq = calculate_word_frequency(text_input)
            
            # Tampilkan hasil
            st.write("Hasil Analisis:")
            for word, freq in word_freq.items():
                st.write(f"- Kata: '{word}', Frekuensi: {freq}")
        else:
            st.write("Silakan masukkan teks untuk dianalisis.")

if __name__ == "__main__":
    main()
