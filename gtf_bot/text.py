from .utils import get
from fn import _, F
from fn.iters import first
from fn.func import identity
from fn.monad import Option, optionable
from .commands.start import answer_of_start


no_answer = identity
answers = {
    None: no_answer,
    '/start': answer_of_start
}
answer_of = get(no_answer, answers)
skip_cmds_after_texts = lambda d: (v for k, v in d.items() if not k.offset)


def command_anwser_of(msg):
    entities = msg.parse_entities(['bot_command'])
    cmds = skip_cmds_after_texts(entities)
    return first(tuple(cmds) + tuple([None]))


def answer_of_text(update):
    msg = update.effective_message
    command = command_anwser_of(msg)
    answer = answer_of(command)
    return answer(update)
