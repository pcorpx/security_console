from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    # Получение всех визитов для выбранного пропуска
    this_passcard_visits =Visit.objects.filter(passcard=passcard)
    for visit in this_passcard_visits:
        duration = visit.get_duration()
        visit.duration = Visit.format_duration(duration)
        visit.who_entered = visit.passcard
        visit.is_strange = visit.is_visit_long()
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
