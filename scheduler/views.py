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

            val_state = {}
            col_state = {}
            for sd in schedule_data:
                if sd.value:
                    if sd.time not in val_state:
                        val_state[sd.time] = [''] * 7
                    val_state[sd.time][sd.day] = sd.value
                if sd.type:
                    if sd.time not in col_state:
                        col_state[sd.time] = [''] * 7
                    col_state[sd.time][sd.day] = sd.type

            context_dict['value_state'] = json.dumps(val_state)
            context_dict['color_state'] = json.dumps(col_state)

            return render(request, 'home/finished.html', context_dict)

    return render(request, 'home/empty.html', context_dict)
