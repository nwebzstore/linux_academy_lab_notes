# linux academy python 2.7 development notes:
# regular expression session

# example shows aquiring info to answer questsion about ip activity
# @ vim /var/log/secure: we want all and only sshd messages

import re

# test input for regex
line = "Apr 18 03:06:41 anthony1 sshd[894]: Server listening on 0.0.0.0 port 22."

match = re.search('sshd',line)

match1= re.search('[A-Z][a-z]{2}\s{1,2}\d{1,2}\s\d{2}\s\w*\sshd\[\d*\]: Failed password for \w+ from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} port \d* ssh2',line)

matcha = re.search('^(.*?)\s(\w+)\ssshd.*?Failed\spass.*?from\s(.*?)\sport.*$',line)
