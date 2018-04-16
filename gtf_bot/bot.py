import json
from os import environ
from telegram import Bot, Update
from zappa.async import task
from toolz.functoolz import compose, curry

webhook = lambda: environ.get('BOT_WEBHOOK_URL')
token = lambda: environ.get('BOT_TOKEN')
get_bot = compose(Bot, token)
bot_update = curry(lambda b, event: Update.de_json(event, b))


@task
def handler(event):
    update_from = compose(bot_update(get_bot()), json.loads)
    update = update_from(event)
    message = update.effective_message
    user = update.effective_user
    print(message, user)

def set_webhook():
    b = get_bot()
    url = webhook()
    b.setWebhook(url)

def get_webhook():
    b = get_bot()
    info = b.getWebhookInfo()
    print(info)

def del_webhook():
    b = get_bot()
    b.delete_webhook()

def get_me():
    b = get_bot()
    print(b.get_me())
