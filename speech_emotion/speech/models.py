from django.db import models

class SpeechFile(models.Model):
    file = models.FileField(upload_to='speech_files')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    emotion = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.file.name