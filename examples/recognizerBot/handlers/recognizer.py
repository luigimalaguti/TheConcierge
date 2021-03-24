import subprocess
import speech_recognition

from telethon import events


@events.register(events.NewMessage)
async def voice(event):
    if event.voice:
        voice_oga = "files/voice.oga"
        voice_wav = "files/voice.wav"
        await event.download_media(voice_oga)
        process = subprocess.run(["ffmpeg", "-loglevel", "quiet", "-i", voice_oga, "-y", voice_wav])
        recognizer = speech_recognition.Recognizer()
        voice = speech_recognition.AudioFile(voice_wav)
        with voice as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        await event.reply(text)
