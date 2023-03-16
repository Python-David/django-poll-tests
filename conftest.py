import datetime

import pytest
from django.utils import timezone

from polls.models import Choice, Question


@pytest.fixture()
def new_question_factory(db):
    def create_question(
            question_text: str,
            pub_date: datetime.datetime = timezone.now()
    ):
        question = Question.objects.create(
            question_text=question_text,
            pub_date=pub_date
        )

        return question
    return create_question


@pytest.fixture()
def new_choice_factory(db):
    def create_choice(
            question: Question,
            choice_text: str,
            votes: int = 0,
    ):
        choice = Choice.objects.create(
            question=question,
            choice_text=choice_text,
            votes=votes
        )

        return choice
    return create_choice


@pytest.fixture()
def new_question(db, new_question_factory):
    return new_question_factory("How are you?")


@pytest.fixture()
def new_choice_1(db, new_choice_factory, new_question):
    return new_choice_factory(new_question, "I am fine")


@pytest.fixture()
def new_choice_2(db, new_choice_factory, new_question):
    return new_choice_factory(new_question, "I am not fine")
