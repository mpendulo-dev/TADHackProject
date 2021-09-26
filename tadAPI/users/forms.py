from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


GRADE =(
    (0, "Grade 10"),
    (1, "Grade 11"),
        (2, "Grade 12"),

)

class LearnerForm(UserCreationForm):
    firsname=forms.CharField(required=False, max_length=20)
    lastname=forms.CharField(required=False, max_length=20)
    ID=forms.IntegerField(required=True)
    Grade=forms.IntegerField(required=True)
    email=forms.EmailField(required=True)
    
    
    class Mata:
        model=User
        fields=("username", "email", "password1", "password2")

        def save(self, commit=True):
            learner = super(LearnerForm, self).save(commit=False)
            learner.email = self.cleaned_data['email']
            learner.firstname = self.cleaned_data['firstname']
            learner.lastname = self.cleaned_data['lastname']
            learner.ID = self.cleaned_data['ID']
            #learner.Grade= self.cleaned_data['Grade']
            if commit:
                learner.save()
                return learner