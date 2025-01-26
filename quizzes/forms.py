from django import forms
from .models import CATEGORY_CHOICES


class CategoryForm(forms.Form):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True, label='Виберіть категорію')
