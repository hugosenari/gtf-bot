from gtf_bot.handlers import no_answer
from gtf_bot.handlers import answer_of
from gtf_bot.handlers import answer_of_text
from gtf_bot.handlers import answer_of_venue
from gtf_bot.handlers import answer_of_location

def test_answer_of_text():
    result = answer_of('text')
    assert result == answer_of_text

def test_answer_of_venue():
    result = answer_of('venue')
    assert result == answer_of_venue

def test_answer_of_location():
    result = answer_of('location')
    assert result == answer_of_location

def test_answer_of_none():
    result = answer_of(None)
    assert result == no_answer

def test_answer_of_unknown():
    result = answer_of('asdfasdfas')
    assert result == no_answer
