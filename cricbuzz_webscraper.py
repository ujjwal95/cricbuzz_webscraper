import urllib2

cricbuzz = "http://www.cricbuzz.com/cricket-match/live-scores"

page = urllib2.urlopen(cricbuzz)

from bs4 import BeautifulSoup
import time
from gi.repository import Notify

soup = BeautifulSoup(page)
matches_info = soup.find_all('div' ,class_="cb-col-50 cb-col")
while True:	
	body = ''
	for scores in matches_info:
		x = scores.get_text().encode("unicode-escape").replace("\\xa0\\u2022\\xa0 ", "vs ")
		body += x + "\n"
		# print body
	summary = "Current Scores"
	Notify.init("Cricket Score")
	notification = Notify.Notification.new(summary,body)
	notification.set_timeout(8000)
	notification.show()
	time.sleep(15)
