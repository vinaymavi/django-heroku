import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question


class QuestionMethodTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for question whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently should return false for question whose
        pub_date is old
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently should return true for question which
        pub_date is 1 hour before.
        """
        time = timezone.now()-datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(),True)
