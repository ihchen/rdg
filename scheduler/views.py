from django.shortcuts import render

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
            context_dict['schedule_data'] = schedule_data
            return render(request, 'home/finished.html', context_dict)

    return render(request, 'home/empty.html', context_dict)
