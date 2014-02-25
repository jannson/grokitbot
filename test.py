#!/usr/bin/env python
from AIMLBot import AIMLBot
import sys
import re

nickname = 'piming'
aiml = AIMLBot(nickname)
#sentence = aiml.on_MSG_IN(nickname, 'hello')

while True:
    print aiml.on_MSG_IN(nickname, raw_input("> "))



