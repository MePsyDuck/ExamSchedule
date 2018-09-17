from django import forms

from MainApp.models import Schedule


class StudLoginForm(forms.Form):
    user = forms.CharField(max_length=100)

    class Meta:
        model = Schedule
        fields = ('vtu_id',)

    # TODO maybe add password validation in future
    # password = forms.CharField(widget=forms.PasswordInput())

    def get_vtu(self):
        if self.is_valid():
            return self.cleaned_data['vtu_id']
