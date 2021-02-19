from aiogram import types
from aiogram.dispatcher.filters import ContentTypeFilter
from aiogram.dispatcher import FSMContext
import time

from gtts import gTTS
import playsound
import speech_recognition as sr
import pyaudio

import numpy as np
import wavio
import PyWave
import wave
from pydub import AudioSegment
from pydub.playback import play
import fleep


from loader import dp
from config import config_path

@dp.message_handler(content_types=[types.ContentType.VOICE])
async def download_voice(message: types.Message):
    await message.answer("Я получил твое голосовое послание!")
    file = await dp.bot.get_file(message.voice.file_id)
    #convert_wave_file_pac()
    #convert_wave_file()
    #wav2pcm()
    #convert()
    #recognize_command()
    conwert_wave_file_wavio()
    # convert_pywave_file()
    #get_wave_file_info()
    recognize_command()
    await dp.bot.download_file(file.file_path, config_path.PATH_TO_SAVE_VOICE + "voice_" +  str(time.time()) +  ".wav")

    get_wave_file_info()

    file.clean()


def recognize_command():
    try:
        r = sr.Recognizer()
        #audio = open(config_path.PATH_TO_SAVE_VOICE + "voice_1613509823.2372043.oga", "rb")
        with sr.AudioFile(config_path.PATH_TO_SAVE_VOICE + "voice_update3.wav") as source:
            #r.adjust_for_ambient_noise(source)
            audio = r.record(source)
            # recognize speech using Google Speech Recognition
            try:
                our_speech = r.recognize_google(audio, language="ru-RU")
                print("Вы сказали: " + our_speech)
                return r.recognize_google(audio, language="ru-RU")
            except sr.UnknownValueError as esr:
                print("Ошибка recognize_google\n" + repr(esr))
                return "Ошибка"
            except sr.RequestError as e:
                print("Ошибка recognize_google\n" + repr(e))
                return "Ошибка"
    except Exception as e:
        print("Ошибка sr.AudioFile recognize_google\n" + repr(e))


def convert():
    sound = AudioSegment.from_file(r"D:\Python\BotRTLabs\static\voice\voice_1613565101.3835237.wav", format="wav")
    print("Открыл файл mp3")
    sound.export(config_path.PATH_TO_SAVE_VOICE + "voice_1613555310_test23.wav", format="wav")


def wav2pcm():
    f = open(config_path.PATH_TO_SAVE_VOICE + "voice_original.wav", "rb")
    f.seek(1)
    f.read(44)
    data = np.fromfile(f, dtype=np.int16)
    data.tofile(config_path.PATH_TO_SAVE_VOICE + "voice_update2.wav")


def pcm2wav():
    bits = 16
    channels = 1
    sample_rate = 16000
    pcmf = open(config_path.PATH_TO_SAVE_VOICE + "voice_original.wav", 'rb')
    pcmdata = pcmf.read()
    pcmf.close()

    if bits % 8 != 0:
        raise ValueError("bits % 8 must == 0. now bits:" + str(bits))

    wavfile = wave.open(config_path.PATH_TO_SAVE_VOICE + "voice_update2.wav", 'wb')
    wavfile.setnchannels(channels)
    wavfile.setsampwidth(bits // 8)
    wavfile.setframerate(sample_rate)
    wavfile.writeframes(pcmdata)
    wavfile.close()



def get_wave_file_info():

    wav = wave.open(config_path.PATH_TO_SAVE_VOICE + "voice_update.wav", "r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
    print("nchannels = " + str(nchannels))
    print("sampwidth = " + str(sampwidth))
    print("framerate = " + str(framerate))
    print("nframes = " + str(nframes))
    print("comptype = " + str(comptype))
    print("compname = " + str(compname))
    print("---------------------------------\n")
    wav = wave.open("D:\\Python\\BotRTLabs\\static\\voice\\" + "voice-original.wav", "r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
    print("nchannels = " + str(nchannels))
    print("sampwidth = " + str(sampwidth))
    print("framerate = " + str(framerate))
    print("nframes = " + str(nframes))
    print("comptype = " + str(comptype))
    print("compname = " + str(compname))


def convert_pywave_file():
    try:
        PATH = config_path.PATH_TO_SAVE_VOICE + "voice_1613565101.3835237.wav"
        wf = PyWave.open(path=PATH, mode="r")
        print("This WAVE file has the following properties:")
        print(wf.channels, "channels")
        print(wf.frequency, "Hz sample rate")
        print(wf.bitrate, "bits per second")
        print(wf.samples, "total samples")
    except Exception as e:
        print("Ошибка PyWave following properties:\n" + repr(e))

    try:
        wf_copy = PyWave.open(config_path.PATH_TO_SAVE_VOICE + "voice_1613514226.5290203_copy.wav",
                              mode="w",
                              channels=wf.channels,
                              frequency=wf.frequency,
                              bits_per_sample=wf.bits_per_sample,
                              format=wf.format)
        wf_copy.write(wf.read())
        wf.close()
        wf_copy.close()
    except Exception as e:
        print("Ошибка PyWave copy file:\n" + repr(e))




def conwert_wave_file_wavio():
    try:
        with open(config_path.PATH_TO_SAVE_VOICE + "voice_original.wav", 'rb') as pcmfile:
            pcmdata = pcmfile.read()
        with wave.open(config_path.PATH_TO_SAVE_VOICE + "voice_update3.wav", 'wb') as wavfile:
            wavfile.setparams((2, 1, 44100, 0, 'NONE', 'NONE'))
            wavfile.writeframes(pcmdata)
        '''    
        rate = 22050  # samples per second
        T = 3  # sample duration (seconds)
        f = 440.0  # sound frequency (Hz)
        t = np.linspace(2, T, T * rate, endpoint=False)
        x = np.sin(2 * np.pi * f * t)
        data = sr.AudioFile(config_path.PATH_TO_SAVE_VOICE + "voice_original.wav")
        #datar = wavio.read(config_path.PATH_TO_SAVE_VOICE + "voice_update.wav")
        wavio.write(config_path.PATH_TO_SAVE_VOICE + "voice_update.wav", x, rate, sampwidth=3)
        '''
        print("File decode")
    except Exception as e:
        print("Ошибка wavio\n" + repr(e))


#conwert_wave_file_wavio()
#wav2pcm()
#pcm2wav()
#conwert_wave_file_wavio()
#convert_pywave_file()
#get_wave_file_info()
#recognize_command()

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:

        r.adjust_for_ambient_noise(source)
        print("Скажите вашу команду: ")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        our_speech = r.recognize_google(audio, language="ru-RU")
        print("Вы сказали: " + our_speech)
        return r.recognize_google(audio, language="ru-RU")
    except sr.UnknownValueError:
        return "Ошибка"
    except sr.RequestError as e:
        return "Ошибка"


def do_this_command(message):
    message = message.lower()
    if "привет" in message:
        say_message("Привет друг!")
    elif "пока" in message:
        say_message("Пока!")
        exit()
    else:
        say_message("Команда не распознана")


def say_message(message):
    voice = gTTS(message, lang="ru")
    file_voice_name = "audio_" + str(time.time()) + "_" + ".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print(message)


if __name__ == '__main__':
    print("")
    #while True:
        #command = listen_command()
        #do_this_command(command)