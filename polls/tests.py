def test_question(new_question):
    assert new_question.question_text == "How are you?"


def test_choice(new_choice_1, new_question):
    assert new_choice_1.question.question_text == "How are you?"


def test_second_choice(new_choice_2, new_question):
    assert new_choice_2.question.question_text == "How are you?"

