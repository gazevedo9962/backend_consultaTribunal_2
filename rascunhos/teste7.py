import re

s = 'A! B. C D 1-1'
pattern = r'\d-\d'

l = re.split(pattern, s)
print(l)

p = re.compile('[a-z]+')
print(p.match('::: message'))
m = p.search('::: message') 
print(m)
#<re.Match object; span=(4, 11), match='message'>
m.group()
m.span()
print(re.search(' - \d+', '21544message65465465 - awdasdfa - asdas - 1212312')) 
