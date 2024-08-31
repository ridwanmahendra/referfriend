import streamlit as st
import openai
from dotenv import load_dotenv
import os
import re

# Memuat variabel dari file .env
load_dotenv()

# Mengambil API Key dari variabel lingkungan
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_research_ideas(topic, num_ideas=3):
    messages = [
        {"role": "system", "content": "Anda adalah AI yang membantu menghasilkan ide penelitian."},
        {"role": "user", "content": f"Hasilkan {num_ideas} ide penelitian yang terkait dengan topik berikut: {topic}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Menggunakan model gpt-3.5-turbo
        messages=messages,
        max_tokens=400,  # Mengatur lebih tinggi untuk menampung beberapa ide
        temperature=0.7,
    )
    
    # Mendapatkan dan membersihkan ide
    raw_ideas = response.choices[0].message['content'].strip()
    
    # Membersihkan dan memformat ide
    cleaned_ideas = re.split(r'\d+\.', raw_ideas)
    
    # Menghapus elemen kosong atau tidak relevan
    return [idea.strip() for idea in cleaned_ideas if idea.strip()]

# Judul aplikasi Streamlit
st.title("Stormer - Universitas Teknokrat Indonesia")

# Deskripsi aplikasi
st.markdown(
    """
    Masukkan topik penelitian Anda dan biarkan AI membantu Anda menghasilkan ide-ide penelitian yang menarik dan kreatif.
    """
)

# Input pengguna untuk topik penelitian
topic = st.text_input("Masukkan topik penelitian:")

if topic:
    # Tombol untuk menghasilkan ide penelitian
    if st.button("Hasilkan Ide"):
        ideas = generate_research_ideas(topic)
        
        # Tampilan hasil yang lebih menarik
        st.subheader("Ide Penelitian:")
        
        # Gunakan expander untuk menampilkan hasil
        with st.expander("Klik untuk melihat ide yang dihasilkan"):
            st.markdown("### Topik: " + topic)
            st.markdown("**Berikut adalah beberapa ide penelitian yang dapat Anda pertimbangkan:**")
            
            # Menampilkan setiap ide tanpa nomor
            for idea in ideas:
                st.markdown(f"- {idea}")  # Menggunakan bullet points

        st.success("Ide berhasil dihasilkan! Lihat detail di atas.")
st.markdown("Dibuat dengan ❤️ oleh Pusat Unggulan Kecerdasan Buatan Universitas Teknokrat Indonesia")