from faster_whisper import WhisperModel

model = WhisperModel("tiny", device="cpu", compute_type="int8")


def transcribe(audio_array):

    segments, _ = model.transcribe(
        audio_array,
        beam_size=1
    )

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()