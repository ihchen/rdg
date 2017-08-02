from django.test import TestCase

from datetime import date
from scheduler.models import Semester, Current
# from scheduler.views import home

class HomeViewTests(TestCase):
    def test_no_current_uses_empty_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/empty.html')

    def test_progress_0_uses_pre_audition_template(self):
        s = Semester()
        s.title = "test 20xx"
        s.audition_date = date.today()
        s.save()

        c = Current()
        c.semester = s
        c.save()

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/pre_audition.html')

    def test_progress_1_uses_auditioning_template(self):
        s = Semester()
        s.title = "test 20xx"
        s.audition_date = date.today()
        s.save()

        c = Current()
        c.semester = s
        c.progress = 1
        c.save()

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/auditioning.html')

    def test_progress_2_uses_finished_template(self):
        s = Semester()
        s.title = "test 20xx"
        s.audition_date = date.today()
        s.save()

        c = Current()
        c.semester = s
        c.progress = 2
        c.save()

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/finished.html')
