# A simple network chat program between two IPs

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



if ( os.path.isfile("chat.conf") ):
  config = {}
  execfile("chat.conf", config)


cls()

print "Chat Program"

##
# Decide whether we're calling or we're waiting
if (len(sys.argv) >= 2):
  network.call(sys.argv[1], whenHearCall=heard)
else:
  if ( network.testClient('192.168.1.101', 8888) ):
    network.wait(whenHearCall=heard)
  else:
    network.call(config['default_client'], whenHearCall=heard)



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
  
