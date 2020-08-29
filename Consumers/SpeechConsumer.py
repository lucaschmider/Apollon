from google.oauth2.service_account import Credentials
from google.cloud.texttospeech import \
    SynthesisInput, \
    VoiceSelectionParams, \
    TextToSpeechClient, \
    SsmlVoiceGender, \
    AudioConfig, \
    AudioEncoding
from pygame import mixer
from Consumers.ConsumerBase import ConsumerBase


class SpeechConsumer(ConsumerBase):
    __client__: TextToSpeechClient = None
    __TEMPORARY_FILE__: str = "output.wav"

    def __init__(self, service_account__file: str):
        credentials = Credentials.from_service_account_file(
            service_account__file)
        self.__client__ = TextToSpeechClient(credentials=credentials)
        mixer.init()

    def prepare_consumption(self, message: str) -> None:
        self.synthesize_text(message, self.__TEMPORARY_FILE__)

    def consume(self, message: str) -> None:
        mixer.music.load(self.__TEMPORARY_FILE__)
        mixer.music.play()
        while mixer.music.get_busy():
            pass

    def synthesize_text(self, text: str, output_location: str) -> None:
        """Synthesizes speech from the input string of text."""

        input_text = SynthesisInput(text=text)
        voice = VoiceSelectionParams(
            language_code="de-DE",
            name="de-DE-Wavenet-E",
            ssml_gender=SsmlVoiceGender.FEMALE,
        )
        audio_config = AudioConfig(
            audio_encoding=AudioEncoding.LINEAR16
        )
        response = self.__client__.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config}
        )

        with open(output_location, "wb") as out:
            out.write(response.audio_content)
            print('Audio content written to file "'+ output_location + '"')
