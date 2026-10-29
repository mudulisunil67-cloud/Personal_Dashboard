from django import forms
from .models import Project
from .models import Certificate


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title","description",
            "technologies",
            "code_link",
            "demo_link",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "e.g. Weather app"
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "What it does",
                "rows": 3,
            }),
            "technologies": forms.TextInput(attrs={
                "placeholder": "Django, Bootstrap, SQLite"
            }),
            "code_link": forms.URLInput(attrs={
                "placeholder": "https://github.com/..."
            }),
            "demo_link": forms.URLInput(attrs={
                "placeholder": "https://..."
            }),
        }

class CertificateForm(forms.ModelForm):

    class Meta:
        model = Certificate

        fields = [
            "name",
            "issuing_organization",
            "issue_date",
            "credential_id",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "e.g. Python Basic Certificate"
            }),

            "issuing_organization": forms.TextInput(attrs={
                "placeholder": "e.g. HackerRank"
            }),

            "issue_date": forms.DateInput(attrs={
                "type": "date"
            }),

            "credential_id": forms.TextInput(attrs={
                "placeholder": "Enter credential ID (optional)"
            }),
        }
