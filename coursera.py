import urllib.request as ur
import xml.etree.ElementTree as et

url = input('Enter location: ')
 'http://py4e-data.dr-chuck.net/comments_725306.xml'

total_number = 0
sum = 0

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)

#---------------------------------------------------------------------------------------------------------------
# XML with Python // File "<string>", line None 
import xml.etree.ElementTree as ET

data = ''''
<person>
    <name>Chuck</name>
    <phone type='intl'>
        +1 925 786 1715
    </phone>
    <email hide='yes'/>
</person> '''

tree = ET.fromstring(data)
print('Name:' , tree.find('name').text)
print('Attribute:' , tree.find('email').get('hide'))
#---------------------------------------------------------------------------------------------------------------
# Network Programs / Web Crawling with BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
html = urllib.request.urlopen(url , context=ctx).read()
soup = BeautifulSoup(html ,'html.parser')

retrieveAnchorTags = soup('a')
for tag in retrieveAnchorTags:
    print(tag.get('href' , None))

''' or '''

import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL -')
repeat = int(input('Enter number of repeatations: '))
position = int(input('Enter the link position: '))

#to repeat desired times
for i in range(repeat):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count +1

        #stopping at desired position
        if count>position:
            break
        url = tag.get('href', None)
        name = tag.contents[0]

print(name)

#---------------------------------------------------------------------------------------------------------------
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()                        #list for the desired output
for line in fh:                     #to read every line of file romeo.txt
    word= line.rstrip().split()     #to eliminate the unwanted blanks and turn the line into a list of words
    for element in word:            #check every element in word
        if element in lst:          #if element is repeated
            continue                #do nothing
        else :                      #else if element is not in the list
            lst.append(element)     #append
lst.sort()                          #sort the list (de-indent indicates that you sort when the loop ends)
print lst                           #print the list

#---------------------------------------------------------------------------------------------------------------
# Extracting data from json 
import urllib.request as ur
import json

# json_url = 'http://py4e-data.dr-chuck.net/comments_725307.json'

json_url = input("Enter location: ")
print("Retrieving ", json_url)
data = ur.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

sum = 0
total_number = 0

for comment in json_obj["comments"]:
    sum += int(comment["count"])
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)

#---------------------------------------------------------------------------------------------------------------
import urllib.error, urllib.request, urllib.parse
import json

target = "http://py4e-data.dr-chuck.net/json?"
local = input('Enter location: ')
url = target + urllib.parse.urlencode({'address': local, 'key' : 42})

print('Retriving', url)
data = urllib.request.urlopen(url).read()
print('Retrived', len(data), 'characters')
js = json.loads(data)
print(json.dumps(js, indent = 4)) 
print('Place id', js['results'][0]['place_id'])


