import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening... Speak something!")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        # Using the Google Web Speech API for speech recognition
        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return None

    except sr.RequestError:
        print("Sorry, my speech recognition service is currently unavailable.")
        return None

if __name__ == "__main__":
    while True:
        result = speech_to_text()
        if result:
            print(f"You said: {result}")
            if result.lower() == "exit":
                print("Exiting the program.")
                break
