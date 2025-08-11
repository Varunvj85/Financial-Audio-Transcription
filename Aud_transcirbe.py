import whisper
audio_file_path = "Mixed.m4a"
model = whisper.load_model("large")  
result = model.transcribe(audio_file_path, task="translate")
print(result["text"])