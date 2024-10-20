from django import forms
from .models import Skill
"""
    Form for adding a new skill.

    Meta:
        model: The model linked to the form.
        fields: The fields to include in the form.
    """
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title', 'description']
