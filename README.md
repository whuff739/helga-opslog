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

~ show ~

show last 5 global entries:    
`!opslog showall`

show x number of global entries:  
`!opslog showall x`

show last 5 entries in current channel:  
`!opslog show` or `!opslog`

show x number of entries in current channel:  
`!opslog show x`

~ delete ~

deleting an entry:  
(A user can only delete the most recent entry they created.)  
`!opslog deletelast`  

~ search ~

searching entries in current channel:  
`!opslog search foo`

searching in different channel:  
`!opslog search #channel foo`

search all entries:  
`!opslog searchall foo`

searching for specific phrase in current channel:  
`!opslog search 'foo bar'`

searching for specific phrase in a different channel:    
`!opslog search #channel 'foo bar'`
