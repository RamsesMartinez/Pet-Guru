from django import forms
from .models import Question, Bovine, Porcine, Horse, Goat, Ovine, Rabbit


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



class CowForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
      super(CowForm, self).__init__(*args, **kwargs)
      self.fields['specie'].widget.attrs.update({'class':'form-control','id':'cowspecie'})
      self.fields['race'].widget.attrs.update({'class':'form-control','id':'cowrace'})
      self.fields['age'].widget.attrs.update({'class':'form-control','id':'cowage'})
      self.fields['gender'].widget.attrs.update({'class':'form-control','id':'cowgender'})
      self.fields['weight'].widget.attrs.update({'class':'form-control','id':'cowweight'})
      self.fields['heart_rate'].widget.attrs.update({'class':'form-control','id':'cowheart'})
      self.fields['respiratory_rate'].widget.attrs.update({'class':'form-control','id':'cowresp'})
      self.fields['temperature'].widget.attrs.update({'class':'form-control','id':'cowtemp'})
      self.fields['capilar'].widget.attrs.update({'class':'form-control','id':'cowcapilar'})
      self.fields['mucosal_color'].widget.attrs.update({'class':'form-control','id':'cowmucosal'})
      self.fields['lymph_nodes'].widget.attrs.update({'class':'form-control','id':'cowlymph'})
      self.fields['ruminal'].widget.attrs.update({'class':'form-control','id':'cowruminal'})
      self.fields['body_condition'].widget.attrs.update({'class':'form-control','id':'cowcondition'})
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


class PorcineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
      super(PorcineForm, self).__init__(*args, **kwargs)
      self.fields['specie'].widget.attrs.update({'class':'form-control', 'id':'porspecie'})
      self.fields['physiological_stage'].widget.attrs.update({'class':'form-control', 'id':'porphysio'})
      self.fields['race'].widget.attrs.update({'class':'form-control', 'id':'porrace'})
      self.fields['age'].widget.attrs.update({'class':'form-control', 'id':'porage'})
      self.fields['gender'].widget.attrs.update({'class':'form-control', 'id':'porgender'})
      self.fields['weight'].widget.attrs.update({'class':'form-control', 'id':'porweight'})
      self.fields['heart_rate'].widget.attrs.update({'class':'form-control', 'id':'porheart'})
      self.fields['respiratory_rate'].widget.attrs.update({'class':'form-control', 'id':'porresp'})
      self.fields['temperature'].widget.attrs.update({'class':'form-control', 'id':'portemp'})
      self.fields['production_system'].widget.attrs.update({'class':'form-control', 'id':'porprod'})
      self.fields['curse'].widget.attrs.update({'class':'form-control', 'id':'porcurse'})
      self.fields['attitude'].widget.attrs.update({'class':'form-control', 'id':'poratt'})
      self.fields['color'].widget.attrs.update({'class':'form-control', 'id':'porcolor'})
      self.fields['body_condition'].widget.attrs.update({'class':'form-control', 'id':'porcondition'})
    class Meta:
        model = Porcine       
        fields = (
          'specie',
          'physiological_stage',
          'race',
          'age',
          'gender',
          'weight',
          'heart_rate',
          'respiratory_rate',
          'temperature',
          'production_system',
          'curse',
          'attitude',
          'color',
          'body_condition',
          )
        labels = {
          'specie': 'Especie: ',
          'physiological_stage': 'Etapa fisiológica: ',
          'race': 'Raza: ',
          'age': 'Edad: ',
          'gender': 'Género: ',
          'weight': 'Peso: ',
          'heart_rate': 'Frecuencia cardiaca (lpm): ',
          'respiratory_rate': 'Frecuencia respiratoria (rpm): ',
          'temperature': 'Temperatura (°C): ',
          'production_system': 'Sistema de producción: ',
          'curse': 'Curso del padecimiento en días: ',
          'attitude': 'Actitud: ',
          'color': 'Coloración de la piel y/o mucosas: ',
          'body_condition': 'Condición corporal: ',
          }


class HorseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
      super(HorseForm, self).__init__(*args, **kwargs)
      self.fields['specie'].widget.attrs.update({'class':'form-control', 'id':'horspecie'})
      self.fields['race'].widget.attrs.update({'class':'form-control', 'id':'horrace'})
      self.fields['age'].widget.attrs.update({'class':'form-control', 'id':'horage'})
      self.fields['gender'].widget.attrs.update({'class':'form-control', 'id':'horgender'})
      self.fields['weight'].widget.attrs.update({'class':'form-control', 'id':'horweight'})
      self.fields['heart_rate'].widget.attrs.update({'class':'form-control', 'id':'horheart'})
      self.fields['respiratory_rate'].widget.attrs.update({'class':'form-control', 'id':'horresp'})
      self.fields['temperature'].widget.attrs.update({'class':'form-control', 'id':'hortemp'})
      self.fields['capilar'].widget.attrs.update({'class':'form-control', 'id':'horcapilar'})
      self.fields['mucosal_color'].widget.attrs.update({'class':'form-control', 'id':'hormucosal'})
      self.fields['lymph_nodes'].widget.attrs.update({'class':'form-control', 'id':'horlymph'})
      self.fields['body_condition'].widget.attrs.update({'class':'form-control', 'id':'horcondition'})
    class Meta:
        model = Horse       
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
          'body_condition': 'Condición corporal: ',
          }


class GoatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
      super(GoatForm, self).__init__(*args, **kwargs)
      self.fields['specie'].widget.attrs.update({'class':'form-control','id':'goatspecie'})
      self.fields['physiological_stage'].widget.attrs.update({'class':'form-control','id':'goatphysio'})
      self.fields['race'].widget.attrs.update({'class':'form-control','id':'goatrace'})
      self.fields['age'].widget.attrs.update({'class':'form-control','id':'goatage'})
      self.fields['gender'].widget.attrs.update({'class':'form-control','id':'goatgender'})
      self.fields['ruminal'].widget.attrs.update({'class':'form-control','id':'goatruminal'})
      self.fields['weight'].widget.attrs.update({'class':'form-control','id':'goatweight'})
      self.fields['heart_rate'].widget.attrs.update({'class':'form-control','id':'goatheart'})
      self.fields['respiratory_rate'].widget.attrs.update({'class':'form-control','id':'goatresp'})
      self.fields['temperature'].widget.attrs.update({'class':'form-control','id':'goattemp'})
      self.fields['production_system'].widget.attrs.update({'class':'form-control','id':'goatprod'})
      self.fields['zootechnical'].widget.attrs.update({'class':'form-control','id':'goatzoo'})
      self.fields['lymph_nodes'].widget.attrs.update({'class':'form-control','id':'goatlymph'})
      self.fields['capilar'].widget.attrs.update({'class':'form-control','id':'goatcapilar'})
      self.fields['cough'].widget.attrs.update({'class':'form-control','id':'goatcough'})
      self.fields['mucosal_color'].widget.attrs.update({'class':'form-control','id':'goatmucos'})
      self.fields['body_condition'].widget.attrs.update({'class':'form-control','id':'goatcondition'})
    class Meta:
        model = Goat       
        fields = (
          'specie',
          'physiological_stage',
          'race',
          'age',
          'gender',
          'ruminal',
          'capilar',
          'cough',
          'weight',
          'heart_rate',
          'respiratory_rate',
          'temperature',
          'production_system',
          'zootechnical',
          'lymph_nodes',
          'mucosal_color',
          'body_condition',
          )
        labels = {
          'specie': 'Especie: ',
          'physiological_stage': 'Etapa fisiológica: ',
          'race': 'Raza: ',
          'age': 'Edad: ',
          'capilar': 'Tiempo de llenado capilar: ',
          'cough': 'Relfejo tusígeno: ',
          'gender': 'Género: ',
          'ruminal': 'Movimientos ruminales: ',
          'weight': 'Peso: ',
          'heart_rate': 'Frecuencia cardiaca (lpm): ',
          'respiratory_rate': 'Frecuencia respiratoria (rpm): ',
          'temperature': 'Temperatura (°C): ',
          'production_system': 'Sistema de producción: ',
          'zootechnical': 'Fin zootécnico: ',
          'lymph_nodes': 'Linfonodos: ',
          'mucosal_color': 'Coloración de mucosas: ',
          'body_condition': 'Condición corporal: ',
          }


class OvineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
      super(OvineForm, self).__init__(*args, **kwargs)
      self.fields['specie'].widget.attrs.update({'class':'form-control', 'id':'ovispecie'})
      self.fields['physiological_stage'].widget.attrs.update({'class':'form-control', 'id':'oviphysio'})
      self.fields['race'].widget.attrs.update({'class':'form-control', 'id':'ovirace'})
      self.fields['age'].widget.attrs.update({'class':'form-control', 'id':'oviage'})
      self.fields['gender'].widget.attrs.update({'class':'form-control', 'id':'ovigender'})
      self.fields['weight'].widget.attrs.update({'class':'form-control', 'id':'oviweight'})
      self.fields['heart_rate'].widget.attrs.update({'class':'form-control', 'id':'oviheart'})
      self.fields['respiratory_rate'].widget.attrs.update({'class':'form-control', 'id':'oviresp'})
      self.fields['temperature'].widget.attrs.update({'class':'form-control', 'id':'ovitemp'})
      self.fields['production_system'].widget.attrs.update({'class':'form-control', 'id':'oviprod'})
      self.fields['zootechnical'].widget.attrs.update({'class':'form-control', 'id':'ovizoo'})
      self.fields['ruminal'].widget.attrs.update({'class':'form-control', 'id':'oviruminal'})
      self.fields['lymph_nodes'].widget.attrs.update({'class':'form-control', 'id':'ovilymph'})
      self.fields['mucosal_color'].widget.attrs.update({'class':'form-control', 'id':'ovimucos'})
      self.fields['body_condition'].widget.attrs.update({'class':'form-control', 'id':'ovicondition'})
    class Meta:
        model = Ovine       
        fields = (
          'specie',
          'physiological_stage',
          'race',
          'age',
          'gender',
          'ruminal',
          'weight',
          'heart_rate',
          'respiratory_rate',
          'temperature',
          'production_system',
          'zootechnical',
          'lymph_nodes',
          'mucosal_color',
          'body_condition',
          )
        labels = {
          'specie': 'Especie: ',
          'physiological_stage': 'Etapa fisiológica: ',
          'race': 'Raza: ',
          'age': 'Edad: ',
          'gender': 'Género: ',
          'ruminal': 'Movimientos ruminales: ',
          'weight': 'Peso: ',
          'heart_rate': 'Frecuencia cardiaca (lpm): ',
          'respiratory_rate': 'Frecuencia respiratoria (rpm): ',
          'temperature': 'Temperatura (°C): ',
          'production_system': 'Sistema de producción: ',
          'zootechnical': 'Fin zootécnico: ',
          'lymph_nodes': 'Linfonodos: ',
          'mucosal_color': 'Coloración de mucosas: ',
          'body_condition': 'Condición corporal: ',
          }


class RabbitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
      super(RabbitForm, self).__init__(*args, **kwargs)
      self.fields['specie'].widget.attrs.update({'class':'form-control', 'id':'rabspecie'})
      self.fields['productive_stage'].widget.attrs.update({'class':'form-control', 'id':'rabprod'})
      self.fields['race'].widget.attrs.update({'class':'form-control', 'id':'rabrace'})
      self.fields['age'].widget.attrs.update({'class':'form-control', 'id':'rabage'})
      self.fields['gender'].widget.attrs.update({'class':'form-control', 'id':'rabgender'})
      self.fields['weight'].widget.attrs.update({'class':'form-control', 'id':'rabweight'})
      self.fields['heart_rate'].widget.attrs.update({'class':'form-control', 'id':'rabheart'})
      self.fields['respiratory_rate'].widget.attrs.update({'class':'form-control', 'id':'rabresp'})
      self.fields['temperature'].widget.attrs.update({'class':'form-control', 'id':'rabtemp'})
      self.fields['capilar'].widget.attrs.update({'class':'form-control', 'id':'rabcapilar'})
      self.fields['dehydration'].widget.attrs.update({'class':'form-control', 'id':'rabdehy'})
      self.fields['lymph_nodes'].widget.attrs.update({'class':'form-control', 'id':'rablymph'})
      self.fields['mucosal_color'].widget.attrs.update({'class':'form-control', 'id':'rabmucos'})
      self.fields['body_condition'].widget.attrs.update({'class':'form-control', 'id':'rabcondition'})
    class Meta:
        model = Rabbit       
        fields = (
          'specie',
          'productive_stage',
          'race',
          'age',
          'gender',
          'weight',
          'heart_rate',
          'respiratory_rate',
          'temperature',
          'capilar',
          'dehydration',
          'lymph_nodes',
          'mucosal_color',
          'body_condition',
          )
        labels = {
          'specie': 'Especie: ',
          'productive_stage': 'Etapa productiva: ',
          'race': 'Raza: ',
          'age': 'Edad: ',
          'gender': 'Género: ',
          'weight': 'Peso: ',
          'heart_rate': 'Frecuencia cardiaca (lpm): ',
          'respiratory_rate': 'Frecuencia respiratoria (rpm): ',
          'temperature': 'Temperatura (°C): ',
          'capilar': 'Tiempo de llenado capilar: ',
          'dehydration': 'Deshidratación: ',
          'lymph_nodes': 'Ganglios linfáticos: ',
          'mucosal_color': 'Coloración de mucosas: ',
          'body_condition': 'Condición corporal: ',
          }