from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'date_start', 'date_end', 'color']  # Changed 'description' to 'content'
        widgets = {
            'date_start': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_end': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})  # Assuming you want a textarea for the content
        }
