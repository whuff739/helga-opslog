# -*- coding: utf-8 -*-

import re
from datetime import datetime as dt
from datetime import timedelta

from helga.plugins import command, preprocessor, random_ack
from helga.db import db
from helga import log, settings


logger = log.getLogger(__name__)

RESULT_LEN = 5
MAX_RESULT_LEN = 10


@command('opslog', shlex=True, help='Usage: helga opslog [show <count>|deletelast|search <string>] <entry>')
def opslog(client, channel, nick, message, cmd, args):

    if not args:
        return show(client, channel, RESULT_LEN)    
    
    subcmd = args[0]

    if subcmd == 'show':
        if len(args) >= 2 and args[1].isdigit():
            return show(client, channel, int(args[1]), nick)
        else:
            return show(client, channel, RESULT_LEN)
    elif subcmd == 'search':
        return search(client, channel, args[1:], nick)
    elif subcmd == 'deletelast':
        return deletelast(nick)
    else:
        logger.info('Adding an opslog entry by user %s', nick)
        input = ' '.join(args)
        db.opslog.insert({
            'date': dt.utcnow(),
            'logline': input,
            'user': nick,
        })
            
    
def show(client, channel, entry_count, user=None):
    records = []
    cur = db.opslog.find().sort('date', -1).limit(entry_count)
    for i in cur:
        to_add = '{0:%a %d/%m %H:%M} {1}: {2}'.format(
                tz_convert(i['date']),
                i['user'],
                i['logline'])
        records.append(to_add)
    if entry_count > MAX_RESULT_LEN:
        if channel != user:
            client.me(channel, 'whispers to {0}'.format(user))
            client.msg(user, u'\n'.join(records))
        else:
            return records
    else:
        return records


def deletelast(user):
    logger.info('Deleting opslog entry by user %s', user)
    cur = db.opslog.find_one_and_delete({'user': user}, sort=[('date', -1)])
    return random_ack()


def search(client, channel, s_strings, user):
    records = []
    record_strings = []
    for i in s_strings:
        regex = re.compile(i, re.IGNORECASE)
        cur = db.opslog.find({'logline': regex}).sort('date', -1)
        for j in cur:
            if j not in records:
                records.append(j)
    for i in records:
        to_add = '{0:%a %d/%m %H:%M} {1}: {2}'.format(
                tz_convert(i['date']),
                i['user'],
                i['logline'])
        record_strings.append(to_add)
    if len(record_strings) > MAX_RESULT_LEN:
        if channel != user:
            client.me(channel, 'whispers to {0}'.format(user))
            client.msg(user, u'\n'.join(records))
        else:
            return record_strings
    else:
        return record_strings


def tz_convert(utc_dt):
    return utc_dt - timedelta(hours=4)
