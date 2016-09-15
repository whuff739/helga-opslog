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

adding an entry:  
`!opslog foo`

show last 5 entries:  
`!opslog` or `!opslog show`

show x number of entries:  
`!opslog show x`

deleting an entry:  
(A user can only delete the most recent entry they created.)  
`!opslog deletelast`  

searching all entries:  
`!opslog search foo`

searching by channel:  
`!opslog search #channel foo`

searching for specific words together:  
`!opslog search 'foo bar'`

combining channel and specific words:  
`!opslog search #channel 'foo bar'`
