from django import forms
from .models import Question, Bovine


class Login(forms.Form):
  usuario = forms.CharField(max_length=20)
  contraseña = forms.CharField(max_length=20, widget = forms.PasswordInput())


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
      super(BaseForm, self).__init__(*args, **kwargs)
      self.fields['title'].widget.attrs.update({'class':'form-control'})
      self.fields['description'].widget.attrs.update({'class':'form-control'})
   
    class Meta:
        model = Question

        fields = (
          'title',
          'description',
          )
        
        labels = {
          'title': 'Título de la consulta: ',
          'description': 'Descripción de la consulta: ',
          }



class VacaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
      super(VacaForm, self).__init__(*args, **kwargs)
      self.fields['specie'].widget.attrs.update({'class':'form-control'})
      self.fields['race'].widget.attrs.update({'class':'form-control'})
      self.fields['age'].widget.attrs.update({'class':'form-control'})
      self.fields['gender'].widget.attrs.update({'class':'form-control'})
      self.fields['weight'].widget.attrs.update({'class':'form-control'})
      self.fields['heart_rate'].widget.attrs.update({'class':'form-control'})
      self.fields['respiratory_rate'].widget.attrs.update({'class':'form-control'})
      self.fields['temperature'].widget.attrs.update({'class':'form-control'})
      self.fields['capilar'].widget.attrs.update({'class':'form-control'})
      self.fields['mucosal_color'].widget.attrs.update({'class':'form-control'})
      self.fields['lymph_nodes'].widget.attrs.update({'class':'form-control'})
      self.fields['ruminal'].widget.attrs.update({'class':'form-control'})
      self.fields['body_condition'].widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Bovine
        
        fields = (
          'specie',
          'race',
          'age',
          'gender',
          'weight',
          'heart_rate',
          'respiratory_rate',
          'temperature',
          'capilar',
          'mucosal_color',
          'lymph_nodes',
          'ruminal',
          'body_condition',
          )

        labels = {
          'specie': 'Especie: ',
          'race': 'Raza: ',
          'age': 'Edad: ',
          'gender': 'Género: ',
          'weight': 'Peso: ',
          'heart_rate': 'Frecuencia cardiaca (lpm): ',
          'respiratory_rate': 'Frecuencia respiratoria (rpm): ',
          'temperature': 'Temperatura (°C): ',
          'capilar': 'Llenado capilar (segundos): ',
          'mucosal_color': 'Color de mucosas: ',
          'lymph_nodes': 'Linfonodos: ',
          'ruminal': 'Movimientos ruminales: ',
          'body_condition': 'Condición corporal: ',
          }