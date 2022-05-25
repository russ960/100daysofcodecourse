from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
url_code = requests.get(url).text
soup = BeautifulSoup(url_code, "html.parser")

rank_title = soup.find_all(name='h3', class_='title')

movie_rank = {}

for movie in rank_title:
    movie_data = movie.text.replace(': ', ':')
    movie_data = movie_data.replace(') ', ':')
    rank = int(movie_data.split(':')[0])
    movie_title = movie_data.split(':')[1]
    if movie_title == "Spirited Away":
        rank = 80
    movie_rank[rank] = movie_title
    
with open("45\\movies.txt", mode='w') as file:
    for mr in range(1,101):
        file.write(f"{mr}: {movie_rank[mr]}\n")
     

# print(movie_rank)