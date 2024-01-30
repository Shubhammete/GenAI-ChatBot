import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/YOUR_API_KEY_:)"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "YOUR_API_KEY_:)"
}

data = {
  "text": "Some very long text to be read by the voice",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0,
    "similarity_boost": 0
  }
}

response = requests.post(url, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)


<audio src="{{ url_for('static', filename='output.mp3') }}?v={{ cache_bust }}" controls></audio>