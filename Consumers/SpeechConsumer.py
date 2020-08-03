import time

from Consumers.ConsumerBase import ConsumerBase
from google.cloud import texttospeech
from google.oauth2 import service_account
import playsound


class SpeechConsumer(ConsumerBase):
    __client__ = None  # type: texttospeech.TextToSpeechClient

    def __init__(self, service_account__file: str):
        credentials = service_account.Credentials.from_service_account_file(
            service_account__file)
        self.__client__ = texttospeech.TextToSpeechClient(credentials=credentials)

    def consume(self, message: str) -> None:
        self.synthesize_text(message, "output.mp3")
        playsound.playsound("output.mp3")

    def synthesize_text(self, text: str, output_location: str) -> None:
        """Synthesizes speech from the input string of text."""

        input_text = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="de-DE",
            name="de-DE-Wavenet-E",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = self.__client__.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config}
        )

        with open(output_location, "wb") as out:
            out.write(response.audio_content)
            print('Audio content written to file "output.mp3"')
