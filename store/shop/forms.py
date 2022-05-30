from django import forms

from .models import Reviews

class ReviewForm(forms.ModelForm):
    """Reviews form"""
    class Meta:
        model = Reviews
        fields = ("name", "text", "email")


class SortForm(forms.ModelForm):
    sort_form = forms.TypedChoiceField(choices=[('a-z', 'By alphabet'),
                                                ('price_lth', 'From low to high price'),
                                                ('price_htl', 'From high to low price')
                                                ])


