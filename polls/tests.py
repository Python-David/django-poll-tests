import pytest
from .models import Question, Choice


@pytest.mark.django_db
def test_new_question(new_question1):
    count = Question.objects.all().count()

    print(count)
    print(new_question1.question_text)

    assert True


@pytest.mark.django_db
def test_new_choice(choice_factory, new_question1):
    choice = choice_factory.create(question=new_question1, choice_text='Blue')

    print(choice.question.question_text)
    assert True


@pytest.mark.django_db
def test_new_choice_2(new_choice1):
    count = Choice.objects.all().count()

    print(count)
    print(new_choice1.question.pub_date)

    assert True
