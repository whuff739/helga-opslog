## helga-opslog

A helga plugin to record & query opslog entries.

### Installation

```
source bin/activate
git clone https://github.atl.pdrop.net/whuff/helga-opslog.git
cd src/helga-opslog
python setup.py develop
```

After installing the helga-opslog the helga process requires a restart.

### Usage

Adding an entry:  

`!opslog <foo>`

Deleting an entry:  

A user can only delete entries they created. Only the most previous entry can be deleted.  
`!opslog deletelast`

Searching:

searching all entries:  
`!opslog search foo`

searching by channel:  
`!opslog search #channel foo`

searching for specific words together:  
`!opslog search 'foo bar'`

combining channel and specific words:  
`!opslog search #channel 'foo bar'`

Show:

show last 5 entries:  
`!opslog`

show x number of entries:  
`!opslog show x`
