from django import forms

class InscreverForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.CharField(label='E-mail')
    observacao = forms.CharField(label='Observação', widget=forms.Textarea)
    