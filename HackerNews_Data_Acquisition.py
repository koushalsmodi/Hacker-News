# Program collects URL, headline, and vote count data from the official Hacker News website, 
# spanning from 2008 to 2022, with a monthly breakdown and coverage for each of the 28 days per month.


import requests # to acquire the data from the url link 
from bs4 import BeautifulSoup # to web scrape the data by parsing the data
import csv # write the data to a csv file



years = [str(i) for i in range(2022, 2023)] # years 2008-2022
months = [str(i) for i in range(1,2)] # 1-12 months, that is, January to December
days = [str(i) for i in range(1,3)] # 1-28 days

dates = [] # dates list stores each date 

# nested for loops
for year in years:
    for month in months:
        for day in days:
            date = year + '-' + month + '-' + day # specific format for date 
            dates.append(date) 
            
# empty lists to store data for url links, vote counts and headlines          
urls = []
vote_counts = []
headlines = []

for date in dates: 
    for i in range(1,6): # 5 pages per day for each day (website section: past)
        
        url = 'https://news.ycombinator.com/front?day=' + date + f'&p={i}'
        # sample: https://news.ycombinator.com/front?day=2007-11-11&p=1
        
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib') # html parser to parse the contents of the url
        
        
        table1 = soup.find_all('span', class_ = 'titleline') # table1 stores urls and headlines on the website
        table2 = soup.find_all('span', class_ = 'score') # table2 stores vote counts on the website
        
        # adding urls and headlines
        for row in table1:
            urls.append(row.a['href']) # sample: <a href="https://www.fly.faa.gov/adv/adv_spt.jsp"
            headlines.append(row.a.text)
            # sample: <a href="https://www.fly.faa.gov/adv/adv_spt.jsp" rel="noreferrer">Starship will attempt a launch this weekend</a
            
        # adding votes
        for row in table2:
            vote_counts.append(row.text.split()[0])
            # sample:  <span class="score" id="score_38257794">74 points</span>
      
        print(url)



        
num_posts= len(headlines) # number of posts is equal to the number of headlines
posts = [] # posts list
for i in range(num_posts):
    dct = {'URL':urls[i], 'Headline':headlines[i], 'Votes':vote_counts[i]} # dictionary to store
    # keys: URL, Headlines, Votes and values: respective entries inside their list
    posts.append(dct) # a list with a dictionary

                                                                       


filename = '/Users/koushalsmodi/Desktop/web_scraping/trial.csv' # file to store data

with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['URL', 'Headline', 'Votes'])  # write data
    w.writeheader() # header to classify the data 

    for post in posts:
        w.writerow(post) # write the data across each row
                       
        
        


        
        
        
            














    
        
            
            
            
            

