from datetime import datetime as dt

from helga.plugins import command
from helga.db import db
from helga import log, settings


logger = log.getLogger(__name__)

MAX_CHANNEL_SHOW = 10

@command('opslog', help='Usage: helga opslog [ENTRY]')
def opslog(client, channel, nick, message, cmd, args):

    if not args:
        return show(5)    
    
    subcmd = args[0]

    if subcmd == 'show' or not args:
        if args[1].isdigit():
            return show(args[1], nick)
        else:
            return show(5)
    elif subcmd == 'search':
        input = ' '.join(args[1:])
        return search(input, nick)
    elif subcmd == 'deletelast':
        return deletelast(_)
    else:
        logger.info('Adding an opslog entry by user %s', nick)
        input = ' '.join(args)
        db.opslog.insert({
            'date': dt.utcnow(),
            'logline': input,
            'user': nick,
        })
            
    
def show(entries, user=None):
    """


    """
    records = []
    cur = db.opslog.find().sort('date', -1).limit(entries)
    for i in cur:
        to_add = '%s %s: %s' % ("{:%m/%d/%y %-I:%M:%S}".format(i['date']), i['user'], i['logline'])
        records.append(to_add)
    return records

def deletelast():
    pass

def search():
    query = {'logline': syllables}
    pass

