import json
import logging
from fn import _, F
from fn.op import flip
from fn.func import curried
from zappa.async import task
from telegram import Bot, Update
from os import environ as from_env
from .handlers import handle
from .utils import get as D

logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

get = D(None, from_env)
token = F(get, 'BOT_TOKEN')
webhook = F(get, 'BOT_WEBHOOK_URL')
get_bot = F(token) >> Bot
bot_update = lambda b, event: print('handler', json.dumps(event)) or Update.de_json(event, b())
update_from = F(json.loads) >> (bot_update, get_bot)

@task
def handler(event):
    print('handler', event)
    update = update_from(event)
    handle(update)

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

def get_update():
    b = get_bot()
    updates = b.get_updates()
    update = (updates + [None])[0]
    print(update and update.to_json() or update)
