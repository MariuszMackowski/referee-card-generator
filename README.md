# Business card generator
My brother is referee.

He needs a card for every match that shows: playing teams, time and date, place and referees names.
I got bored with pasteing everything to paint, so I automated this with Python. 

#### Used libraries: PyQt5, easygui, cv2, Pillow, bs4, urllib2

Simple GUI allows user to scrape info from http://ligowiec.net/ and edit or provide it by yourself.
<img empty_gui placeholder>

#### Example input and output:

Info: [link](http://ligowiec.net/mecz/142150/polonia-gizyn-iskra-ii-banie/komentarze/0)

Scraped info:
<img gui placeholder>

Output
<img output placeholder>


#### Known bugs:
If website doesn't provide referess names, 'list index out of range' is thrown. Program doesn't stop.
After match day, website clears referess names, same thing happens like above.
....

#### TODO
Correct alignment of texts and images.
