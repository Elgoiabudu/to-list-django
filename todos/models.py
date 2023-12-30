from datetime import date

from django.db import models


class UserAPI(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    surname = models.CharField(max_length=150, null=False, blank=False)
    nickname = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    title = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Título:"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False, verbose_name="Prazo Final:")
    fineshed_at = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ("fineshed_at", "deadline")

    def mark_has_completed(self):
        if not self.fineshed_at:
            self.fineshed_at = date.today()
            self.save()

    def __str__(self):
        return self.title
