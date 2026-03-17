from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu", compute_type="int8")


def transcribe(audio_array):

    segments, _ = model.transcribe(
        audio_array,
        beam_size=1, 
        language="en"
    )

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()


