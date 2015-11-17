import os
import re
import time

from slackclient import SlackClient

base_dir = os.path.dirname(os.path.realpath(__file__))

PLAYER = 'mpg123'
BOTS_CHANNEL = 'general'
TOKEN = ''
CLIENT = SlackClient(TOKEN)
PUDDI_PUDDI = os.path.join(base_dir, 'sound.mp3')
OH_MY = os.path.join(base_dir, 'ohmy.mp3')


def check_github_message(event):
    regex = re.compile('.*Pull request closed.*')
    return any(regex.match(at['pretext']) for at in event['attachments'])


def check_jira_message(event):
    regex = re.compile('.* completed .*')
    return regex.match(event['text'])


CHECK_TYPES = [
    (lambda x: x.get('username') == 'github', check_github_message, "GIGA :puddi:", PLAYER + ' ' + PUDDI_PUDDI),
    (lambda x: x.get('username') == 'jira', check_jira_message, "You rock :+1:", PLAYER + ' ' + OH_MY)
]


def action(client, command, message):
    print("{}: {}".format(message, command))
    client.rtm_send_message(BOTS_CHANNEL, message)
    os.system(command)


def listen(client):
    print('Connecting using token "{}"'.format(TOKEN))
    if client.rtm_connect():
        while True:
            for event in CLIENT.rtm_read():
                print(event)
                for check_type, match_regex, message, command in CHECK_TYPES:
                    if event.get('type') and check_type(event):
                        if match_regex(event):
                            action(client, command, message)
            time.sleep(1)
    else:
        print('Connection failed, invalid token?')

listen(CLIENT)
