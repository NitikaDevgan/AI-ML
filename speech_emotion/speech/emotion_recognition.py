import librosa
import numpy as np
from joblib import load
from sklearn.preprocessing import LabelEncoder
from pathlib import Path

# Load the saved model
model_file = Path(__file__).resolve().parent.parent / 'speech_models/emotion_classifier_model.joblib'
model = load(model_file)

# Define the emotions and corresponding labels in RAVDESS dataset
emotions = {
    '0': 'neutral',
    '1': 'calm',
    '2': 'happy',
    '3': 'sad',
    '4': 'angry',
    '5': 'fearful',
    '6': 'disgust',
    '7': 'surprised'
}

# Function to extract audio features using librosa
def extract_features(file_path):
    try:
        audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccs_processed = np.mean(mfccs.T, axis=0)
        return mfccs_processed
    except Exception as e:
        print("Error encountered while parsing file: ", file_path)
        print(f"Error Message : {str(e)}")
        return None

# Function to predict emotion from audio
def predict_emotion(audio_path):
    # Extract features from the audio
    print(audio_path)
    features = extract_features(audio_path)
    if features is not None:
        # Reshape features array to match the input shape of the model
        features = features.reshape(1, -1)
        # Make prediction using the loaded model
        predicted_label = model.predict(features)[0]
        # Convert numerical label to emotion
        print("PREDICTED LABLE-----------------------------------------\n\n\n\n\n\n\n\n\n",predicted_label)
        predicted_emotion = emotions[str(predicted_label)]
        return predicted_emotion
    else:
        print("\n\n\n\n\n\nerror in prediction\n\n\n\n\n\n\n\n")
        return None
