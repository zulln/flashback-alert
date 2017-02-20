#coding: utf-8
# it is a fulhack, but hey, it works

import requests
import re
import HTMLParser

keywords = ["zulln", "GitHub", "munsår", "betyg"] # keywords of interest

r = requests.get('https://www.flashback.org/nya-amnen')

if r.status_code != 200:
	exit('Flashback fucked up.')
	
pushed = []
for thread in re.findall(r'id="thread_title_(.+?)">(.+?)</a>', r.text, re.DOTALL):
    threadId = thread[0]
    threadTitle = HTMLParser.HTMLParser().unescape(thread[1])
    
    for keyword in keywords:
        if keyword.lower() in threadTitle.encode("UTF-8").lower():
            if "db" not in locals():
                dbFile = open("pushed.txt", "r")
                db = [line.rstrip() for line in dbFile]
                dbFile.close()
                
            if threadId not in db and threadId not in pushed: # a thread could contain multiple keywords
                msg = threadTitle + " https://flashback.org/t" + threadId
                
                payload = {
                	"token" : "[application_token]", # application token from pushover.net
                	"user" : "[user_key]",  # user key
                	"message" : msg
                }

                r = requests.post("https://api.pushover.net/1/messages.json", data=payload)
                if r.status_code != 200:
                	exit("Failed to send push.")
                
                pushed.append(threadId)
     
if pushed:
    dbFile = open("pushed.txt", "a")
    dbFile.write("\n".join(pushed) + "\n")
    dbFile.close()       