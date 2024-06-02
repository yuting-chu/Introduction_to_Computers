#hw5_3
#經濟系大三 D54101039朱郁庭

import csv
from collections import defaultdict

#Q1
def Q1(data):
    movies_2016 = [movie for movie in data if movie['Year'] == '2016']
    movies_2016.sort(key=lambda x: float(x['Rating']), reverse=True)
    top_3 = movies_2016[:3]
    print("1.Top-3 movies with the highest ratings in 2016:")
    for i, movie in enumerate(top_3, 1):
        print(f"\tTop {i}: {movie['Title']} with rating {movie['Rating']}")

#Q2
def Q2(data):
    directors = defaultdict(int)
    for movie in data:
        directors[movie['Director']] += 1
    most_movies_director = max(directors, key=directors.get)
    print(f"2.The director involved in the most movies: {most_movies_director}")

#Q3
def Q3(data):
    actors_revenue = defaultdict(int)
    for movie in data:
        revenue = float(movie['Revenue (Millions)']) if movie['Revenue (Millions)'] else 0
        actors = movie['Actors'].split(', ')
        for actor in actors:
            actors_revenue[actor] += revenue
    highest_revenue_actor = max(actors_revenue, key=actors_revenue.get)
    print(f"3.The actor generating the highest total revenue: {highest_revenue_actor}")

#Q4
def Q4(data):
    ratings = [float(movie['Rating']) for movie in data if 'Emma Watson' in movie['Actors']]
    avg_rating = sum(ratings) / len(ratings) if ratings else 0
    print(f"4.The average rating of Emma Watson’s movies: {avg_rating}")

#Q5
def Q5(data):
    actors_movies = defaultdict(int)
    for movie in data:
        actors = movie['Actors'].split(', ')
        for actor in actors:
            actors_movies[actor] += 1
    top_4_actors = sorted(actors_movies.items(), key=lambda x: x[1], reverse=True)[:4]
    print("5.Top-4 actors playing the most movies:")
    for i, (actor, count) in enumerate(top_4_actors, 1):
        print(f"\tTop {i}: {actor} with {count} movies")

#Q6
def Q6(data):
    collaborations = defaultdict(int)
    for movie in data:
        director = movie['Director']
        actors = movie['Actors'].split(', ')
        for actor in actors:
            collaborations[(director, actor)] += 1
    top_7_collaborations = sorted(collaborations.items(), key=lambda x: x[1], reverse=True)[:7]
    print("6.Top-7 frequent collaboration pairs of director & actor:")
    for i, ((director, actor), count) in enumerate(top_7_collaborations, 1):
        print(f"\tTop {i}: Director {director} and Actor {actor} with {count} collaborations")

#Q7
def Q7(data):
    director_actors = defaultdict(set)
    for movie in data:
        director = movie['Director']
        actors = movie['Actors'].split(', ')
        for actor in actors:
            director_actors[director].add(actor)
    top_3_directors = sorted(director_actors.items(), key=lambda x: len(x[1]), reverse=True)[:3]
    print("7.Top-3 directors who collaborate with the most actors:")
    for i, (director, actors) in enumerate(top_3_directors, 1):
        print(f"\tTop {i}: {director} with {len(actors)} actors")

#Q8
def Q8(data):
    actor_genres = defaultdict(set)
    for movie in data:
        genres = movie['Genre'].split(', ')
        actors = movie['Actors'].split(', ')
        for actor in actors:
            for genre in genres:
                actor_genres[actor].add(genre)
    top_6_actors = sorted(actor_genres.items(), key=lambda x: len(x[1]), reverse=True)[:6]
    print("8.Top-6 actors playing in the most genres of movies:")
    for i, (actor, genres) in enumerate(top_6_actors, 1):
        print(f"\tTop {i}: {actor} in {len(genres)} genres")

#Q9
def Q9(data):
    actor_years = defaultdict(list)
    for movie in data:
        year = int(movie['Year'])
        actors = movie['Actors'].split(', ')
        for actor in actors:
            actor_years[actor].append(year)
    actor_gaps = {actor: max(years) - min(years) for actor, years in actor_years.items() if len(years) > 1}
    top_3_gaps = sorted(actor_gaps.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Top-3 actors whose movies lead to the largest maximum gap of years:")
    for i, (actor, gap) in enumerate(top_3_gaps, 1):
        print(f"Top {i}: {actor} with a gap of {gap} years")

# 打開檔案，將資料存起來，再跑完所有問題
with open("IMDB-Movie-Data.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
for i in range(9):
    i+=1
    func_name = f"Q{i}"
    globals()[func_name](data)

