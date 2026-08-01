import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile

model = whisper.load_model("base")

def listen():
    fs = 16000
    duration = 2

    print("🎤 Speak now...")

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(temp.name, fs, recording)

    result = model.transcribe(
        temp.name,
        fp16=False
    )

    text = result["text"].strip()

    print("You:", text)

    return text.lower()