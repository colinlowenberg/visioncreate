""" THIS SCRIPT IS STILL IN DEV 
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


import requests

def send_to_api_and_display_usdz(transcribed_text):
    url = 'https://webapp.engineeringlumalabs.com/api/v3/creations'
    headers = {'Authorization': 'luma-api-key=API_KEY_LUMA', 'Content-Type': 'application/json'}
    data = {"input": {"text": transcribed_text, "type": "imagine_3d_one"}}
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        usdz_url = response.json().get('url')  # Adjust based on actual API response
        if usdz_url:
            print('USDZ object is ready!')
            print(f"Download USDZ Object: {usdz_url}")
        else:
            print('USDZ object URL not found in the response.')
    else:
        print('Failed to create USDZ object.')

# Test the function with a string
send_to_api_and_display_usdz("Your test string here")  """
