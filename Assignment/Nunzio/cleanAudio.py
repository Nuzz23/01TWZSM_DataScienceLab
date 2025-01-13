import noisereduce as nr
import torchaudio
from scipy.io import wavfile
import pandas as pd


df = pd.read_csv('Assignment/Nunzio/NonAfrica.csv', header=0, index_col=0)

for item in df['path']:
    wavfile.write('Assignment/data/cleanAudioDevelopment/'+item, 22050, 
                    nr.reduce_noise(y=torchaudio.load("Assignment/data/clean_silence/Audios/"+item)[0], 
                                                    sr=22050, stationary=False)[0])