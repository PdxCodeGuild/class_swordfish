from django.test import TestCase

import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question #.models because it's same folder

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently should return False for questions with a pub_date in the future.
        """
        future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=1))
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        recent_question = Question(pub_date=timezone.now()- datetime.timedelta(hours=12))
        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_old_question(self):
        old_question = Question(pub_date=timezone.now() - datetime.timedelta(days=7))
        self.assertIs(old_question.was_published_recently(), False)

class IndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('pulls:index'))
        self.assertEqual(response.status_code, 200) #did page load ok?
        self.assertContains(response, "No polls are available.") #must be exactly the same as it's written in index.html
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        question = create_question("Past question?", days=-7)
        response = self.client.get(reverse('pulls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])
        self.assertContains(response,question.question_text)

    def test_future_question(self):
        question = create_question("Future question?", days=7)
        response = self.client.get(reverse('pulls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        question1 = create_question("Past question?", days=-7)
        question2 = create_question("Future question?", days=7)
        response = self.client.get(reverse('pulls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question1])
        self.assertContains(response, question1.question_text)

    def test_two_past_questions(self):
        question1 = create_question("Past question 1?", days=-7)
        question2 = create_question("Past question 2?", days=-14)
        response = self.client.get(reverse('pulls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question1, question2])
        self.assertContains(response, question1.question_text)
        self.assertContains(response, question2.question_text)

class DetailViewTests(TestCase):
    def test_future_question(self):
        question = create_question("Future question?", days=7)
        response = self.client.get(reverse('pulls:detail', args=(question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        question = create_question("Past question?", days=-7)
        response = self.client.get(reverse('pulls:detail', args=(question.id,)))
        self.assertContains(response, question.question_text)