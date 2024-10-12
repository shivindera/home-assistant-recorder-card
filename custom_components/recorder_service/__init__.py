import requests

DOMAIN = "recorder_service"

WAV_ATTR_NAME = "wav"
URL_ATTR_NAME = "target"

def setup(hass, config):
    def handle_recorder(call):
        wav = call.data.get(WAV_ATTR_NAME, '')
        target = call.data.get(URL_ATTR_NAME, '')

        # Convert the list of integers to bytes
        wav_bytes = bytes(wav)

        # Write the bytes to a file
        with open(target, "wb") as f:
            f.write(wav_bytes)

    hass.services.register(DOMAIN, "process", handle_recorder)

    return True
