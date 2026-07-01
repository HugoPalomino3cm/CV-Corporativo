import os, json
import whisper, imageio_ffmpeg as ffmpeg

# copia el binario ffmpeg para que Whisper lo encuentre
ffexe = ffmpeg.get_ffmpeg_exe()
dst = os.path.join(os.getcwd(), 'ffmpeg.exe')
import shutil
shutil.copy(ffexe, dst)
os.environ['PATH'] = os.getcwd() + os.pathsep + os.environ.get('PATH','')

model = whisper.load_model("tiny")
files = [f for f in os.listdir('.') if f.lower().endswith('.ogg')]
out = {}
for f in files:
    r = model.transcribe(f, language='es', fp16=False)
    out[f] = r.get('text','').strip()

with open('transcriptions.json','w', encoding='utf-8') as h:
    json.dump(out, h, ensure_ascii=False, indent=2)

print('Transcripciones guardadas en transcriptions.json')