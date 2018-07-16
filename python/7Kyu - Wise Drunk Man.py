# My Solution

import re
def wdm(talk):
    clean = talk.replace('puke','')
    cleaner = clean.replace('hiccup', '')
    return re.sub(' +',' ',cleaner).lstrip().rstrip()
