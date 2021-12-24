import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://news.ycombinator.com')
#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
links = (soup.select('.titlelink'))
subtext = soup.select('.subtext')

#function to sort the votes
def sort_stories_by_votes(hnlist):
    #lambda is used to sort the list as dictionary votes couldn't be sorted by itself
    return sorted(hnlist, key= lambda k:k['votes'], reverse= True)

def create_custom_hn(links,subtext):
    #to create a dictionary that contains links and subtexts
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points','')) 
            if points >99:
                hn.append({'title':title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))