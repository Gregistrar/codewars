# My Solution

import re

class Mod:
    mod4 = re.compile(r".*\[[+-]?(\d*([02468][048]|[13579][26])|[048])\].*")
                      
        
    def match(self,test):
        return self.mod4.match(test)
