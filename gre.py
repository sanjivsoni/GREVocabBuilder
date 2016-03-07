from bs4 import BeautifulSoup
from random import randint
import urllib2
import pynotify
import time


def sendMessage(title, message):
	pynotify.init("Test")
	notice = pynotify.Notification(title, message)
	notice.show()
	return

webpage = urllib2.urlopen('https://quizlet.com/58647605/kaplan-900-flash-cards').read()

# Parse the entire webpage
soup = BeautifulSoup(webpage)

word = []
meaning = []

# Scrape words from soup
for words in soup.find_all("span", class_="TermText qWord lang-en"):
	# Convert ascii to string
	word.append(words.text.encode("utf-8"))

# Scrape meanings from soup
for meanings in soup.find_all("span", class_="TermText qDef lang-en"):
	meaning.append(meanings.text.encode("utf-8"))

print("Churning words !")


while(1):
	index = randint(0,700)
	print(index)
	# First just pop the word on screen to wait for response
	sendMessage(word[index],"")
	# Adjust the response time between word and its meaning
	time.sleep(15)
	# Display the meaning with the word
	sendMessage(word[index], meaning[index])
	# Time after which a new word pops on screen
	time.sleep(600)
