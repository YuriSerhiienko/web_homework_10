from django import forms
from .models import Author, Quote


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]


class QuoteForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    new_tags = forms.CharField(
        label="New Tags (comma-separated)",
        required=False,
        help_text="Enter new tags separated by commas",
    )

    class Meta:
        model = Quote
        fields = ["author", "new_tags", "text"]
