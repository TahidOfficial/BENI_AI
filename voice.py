import asyncio
import edge_tts
import os

VOICE = "en-US-AriaNeural"

async def speak_async(text):
    communicate = edge_tts.Communicate(text=text, voice=VOICE)
    await communicate.save("beni_voice.mp3")

def speak(text):
    #print("BENI:", text)

    asyncio.run(speak_async(text))

    os.system("start beni_voice.mp3")