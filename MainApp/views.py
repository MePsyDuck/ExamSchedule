from django.shortcuts import render, redirect

from MainApp.forms import StudLoginForm
from MainApp.models import Schedule


def login(request):
    form = StudLoginForm()
    return render(request, 'login.html', {'form': form})


def show_schedule(request):
    if request.method == "POST":
        form = StudLoginForm(request.POST)
        if form.is_valid():
            user_id = form.get_id()
            if user_id[:3].upper() == 'VTU':
                schedule = Schedule.objects.filter(vtu_id=user_id)
                return render(request, 'view_vtu.html', {'schedule': schedule, 'vtu_id': user_id})
            else:
                schedule = Schedule.objects.filter(tts_id=user_id).values('room_id', 'sub_id', 'session',
                                                                          'date').distinct()
                return render(request, 'view_tts.html', {'schedule': schedule, 'tts_id': user_id})
        else:
            return redirect('/login/')
    else:
        return redirect('/login/')
