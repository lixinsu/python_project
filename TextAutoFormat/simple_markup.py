import sys
import re
from util import *
print '<html><head><tilte>...</title><body>'
title=True
for block in blocks(open("plain.txt")):
    block = re.sub(r'\*(.+?)\*',r'<em>\1<\em>',block)
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        print('<p>')
        print block
        print '</p>'
print '</body><html>'
