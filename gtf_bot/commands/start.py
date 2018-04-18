from fn.func import identity

start_text = '''
Welcome to GTF BOT
'''

def answer_of_start(update):
    msg = update.effective_message
    msg.reply_markdown(start_text)
    return update