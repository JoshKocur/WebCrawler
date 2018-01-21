import sys
import urllib2
import re
from bs4 import BeautifulSoup


#Returns the HTML when passed a URL
def getHtml(url):
    clientResponse = urllib2.urlopen(url)
    htmlText = clientResponse.read()
    return htmlText

#Prints out all the Links in the HTML for a passed url, used for a visual add in developing
def parseForLinks(url):
    searchSpace = getHtml(url)
    soup = BeautifulSoup(searchSpace, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
   
    
    
    

def recursiveCrawler(url, num):
    #Base case, get the HTML for just the passed url   This case works
    if num <=0:
        print(getHtml(url))
        return None
    #Recursive case     
    else:
        print(getHtml(url))
        searchSpace = getHtml(url)
        soup = BeautifulSoup(searchSpace, 'html.parser')
        
        num = num -1
        for link in soup.find_all('a'):
            checkString = link.get('href')
            if re.match("http", checkString):
                recursiveCrawler((link.get('href')), num)


            
url = sys.argv[1]
num = sys.argv[2]
number = int(num)



recursiveCrawler(url, number)    
