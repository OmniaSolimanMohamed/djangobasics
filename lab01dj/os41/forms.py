from django import forms
from django.forms import widgets
from os41.models import Student,Track

class studentForm (forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fname','lname','age','student_track')
        widgets = {
            'fname' : forms.TextInput(attrs={'class': 'form-control'}),
            'lname' : forms.TextInput(attrs={'class': 'form-control'}),
            'age' : forms.NumberInput(attrs={'class': 'form-control'}),
            'student_track' : forms.Select(attrs={'class': 'form-control'}),
        }
class TrackForm (forms.ModelForm):
    class Meta:
        model = Track
        fields = ('name',) # 3mlt comma zyada 3lshn awd7 en da tupel
