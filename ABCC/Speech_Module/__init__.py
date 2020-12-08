import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 140)


class speech:
    def __init__(self):
        pass

    def mic_input(self):
        """
        Fetch input from mic
        :return: user's voice input as text if true, false if fail
        """
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('Say something...')
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
            try:
                command = r.recognize_google(audio).lower()
                print('You said: ' + command + '\n')
            except sr.UnknownValueError:
                print('....')
                command = self.mic_input()
            return command
        except Exception as e:
            print(e)
            return False

    def t2s(self, text):
        """
        Convert any text to speech
        :param text: text (String)
        :return: True / False (Play sound if True otherwise write exception to log and return False)
        """
        engine.say(text)
        engine.runAndWait()