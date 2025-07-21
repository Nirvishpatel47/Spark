import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json



def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def main():
    # Path to your downloaded model folder
    MODEL_PATH = r"D:\HTML tutorial\vosk-model-small-en-us-0.15"

    # Sampling rate (must match model requirements)
    SAMPLE_RATE = 16000

    # Initialize the model and recognizer
    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, SAMPLE_RATE)

    # Queue to hold audio chunks
    global q
    q = queue.Queue()
    print("🗣️ Please start speaking. Press Ctrl+C to stop.")
    with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=8000, dtype='int16',
                           channels=1, callback=audio_callback):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                text = json.loads(result).get("text", "")
                if text:
                    print("You said:", text)
                    return text
            else:
                # Partial result while speaking
                partial = recognizer.PartialResult()
                # Uncomment below if you want to see partial results live
                # print(json.loads(partial).get("partial", ""))

if __name__ == "__main__":
    main()
