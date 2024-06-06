from .models import Review
from django import forms
from django.forms import ModelForm, TextInput,IntegerField, Textarea,NumberInput
from captcha.fields import CaptchaField
class ReviewForm(ModelForm):
    captcha = CaptchaField(label='Введите капчу')
    class Meta:
        model = Review
        fields = ['title','text','estimation']

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Вaше имя:"
            }),
            "text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Ваш отзыв:"
            }),
            "estimation": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Оценка(1-5):"
            })

        }
