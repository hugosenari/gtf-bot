from fn import _, F
from fn.func import identity
from .utils import get
from .text import answer_of_text
from telegram.utils.helpers import effective_message_type

no_answer = identity
answer_of_venue = identity  # TODO
answer_of_location = identity  # TODO
answers = {
    None: no_answer,
    'text': answer_of_text,
    'venue': answer_of_venue,
    'location': answer_of_location
}
answer_of = get(no_answer, answers)


def handle(update):
    msg_type = effective_message_type(update)
    answer = answer_of(msg_type)
    answer(update)
