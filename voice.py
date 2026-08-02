import asyncio
import edge_tts
import pygame
import os
import time

VOICE = "en-IN-NeerjaNeural"

pygame.mixer.init()

async def speak_async(text):
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate="+20%",
        pitch="+0Hz"
    )
    await communicate.save("beni_voice.mp3")


def speak(text):
    asyncio.run(speak_async(text))

    pygame.mixer.music.load("beni_voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()

    try:
        os.remove("beni_voice.mp3")
    except:
        pass