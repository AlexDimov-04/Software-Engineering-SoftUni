from django import forms
from exam_prep_2.web.models import Profile, Plant

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']

class ProfileEditForm(ProfileForm):
    pass

class ProfileDeleteForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Plant.objects.all().delete()
            Profile.objects.all().delete()
        return self.instance

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'

class PlantDeleteForm(PlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()
    
    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
    
class PlantEditForm(PlantForm):
    pass