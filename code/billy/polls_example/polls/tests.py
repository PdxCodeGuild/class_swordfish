from venv import create
from django.test import TestCase

import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        '''
        was_published_recently() should return False for question with a pub_date in the future.
        '''
        future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=1))
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        recent_question = Question(pub_date=timezone.now() - datetime.timedelta(hours=12))
        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_old_question(self):
        old_question = Question(pub_date=timezone.now() - datetime.timedelta(days=7))
        self.assertIs(old_question.was_published_recently(), False)
class IndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "no polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        question = create_question("past question", days=-7)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])
        self.assertContains(response, question.question_text)
    
    def test_future_test(self):
        question = create_question("future question", days=+7)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response,  )
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        question1 = create_question("past question", days=-7)
        question2 = create_question("future question", days=+7)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question1])
        self.assertContains(response, question1.question_text)

    def test_2_past_questions(self):
        question1 = create_question("past question", days=-7)
        question2 = create_question("future question", days=-14)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question1, question2])
        self.assertContains(response, question1.question_text)
        self.assertContains(response, question2.question_text)
