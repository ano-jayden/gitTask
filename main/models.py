
from django.db import models
"""
    Model representing a skill.

    Fields:
        title (CharField): The title of the skill.
        description (TextField): A brief description of the skill.
    """
class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

