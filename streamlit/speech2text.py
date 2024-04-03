import requests


def speech2text(api_key: str, audio_file, language, initial_prompt: str = ""):
    openai.api_key = api_key

    # prepare decode_options
    decode_options = {"language": language}

    headers = {
        'Authorization': 'Bearer TOKEN',
        # requests won't add a boundary if this header is set when you pass files=
        # 'Content-Type': 'multipart/form-data',
    }

    files = {
        'file': open('/path/to/file/german.mp3', 'rb'),
        'model': (None, 'whisper-1'),
    }

    transcript = requests.post(
        'https://api.openai.com/v1/audio/translations', headers=headers, files=files)

    return transcript["text"]
