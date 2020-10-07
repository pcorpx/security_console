from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    # Получение всех незавершенных посещений
    non_closed_visits = Visit.objects.filter(leaved_at=None)
    for visit in non_closed_visits:
        duration = visit.get_duration()
        visit.duration = Visit.format_duration(duration)
        visit.who_entered = visit.passcard
        visit.is_strange = visit.is_visit_long()
    context = {
        "non_closed_visits": non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
