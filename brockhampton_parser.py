# Import all necessary modules
import time
startTime = time.time()
from bs4 import BeautifulSoup
import urllib.request
# import certifi
import requests
# import re
from itertools import groupby

# Attain all song names from lyrics.com since its easier than scraping from genius. This names will be put into genius' song url formula to scrape individual pages.
# The following imports the page data as lxml format
sauce = urllib.request.urlopen('https://www.lyrics.com/artist.php?name=BROCKHAMPTON&aid=3228163&o=1').read()
soup = BeautifulSoup(sauce, 'lxml')

# We set up an empty array and then scrape for song names
song_names = []
for row in soup.find_all('tr'):
    s = row.text
    result = ''.join([i for i in s if not i.isdigit()])
    array = result.split(':')
    song_names.append(array[0])

# The following first removes an unneeded trailing datum, then formats the names so they work with the genius url formula
song_names.remove(song_names[0])
song_names = [w.replace(' / ', '-') for w in song_names]
song_names = [w.replace(' ', '-') for w in song_names]
song_names = [w.replace("'", '') for w in song_names]

# Set necessary info for lyrics parser
first_names = ['ameer', 'matt', 'kevin', 'dom', 'merlyn', 'russell', 'rodney', 'bearface', 'joba', 'ryan']
brockhampton = ['ameer vann', 'matt champion', 'kevin abstract', 'dom mclennon', 'merlyn wood', 'russell boring', 'rodney tenor', 'bearface', 'joba', 'ryan beatty']
identifiers_list = ['[chorus:', '[verse:', '[outro:', '[', '[bridge:', '[verse', '1:', '2:', '3:', '4:', '5: ', '6: ']
bh_members = ' '.join(brockhampton).split(' ')

for name in first_names:
    exec(name + '=[]')  # creates an empty array for each member


def lyrics_parser(url):
    sauce = requests.get(url).content
    soup = BeautifulSoup(sauce, 'lxml')

    for row in soup.find_all("div", {"class": "lyrics"}):
        for item in row.find_all('p'):
            lyrics = item.text  # lyrics how text only would look

    lyrics_lines = lyrics.splitlines()
    lyrics_list = " ".join(lyrics_lines).lower().split(' ')
    # Top two lines ensure lyrics split up by word perfectly

    lyrics_list = [l.replace(']', '') for l in lyrics_list]

    for i, word in enumerate(lyrics_list):
        if word in identifiers_list:
            lyrics_list[i] = ''

    array = [list(g) for k, g in groupby(lyrics_list, key=bool) if k]

    for name in first_names:
        for lst in array:
            if name in lst:
                exec(name + '.append(lst)')


for title in song_names:
    url = 'https://genius.com/Brockhampton-' + title.lower() + '-lyrics'
    lyrics_parser(url)

# The following is used to print the final results
for name in first_names:
    ameer_count = 0
    for lst in ameer:
        for word in lst:
            if word not in bh_members:
                ameer_count += 1
print('Ameer Vann: ' + str(ameer_count))

for name in first_names:
    joba_count = 0
    for lst in joba:
        for word in lst:
            if word not in bh_members:
                joba_count += 1
print('Joba: ' + str(joba_count))

for name in first_names:
    kevin_count = 0
    for lst in kevin:
        for word in lst:
            if word not in bh_members:
                kevin_count += 1
print('Kevin Abstract: ' + str(kevin_count))

for name in first_names:
    matt_count = 0
    for lst in matt:
        for word in lst:
            if word not in bh_members:
                matt_count += 1
print('Matt champion: ' + str(matt_count))

for name in first_names:
    merlyn_count = 0
    for lst in merlyn:
        for word in lst:
            if word not in bh_members:
                merlyn_count += 1
print('Merlyn Wood: ' + str(merlyn_count))


for name in first_names:
    dom_count = 0
    for lst in dom:
        for word in lst:
            if word not in bh_members:
                dom_count += 1
print('Dom Mclennon: ' + str(dom_count))

endTime = time.time()
Time = int(endTime - startTime)
performanceTime = f'Took {Time} seconds to Perform'
print(performanceTime)
