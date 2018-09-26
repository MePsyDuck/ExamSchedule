from django import forms


class StudLoginForm(forms.ModelForm):
    user_id = forms.CharField()

    # TODO maybe add password validation in future
    # password = forms.CharField(widget=forms.PasswordInput())

    def get_id(self):
        if self.is_valid():
            return self.cleaned_data.get('user_id')
        else:
            print(self.errors)
