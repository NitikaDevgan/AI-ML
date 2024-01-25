from django.shortcuts import render, redirect, get_object_or_404
from .forms import SpeechFileForm
from .models import SpeechFile
from .emotion_recognition import predict_emotion



def upload_file(request):
    if request.method == 'POST':
        form = SpeechFileForm(request.POST, request.FILES)
        if form.is_valid():
            speech_file = form.save()
            # Call your emotion recognition function here and assign the recognized emotion
            file_path = speech_file.file.path
            print(file_path)
            speech_file.emotion = predict_emotion(file_path)
            speech_file.save()
            return redirect('emotion_detail', pk=speech_file.pk)
    else:
        form = SpeechFileForm()
    
    return render(request, 'upload.html', {'form': form})

def emotion_detail(request, pk):
    speech_file = get_object_or_404(SpeechFile, pk=pk)
    return render(request, 'emotion_detail.html', {'speech_file': speech_file})
