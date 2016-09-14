from datetime import datetime as dt
from datetime import timedelta

from helga.plugins import command
from helga.db import db
from helga import log, settings


logger = log.getLogger(__name__)

RESULT_LEN = 5
MAX_RESULT_LEN = 10

@command('opslog', help='Usage: helga opslog [show <count>|deletelast|search <string>] <entry>')
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
        return search(_)
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
    #to_delete = db.opslog.find({'user': user}).sort('date', -1).limit(1)
    #logger.info(to_delete._id)
    deleted = db.opslog.delete_one({'_id': to_delete.get('_id')}).sort('date', -1)
    logger.info('Deleting opslog entry by user %s', user)

def search():
    pass

def tz_convert(utc_dt):
    return utc_dt - timedelta(hours=4)
