import pytest

from pytest_factoryboy import register
from polls.factories import QuestionFactory, ChoiceFactory

register(QuestionFactory)  # question_factory
register(ChoiceFactory)  # choice_factory


@pytest.fixture()
def new_question1(db, question_factory):
    question1 = question_factory.create()
    return question1


@pytest.fixture()
def new_choice1(db, choice_factory):
    choice1 = choice_factory.create()
    return choice1

