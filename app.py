import streamlit as st
from audiorecorder import audiorecorder
import speech_recognition as sr

# Products dictionary now without image URLs
products = [
    {"name": "Griffin", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/de485832688f_34dc35630110_A_highly_stylized_G.usdz"},
    {"name": "Frog King", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/c2c9bcefe111_d761c49bffb4_frog_with_a_kings_c.usdz"},
    {"name": "Tent", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/452c0b28bd81_7ff6f50d39ca_old_tribe_tent__rea.usdz"},
    {"name": "Dragon", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/26f24ef4eb68_6c90e1fb8933_a_realistic_dragon.usdz"},
    {"name": "3D Chibi", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/4b224e3e75ff_b9fa53b58dd4_3D_Chibi_handsome_b.usdz"},
    {"name": "Drone", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/7686fb5e9628_0b40672d7c22_FPV_drone_with_4_pr.usdz"},
    {"name": "Tiger", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/8629d582f77a_d0280c1e62ba_Tiger_Cub__Cute__Bi.usdz"},
]

# Function to display products from a dictionary, including USDZ download
def display_products(products):
    st.title('Product Gallery')
    for product in products:
        st.write(product["name"])
        st.markdown(f"[Download {product['name']} USDZ]({product['usdz_url']})", unsafe_allow_html=True)

# Audio recording and transcription
def record_and_transcribe():
    st.title("Name Your Product")
    audio = audiorecorder("Click to record", "Click to stop recording")
    
    if len(audio) > 0:
        # To play audio in frontend:
        audio_data = audio.export()  # Export as IO Bytes
        st.audio(audio_data.read(), format="audio/wav")
        
        # Save audio to a file
        audio_file_path = "audio.wav"
        audio.export(audio_file_path, format="wav")
        
        # Transcribe audio
        text = speech_to_text(audio_file_path)
        st.write("Product Name Transcription:")
        st.write(text)

def speech_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Error: {str(e)}"

# Main app layout
def main():
    display_products(products)
    record_and_transcribe()

if __name__ == "__main__":
    main()
