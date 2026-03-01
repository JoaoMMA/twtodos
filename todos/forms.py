from django import forms
from .models import Todo
from django.utils import timezone


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "deadline"]
        widgets = {
            "deadline": forms.DateInput(
                attrs={"type": "date", "min": timezone.now().date().isoformat()}
            )
        }
        labels = {"title": "Titulo", "deadline": "Data de vencimento"}
