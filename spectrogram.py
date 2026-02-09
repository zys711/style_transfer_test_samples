import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np

def generate_spectrogram(audio_file_path, save_path):
    # Load the audio file
    
    y, sr = librosa.load(audio_file_path)

    # Generate a spectrogram
    plt.figure(figsize=(3, 2),layout='tight')
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=256, fmax=12000)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max),
                             y_axis='mel', fmax=12000, x_axis='time')
    
    
    # D = librosa.stft(y, n_fft=1024)

    # # Convert to a spectrogram
    # spect = np.abs(D)

    # # Display the spectrogram
    
    # librosa.display.specshow(librosa.amplitude_to_db(spect, ref=np.max),
    #                          y_axis='log', x_axis='time')
    # Save the figure as a PNG file
    plt.savefig(save_path)
    


import os

if __name__ == '__main__':
    audio_dir = 'audios'
    spectrogram_dir = 'spectrograms'

    # Iterate over all files in the audio directory
    for root, dirs, files in os.walk(audio_dir):
        for file in files:
            if file.endswith('.wav'):
                audio_file_path = os.path.join(root, file)
                # Create a corresponding spectrogram file path
                relative_path = os.path.relpath(root, audio_dir)
                spectrogram_subdir = os.path.join(spectrogram_dir, relative_path)
                os.makedirs(spectrogram_subdir, exist_ok=True)
                spectrogram_file_path = os.path.join(spectrogram_subdir, file.replace('.wav', '.png'))
                generate_spectrogram(audio_file_path, spectrogram_file_path)