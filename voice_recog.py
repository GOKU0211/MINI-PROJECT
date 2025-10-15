import torch
import soundfile as sf
from speechbrain.inference import EncoderClassifier
import sounddevice as sd
from scipy.io.wavfile import write

recognizer = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb")

# Record short temporary audio for verification
def record_temp(filename="temp_audio.wav", duration=3, fs=16000):
    print(" Recording temporary voice sample...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print(" Temporary recording saved:", filename)
    return filename

def get_embedding(audio_path):
    signal, fs = sf.read(audio_path)
    signal = torch.tensor(signal).unsqueeze(0)
    return recognizer.encode_batch(signal)

def enroll_user(audio_path, user_name="owner"):
    embedding = get_embedding(audio_path)
    torch.save(embedding, f"{user_name}_voice.pt")
    print(f" Voice model saved for {user_name}")

def verify_user(audio_path, user_name="owner"):
    stored = torch.load(f"{user_name}_voice.pt")
    test = get_embedding(audio_path)
    # cosine similarity
    cos = torch.nn.functional.cosine_similarity(stored, test, dim=-1).mean().item()
    print(f"[DEBUG] Cosine similarity score: {cos:.4f}")
    print("Similarity:", cos)
    return cos, cos > 0.75  # threshold tweakable
