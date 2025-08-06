import os
import string
import random
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def generate_unique_course_code():
    chars = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(random.choices(chars, k=6))
        if not Course.objects.filter(code=code).exists():
            return code
        
        
class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True, editable=False) 
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_course_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.code}"


class Document(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='documents/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.title or self.file.name
    
    def clean(self):
        if self.file:
            if not self.file.name.endswith('.pdf'):
                raise ValidationError('Only PDF files are allowed.')
            if self.file.file.content_type != 'application/pdf':
                raise ValidationError('File content must be a PDF.')
            
    def save(self, *args, **kwargs):
        if not self.title and self.file:
            self.title = os.path.splitext(os.path.basename(self.file.name))[0]
        super().save(*args, **kwargs)


class DocumentChunk(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='chunks')
    chunk_id = models.CharField(max_length=100)
    text = models.TextField()
    embedding = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return f"Chunk {self.chunk_id} of {self.document.title}"
