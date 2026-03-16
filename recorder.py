import sounddevice as sd
import numpy as np

SAMPLERATE = 16000
CHANNELS = 1

audio_buffer = []


def start_recording_stream():
    global audio_buffer
    audio_buffer = []

    def callback(indata, frames, time_info, status):
        audio_buffer.append(indata.copy())

    stream = sd.InputStream(
        samplerate=SAMPLERATE,
        channels=CHANNELS,
        callback=callback
    )

    stream.start()

    return stream


def stop_recording_stream(stream):
    stream.stop()
    stream.close()

    if not audio_buffer:
        return None

    audio_array = np.concatenate(audio_buffer, axis=0).flatten()

    return audio_array