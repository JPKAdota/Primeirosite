from django import forms

class InscreverForm(forms.Form):
    nome = forms.CharField(label='Nome')
    telefone = forms.CharField(label='Telefone')
    data = forms.DateTimeField(label='Data da reserva')
    observacao = forms.CharField(label='Observação', widget=forms.Textarea)
    