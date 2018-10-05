from django import forms


class StudLoginForm(forms.Form):
    user_id = forms.CharField()

    # TODO maybe add password validation in future
    # password = forms.CharField(widget=forms.PasswordInput())

    def get_id(self):
        if self.is_valid():
            return self.cleaned_data.get('user_id')
        else:
            print(self.non_field_errors())


class AddNewSchedule(forms.Form):
    date = forms.DateField()
    session = forms.ChoiceField(choices=[('AN', 'AN'), ('FN', 'FN')])
    room_id = forms.CharField()
    sub_id = forms.CharField()
    tts_id = forms.CharField()
    vtu_ids = forms.CharField()

    def process_ids(self):
        if self.is_valid():
            print(str(self.cleaned_data))
        else:
            print(self.non_field_errors())
