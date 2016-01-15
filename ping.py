#v1.0.1 - Initial Release
#!/bin/python

import os
hostname = "192.168.0.200" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print hostname, 'is up!'
else:
  print hostname, 'is down!'

