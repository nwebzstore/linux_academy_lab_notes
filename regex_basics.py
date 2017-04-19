# linux academy python 2.7 development notes:
# regular expression session

# example shows aquiring info to answer questsion about ip activity
# @ vim /var/log/secure: we want all and only sshd messages

import re

# test input for regex
line = "Apr 18 03:06:41 anthony1 sshd[894]: Server listening on 0.0.0.0 port 22."

match = re.search('sshd',line)
matcha = re.search('queef',line)
print(match)
print(matcha)

