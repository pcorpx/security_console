from django.db import models
from django import utils

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)
    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    @classmethod
    def format_duration(cls, duration):
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        return f"{hours} ч. {minutes} мин."
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)
  

    def get_duration(self):
        if not self.leaved_at:
            now = utils.timezone.localtime()
            duration = now - self.entered_at
        else:
          duration = self.leaved_at - self.entered_at
        return duration.total_seconds()

    def is_visit_long(self, minutes=60):
        duration = self.get_duration() 
        visited_minutes = (duration % 3600) // 60
        return visited_minutes > minutes

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
