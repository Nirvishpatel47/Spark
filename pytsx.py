import pyttsx3
def say(user_input,voice_index=0):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice',voices[voice_index].id)
    engine.say(user_input)
    engine.runAndWait()

if __name__ == "__main__":
    say(input("Write: "))