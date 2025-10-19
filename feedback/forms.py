from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Текст отзыва (до 1000 символов)'}),
        }

    def clean_message(self):
        msg = self.cleaned_data['message']
        if 'http://' in msg or 'https://' in msg:
            raise forms.ValidationError('Пожалуйста, не вставляйте ссылки в отзыве.')
        return msg
