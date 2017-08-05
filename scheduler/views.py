from django.shortcuts import render

import json

from scheduler.models import Current, Semester, SemesterSchedule

def home(request):
    curr = Current.objects.all()
    context_dict = {}

    if len(curr):
        curr = curr[0]
        context_dict['semester'] = curr.semester

        if curr.progress == 0:
            return render(request, 'home/pre_audition.html', context_dict)
        elif curr.progress == 1:
            return render(request, 'home/auditioning.html', context_dict)
        else:
            schedule_data = SemesterSchedule.objects.filter(semester=curr.semester)

            schedule_state = {}
            for sd in schedule_data:
                if sd.day not in schedule_state:
                    schedule_state[sd.day] = {}
                if sd.time not in schedule_state[sd.day]:
                    schedule_state[sd.day][sd.time] = {}

                if sd.value:
                    schedule_state[sd.day][sd.time]['value'] = sd.value
                if sd.type:
                    schedule_state[sd.day][sd.time]['color'] = sd.type

            context_dict['schedule_state'] = json.dumps(schedule_state)

            return render(request, 'home/finished.html', context_dict)

    return render(request, 'home/empty.html', context_dict)
