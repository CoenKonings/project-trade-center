from django.core.exceptions import ValidationError
from django import forms
from . import models


class ProposalForm(forms.Form):
    from_project = forms.ModelChoiceField(queryset=models.Project.objects.all(), label="Ik ben ingedeeld bij:")
    to_project = forms.ModelChoiceField(queryset=models.Project.objects.all(), label="Ik wil:")
    name = forms.CharField(min_length=3, max_length=127, label="Naam (zodat je gevonden kan worden bij een match)")

    def clean(self):
        from_project = self.cleaned_data["from_project"]
        to_project = self.cleaned_data["to_project"]
        name = self.cleaned_data["name"]


        if from_project and to_project:
            if from_project == to_project:
                raise ValidationError("From project and to project should be different.")

        if name and models.SwitchProposal.objects.filter(name=name).exists():
                raise ValidationError("You already proposed a switch - check the list at the bottom.")
