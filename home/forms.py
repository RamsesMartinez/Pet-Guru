from django import forms
from .models import Question


class Login(forms.Form):
    username = forms.CharField(max_length=20)
password = forms.CharField(max_length=20, widget = forms.PasswordInput())


class VacaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
      super(VacaForm, self).__init__(*args, **kwargs)
      self.fields['especie'].widget.attrs.update({'class':'form-control'})
      self.fields['pregunta'].widget.attrs.update({'class':'form-control'})
      self.fields['informacion'].widget.attrs.update({'class':'form-control'})
      self.fields['edad'].widget.attrs.update({'class':'form-control'})
      self.fields['peso'].widget.attrs.update({'class':'form-control'})
      self.fields['sexo'].widget.attrs.update({'class':'form-control'})
      self.fields['fisiologico'].widget.attrs.update({'class':'form-control'})
      self.fields['motivo'].widget.attrs.update({'class':'form-control'})
      self.fields['cardiaco'].widget.attrs.update({'class':'form-control'})
      self.fields['respiratorio'].widget.attrs.update({'class':'form-control'})
      self.fields['temperatura'].widget.attrs.update({'class':'form-control'})
      self.fields['llenado'].widget.attrs.update({'class':'form-control'})
      self.fields['mucosas'].widget.attrs.update({'class':'form-control'})
      self.fields['linfonodos'].widget.attrs.update({'class':'form-control'})
      self.fields['clinica'].widget.attrs.update({'class':'form-control'})
      self.fields['image'].widget.attrs.update({'class':'form-control'})
      
    class Meta:
        model = Question
        
        fields = (
          'especie',
          'pregunta',
          'informacion',
          'edad',
          'peso',
          'sexo',
          'fisiologico',
          'motivo',
          'cardiaco',
          'respiratorio',
          'temperatura',
          'llenado',
          'mucosas',
          'linfonodos',
          'clinica',
          'image',
          )

