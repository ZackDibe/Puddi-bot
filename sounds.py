import os
import re
import time
from collections import defaultdict

from slackclient import SlackClient

base_dir = os.path.dirname(os.path.realpath(__file__))

PLAYER = 'mpg123'
BOTS_CHANNEL = 'general'
TOKEN = ''
CLIENT = SlackClient(TOKEN)
SOUND_FILE = os.path.join(base_dir, 'sound.mp3')
COMMAND = PLAYER + ' ' + SOUND_FILE
MESSAGE_ON_PLAY = 'GIGA :puddi:'


def has_attachments(event):
    return 'attachments' in event


def check_attachment(event):
    regex = re.compile('.*Pull request closed.*')
    return any(regex.match(at['pretext']) for at in event['attachments'])


MATCH = defaultdict(lambda: lambda _: False)
MATCH['message'] = check_attachment
CHECK_TYPES = defaultdict(lambda: lambda _: False)
CHECK_TYPES['message'] = has_attachments


def action(client, command, message):
    print("{}: {}".format(message, command))
    client.rtm_send_message(BOTS_CHANNEL, message)
    os.system(command)


def listen(client):
    print('Connecting using token "{}"'.format(TOKEN))
    if client.rtm_connect():
        while True:
            for event in CLIENT.rtm_read():
                if event.get('type') and CHECK_TYPES[event['type']](event):
                    if MATCH[event['type']](event):
                        action(client, COMMAND, MESSAGE_ON_PLAY)
            time.sleep(1)
    else:
        print('Connection failed, invalid token?')

listen(CLIENT)
