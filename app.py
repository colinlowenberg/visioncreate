

import streamlit as st
from audiorecorder import audiorecorder
import speech_recognition as sr
import requests
import json


# Products dictionary now without image URLs
products = [
    {"name": "Griffin 🦅", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/de485832688f_34dc35630110_A_highly_stylized_G.usdz"},
    {"name": "Frog King 🐸", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/c2c9bcefe111_d761c49bffb4_frog_with_a_kings_c.usdz"},
    {"name": "Tent 🏕️", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/452c0b28bd81_7ff6f50d39ca_old_tribe_tent__rea.usdz"},
    {"name": "Dragon🦄", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/26f24ef4eb68_6c90e1fb8933_a_realistic_dragon.usdz"},
    {"name": "3D Chibi🏰", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/4b224e3e75ff_b9fa53b58dd4_3D_Chibi_handsome_b.usdz"},
    {"name": "Drone 🚁", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/7686fb5e9628_0b40672d7c22_FPV_drone_with_4_pr.usdz"},
    {"name": "Tiger 🐅", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/8629d582f77a_d0280c1e62ba_Tiger_Cub__Cute__Bi.usdz"},
    {"name": "AK Gun🔫", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/9858ff1dc082_e72e10559b20_an_ak_44_min.usdz"},
    {"name": "Lovebird👽 ", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/9db9c17e30a9_b15c822f8dd9_Lovebird_Cupid_min.usdz"},
    {"name": "Wand🔮", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/bca0509a18c0_528389f3c695_a_magic_wand_covere.usdz"},
    {"name": "Truck🛸", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/f352220bc0a1_567e8c2ce6e1_truck_avia_a31_min.usdz"},
    {"name": "Fake Pokemon🐧", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/8629d582f77a_d0280c1e62ba_Tiger_Cub__Cute__Bi.usdz"},
    {"name": "Dog🐕", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/347F0E0C-F95F-40C4-95D9-D459D67DF613.usdz"},
    {"name": "Disco ball🪩", "usdz_url": "https://pub-1f023e605fa54fa389f2b51cfb51d679.r2.dev/53A4F1B6-2086-4FD2-932C-189DB9F45868.usdz"},

]

# Function to display products with emojis in two columns
def display_products_with_emojis(products):
    st.title('Product Gallery 🎉')
    col1, col2 = st.columns(2)
    for index, product in enumerate(products):
        current_col = col1 if index % 2 == 0 else col2
        with current_col:
            st.write(product["name"])
            st.markdown(f"[Download {product['name'].split(' ')[0]} USDZ]({product['usdz_url']})", unsafe_allow_html=True)

def record_and_transcribe():
    st.title("Create a New Product 🎙️")
    audio = audiorecorder("Click to record", "Click to stop recording", key="recorder")
    
    if len(audio) > 0:
        audio_data = audio.export()  # Export as IO Bytes
        st.audio(audio_data.read(), format="audio/wav")
        audio_file_path = "audio.wav"
        audio.export(audio_file_path, format="wav")
        text = speech_to_text(audio_file_path)
        st.write("Transcribing... ", text)
        # If text is successfully transcribed, call LUMA API
        if text:
            send_to_api_and_display_usdz(text)

def speech_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Error: {str(e)}"

def send_to_api_and_display_usdz(transcribed_text):
    url = 'https://webapp.engineeringlumalabs.com/api/v3/creations'
    headers = {'Authorization': 'luma-api-key=API_KEY_LUMA', 'Content-Type': 'application/json'}
    data = {"input": {"text": transcribed_text, "type": "imagine_3d_one"}}
    
    with st.spinner('Creating USDZ object...'):
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            usdz_url = response.json().get('url')  # Adjust based on actual API response
            if usdz_url:
                st.success('USDZ object is ready!')
                st.balloons()
                st.markdown(f"[Download USDZ Object]({usdz_url})", unsafe_allow_html=True)
        else:
            st.ballons()

def main():
    display_products_with_emojis(products)
    record_and_transcribe()

if __name__ == "__main__":
    main()
