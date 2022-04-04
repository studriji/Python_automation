#run always with admin permission
#target is to roll back website to loob back ip address that is 127.0.0.1
#add the text in host.txt file

from datetime import datetime

host = 'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'

url = ['www.facebook.com']


#_________blocking____________
'''
with open(host,'r+') as file:
      content = file.readlines()
      for site in url:
         if site in content:
            pass
         else:
            file.write(redirect+" "+site+"\n")

'''
#____________unblocking_____________

with open(host,'r+') as file:
      content = file.readlines()
      file.seek(0)
      for line in content:
         if not any(site in line for site in url):
            file.write(line)
         file.truncate()
      