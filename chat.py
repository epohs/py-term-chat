# A simple network chat program between to Raspberry Pi's

import network
import sys
import os



def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def heard(phrase):
  if (phrase.rstrip() == "C"):
  	cls()
  elif (phrase.rstrip() == "Q"):
  	network.hangUp()
  else:
  	print "them: " + phrase

cls()

print "Chat Program"

if (len(sys.argv) >= 2):
  network.call(sys.argv[1], whenHearCall=heard)
else:  
  network.wait(whenHearCall=heard)



print "Chat away!!"  
while network.isConnected():
  phrase = raw_input()
  if (phrase == "C"):
  	cls()
  elif (phrase.rstrip() == "Q"):
  	network.say(phrase)
  	network.hangUp()
  else:
  	print "me: " + phrase
  
  network.say(phrase)
  
