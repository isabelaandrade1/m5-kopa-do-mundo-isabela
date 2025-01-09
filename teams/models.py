from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=30, null=False)
    titles = models.PositiveIntegerField(default=0, null=True, blank=True)  # Usar PositiveIntegerField para garantir valores positivos
    top_scorer = models.CharField(max_length=50, null=False)
    fifa_code = models.CharField(max_length=3, unique=True, null=False)
    first_cup = models.DateField(null=True, blank=True)

    def __repr__(self):
        return f"<Team [{self.id}] {self.name} - {self.fifa_code}>"

    def __str__(self):
        return f"{self.name} ({self.fifa_code})"
