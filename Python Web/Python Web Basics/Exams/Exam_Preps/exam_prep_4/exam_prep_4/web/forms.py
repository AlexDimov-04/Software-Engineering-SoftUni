from django import forms
from exam_prep_4.web.models import Profile, Game


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']

class ProfileCreateForm(ProfileBaseForm):
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password', 'first_name', 'last_name', 'profile_picture']

class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Game.objects.all().delete()
            Profile.objects.all().delete()
        return self.instance

class GameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

class GameCreateForm(GameBaseForm):
    pass

class GameEditForm(GameBaseForm):
    pass

class GameDeleteForm(GameBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance