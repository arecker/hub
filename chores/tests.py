from django.test import TestCase
from django.utils import timezone

from .models import WeeklyChore, MonthlyChore


class WeeklyChoreTestCase(TestCase):
    def test_find_next_due_date(self):
        now = timezone.now().replace(year=1990, month=10, day=6)

        chore = WeeklyChore(
            name='test chore',
            day_of_the_week=0,
            last_completed=now.replace(year=1990, month=10, day=4)
        )

        actual = chore.find_next_due_date(now=now)
        expected = now.replace(year=1990, month=10, day=8)

        self.assertEqual(actual, expected)


class MonthlyChoreTestCase(TestCase):
    def test_find_next_due_date_this_month(self):
        now = timezone.now().replace(year=1990, month=10, day=6)

        chore = MonthlyChore(
            name='test chore',
            day_of_the_month=20,
            last_completed=now.replace(year=1990, month=10, day=4)
        )

        actual = chore.find_next_due_date(now=now)
        expected = now.replace(year=1990, month=10, day=20)

        self.assertEqual(actual, expected)

    def test_find_next_due_date_next_month(self):
        now = timezone.now().replace(year=1990, month=12, day=6)

        chore = MonthlyChore(
            name='test chore',
            day_of_the_month=5,
            last_completed=now.replace(year=1990, month=10, day=4)
        )

        actual = chore.find_next_due_date(now=now)
        expected = now.replace(year=1991, month=1, day=5)

        self.assertEqual(actual, expected)
