from bs4 import BeautifulSoup
import requests
import random
try:
    user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    ]

    source = requests.get('https://www.imdb.com/chart/top/', headers={'User-Agent': random.choice(user_agents_list)})

    soup = BeautifulSoup(source.text,'html.parser')
    
    
    # Find the <ul> element containing the list of movies
    movies_list = soup.find("ul", class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-3a353071-0 wTPeg compact-list-view ipc-metadata-list--base")

    # Find all <li> elements within the <ul> element
    movie_items = movies_list.find_all("li")

    # Loop through each <li> element and extract the text
    for movie_item in movie_items:
        movie_title = movie_item.find("div", class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-14dd939d-7 fjdYTb cli-title").text.strip()
        print(movie_title)






except Exception as e:
    print(e)
