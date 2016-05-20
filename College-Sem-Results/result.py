import urllib
import re
from BeautifulSoup import *

url="http://vesit.edu/computer-engineering"
#url=raw_input("Enter your College Website URL which will display results:")

html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)
table = soup.find('table')

#Change the Semester according to your requirements 

td = table.find('td', text='Semester VIII')
nextd = td.findNext('td')
if re.search('href="',str(nextd)):
	print "Results are out! Time to Evaluate your Efforts!"
	print nextd.text
else:
	print "Patience is the key to Success."
