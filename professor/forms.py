from django import forms
from disciplina.models import Disciplina
from professor.models import ProfDisc_Curso, Professor_Disc

class ProfForm(forms.Form):
    profName = forms.CharField(max_length=100)
    profEmail = forms.CharField(max_length=123)
    # profDisc = forms.ModelMultipleChoiceField(
    #     queryset=Disciplina.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )

class ProfDiscForm(forms.Form):
    profDisc = forms.ModelMultipleChoiceField(queryset=Disciplina.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

#class plan_descForm(forms.Form):

#class Plan_DescForm(forms.Form):