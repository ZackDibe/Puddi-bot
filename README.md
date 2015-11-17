Simple sound bot
================

Simple bot that plays a sound on pull request closed

Inspired by [Casey Fulton's blog post](www.caseyfulton.com/audiosound-emojis-in-slack/).

Installation
----------

    $ sudo apt-get install python-dev
    $ sudo pip install websocket
    $ sudo pip install slackclient
    $ sudo apt-get install mpg123

Usage
-----
_Note:_ You must obtain a token for the user/bot. You can find or generate these at the [Slack API](https://api.slack.com/web) page. You also need to create the bot for that matter.

Run the bot:

    $ python sounds.py

Add support for other types of messages by changing `MATCH` and `CHECK_TYPES`