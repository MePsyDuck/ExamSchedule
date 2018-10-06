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

    def debug(self):
        if self.is_valid():
            print(str(self.cleaned_data))
        else:
            print(self.non_field_errors())

    def process_ids(self):
        id_list = []
        if self.is_valid():
            mixed_ids = self.cleaned_data.get('vtu_ids').replace(' ', '')
            id_tokens = mixed_ids.split(',')
            for token in id_tokens:
                if '-' in token:
                    start, end = token.split('-', 1)
                    if valid_vtu(start) and valid_vtu(end):
                        for id in range(int(start[3:]), int(end[3:]) + 1):
                            id_list.append('VTU' + str(id))
                    else:
                        print('Invalid id range: ', token)
                else:
                    if valid_vtu(token):
                        id_list.append(token.upper())
                    else:
                        print('Invalid id range: ', token)
        return id_list


def valid_vtu(vtu_id):
    return vtu_id[:3].upper() == 'VTU' and vtu_id[3:].isnumeric()
