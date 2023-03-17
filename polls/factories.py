import factory
from django.utils import timezone
from faker import Faker

from .models import Question, Choice

fake = Faker()


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    question_text = fake.text()
    pub_date = timezone.now()


class ChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Choice

    question = factory.SubFactory(QuestionFactory)
    choice_text = fake.text()
    votes = 0
