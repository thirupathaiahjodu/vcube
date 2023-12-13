# forms.py

from django import forms
from .models import *

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)






class studentuserfrom(forms.ModelForm):
    class Meta:
        model = Studentuser
        fields='__all__'
