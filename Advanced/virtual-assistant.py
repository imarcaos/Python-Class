#
# Bibliotecas - https://pypi.org/ : SpeechRecognition , pyttsx3 , PyAudio, pywhatkit
# PyAudio no Windows : >>> pip install pipwin  and  >>> pipwin install pyaudio
# 28/01/2022

import speech_recognition as sr
import pyttsx3, datetime, pywhatkit

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower() # todo comando de voz é convertido para letra minúscula
            if 'com' in comando:
                comando = comando.replace('com', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Microfone não está ok')

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()

    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando Música')
        maquina.runAndWait()


comando_voz_usuario()