# Referee card generator

## Description
My brother is referee.

He needs a card for every match that shows: playing teams, time and date, place and referees names.
I got bored with pasteing everything to paint, so I automated this with Python. 

#### Used libraries: PyQt5, easygui, cv2, Pillow, bs4, urllib2

Simple GUI allows user to scrape info from http://ligowiec.net/ and edit or provide it by yourself.

![empty_gui](https://user-images.githubusercontent.com/34914611/98465273-5fd67c80-21c8-11eb-95b8-efdd20ce8121.PNG)

## Example input and output:

Info: [link](http://ligowiec.net/mecz/142150/polonia-gizyn-iskra-ii-banie/komentarze/0)

Adding double space between words makes new line.

#### Scraped info:

![gui](https://user-images.githubusercontent.com/34914611/98465274-5fd67c80-21c8-11eb-9401-13c2e2905eb7.PNG)


Provided informations are placed on empty card:
![wizytowka](https://user-images.githubusercontent.com/34914611/98465272-5f3de600-21c8-11eb-9a40-560e61521514.png)

#### Output:

![output](https://user-images.githubusercontent.com/34914611/98465451-69141900-21c9-11eb-9518-cacad0caf85b.png)


#### Known bugs:
If website doesn't provide referess names, 'list index out of range' is thrown. Program doesn't stop.

After match day, website clears referess names, same thing happens like above.

....

#### TODO
Correct alignment of texts and images.
