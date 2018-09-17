from django.shortcuts import render, redirect

from MainApp.forms import StudLoginForm
from MainApp.models import Schedule


def login(request):
    form = StudLoginForm()
    return render(request, 'student_login.html', {'form': form})


def show_schedule(request):
    if request.method == "POST":
        form = StudLoginForm(request.POST)
        print(form.errors, form.non_field_errors)
        if form.is_valid():
            #vtu_id = form.get_vtu()
            schedule = Schedule.objects.filter(vtu_id=45)
            for keys, values in form.cleaned_data.items():
                print(keys)
                print(values)
            return render(request, 'view.html', {'schedule': schedule})
        else:
            return redirect('/login/')
    else:
        return redirect('/login/')
