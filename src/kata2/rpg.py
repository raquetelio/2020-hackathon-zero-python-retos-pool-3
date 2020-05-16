#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(passLen))
