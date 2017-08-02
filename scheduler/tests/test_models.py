from django.test import TestCase
from django.db.utils import IntegrityError

from scheduler.models import Semester, SemesterSchedule, Dancer, Auditionee, DancerSchedule

# class ModelTestCase(TestCase):
#     def createSemester(self, title=''):
#         s = Semester()
#         if title:
#             s.title = title
#         s.save()
#         return s
#
#     def createSemesterSchedule(self, semester, row=0, col=0, value=''):
#         sd = SemesterSchedule()
#         sd.semester = semester
#         sd.row = row
#         sd.col = col
#         if value:
#             sd.value = value
#         sd.save()
#         return sd
#
#     def createDancer(self, first_name='', middle_initial='', last_name='', email=''):
#         d = Dancer()
#         d.first_name = first_name
#         d.middle_initial = middle_initial
#         d.last_name = last_name
#         d.email = email
#         d.save()
#         return d
#
#     def createAuditionee(self, semester, dancer, dancer_number=1, choreographer=False, notes=''):
#         a = Auditionee()
#         a.semester = semester
#         a.dancer = dancer
#         a.dancer_number = dancer_number
#         a.notes = notes
#         a.choreographer = choreographer
#         a.save()
#         return a
#     )
#
#     def createDancerSchedule(self, dancer, row=0, col=0, value=False):
#         ds = DancerSchedule()
#         ds.dancer = dancer
#         ds.row = row
#         ds.col = col
#         ds.value = value
#         ds.save()
#         return ds
