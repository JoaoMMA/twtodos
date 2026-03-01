from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User


def validar_data_futura(value):
    if value < timezone.now().date():
        raise ValidationError("A data não pode ser no passado!")


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(
        null=False, blank=False, validators=[validar_data_futura]
    )
    finish_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadline", "created_at"]

    def mark_as_complete(self):
        if not self.finish_at:
            self.finish_at = timezone.now().date()
            self.save()
