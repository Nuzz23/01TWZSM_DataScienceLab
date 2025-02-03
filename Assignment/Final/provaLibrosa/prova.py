import noisereduce as nr
from scipy.io import wavfile
import librosa
import os
import numpy as np

for item in os.listdir('./data/audios_development/'):
    wavfile.write('./data/allCleanAudio/'+item, 22050, 
              nr.reduce_noise(y=np.array(librosa.effects.trim(
                  librosa.load('./data/audios_development/'+item, sr=22050)[0], top_db=20)[0]), 
                                                    sr=22050, stationary=False))