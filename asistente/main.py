"""
ASISTENTE POR VOZ
"""

import pyttsx3
import speech_recognition as sr

# Voces que hay en el registro
id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

# def audio_a_texto():
#     # Objeto para reconocer el audio
#     r = sr.Recognizer()

#     # Configurar el microfono para capturar el audio
#     with sr.Microphone() as source:

#         # Especificar un tiempo de espera hasta que se activa el microfono
#         r.pause_threshold = 0.8

#         # Mensaje para el usuario para que sepa que ya puede hablar
#         print("Ya puedes hablar")

#         # variable para guardar el audio
#         audio = r.listen(source)

#         try:
#             texto = r.recognize_google(audio, language="es")

#             # Mostrar en pantalla el texto

#             print("Voz reconocida: ", texto)
#         except sr.UnknownValueError:
#             print("El micro no funciona")
#             return "error"
#         except sr.RequestError:
#             print("Falla la transcripción del texto")
#             return "Error"
#         except:
#             print("Error no identificado")
#             return "Error"

# # Lanzo la funcion
# audio_a_texto()

def respuesta_maquina(texto):

    # Iniciar el motor de pyttsx3
    engine = pyttsx3.init()

    # Ajustes 
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150) # velocidad de lectura

    volumen = engine.getProperty("volume")
    engine.setProperty("volume", 1) # volumen

    voz = engine.getProperty("voice")
    engine.setProperty("voice", id1) # seleciona la voz que va a utilizar
    
    # Le indicamos el texto que tiene que decir
    engine.say(texto)

    engine.runAndWait() # Le indicamos que arranque y espere

respuesta_maquina("Hola ¿como estas?")

engine = pyttsx3.init()
for voz in engine.getProperty("voices"): # voces que esta utilizando
    print(voz) # muestra la configuración de voz del registro



        