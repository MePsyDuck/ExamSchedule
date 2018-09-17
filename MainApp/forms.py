from django import forms

from MainApp.models import Schedule


class StudLoginForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ['vtu_id', ]

    # TODO maybe add password validation in future
    # password = forms.CharField(widget=forms.PasswordInput())

    def get_vtu(self):
        if self.is_valid():
            return self.cleaned_data.get('vtu_id')
        else:
            print(self.errors)
