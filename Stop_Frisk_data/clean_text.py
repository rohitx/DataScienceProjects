from collections import defaultdict

with open('CrimeCode.txt', 'r') as f:
    data = f.readlines()

d = defaultdict()

for line in data:
    number = line[:3]
    if not number.isdigit():
        number = number[:len(number)-1].strip()
        text = line[2:]
    else:
        text = line[3:]
    d[int(number)] = text.strip()

with open('CrimeCodesClean.txt', 'w') as g:
    for number, text in d.iteritems():
        g.write("{n:0d}:{t:2s}<br>\n".format(n=number, t=text))
