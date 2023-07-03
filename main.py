import speech_recognition as sr

r = sr.Recognizer()

def voice_to_text():
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Request error: {e}")

# Call the voice_to_text function to convert speech to text
text = voice_to_text()
print("Text:", text)

if __name__ == "__main__":
    text = voice_to_text()
    print("Text:", text)
