import requests
import pprint
import csv
import random
# params = {'imdbid': 'tt1727824'}
# base_url = 'http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid='
# imdbid = '1727824'
#
# omdb_api = '9d964e85'

url = 'http://www.omdbapi.com/?i=tt0059183&apikey=9d964e85'

# response = requests.get(url)
# data = response.json()
# pprint.pprint(data)

# Country, Plot, Production, Rated, Genre, Writer, Director, imdbRating

import os

# girl_names = set()
# boy_names = set()

fem_words = ['she', 'her', 'hers', 'woman', 'women', 'girl', 'mother', 'daughter', 'wife']

with open('ctrain.csv') as train:
    reader = csv.DictReader(train)
    director_stat = {'F, pass':0, 'M, pass':0, 'F, fail':0, 'M, fail':0}
    for row in reader:
        if row['Director'] == 'F':
            if row['class'] == 'P':
                director_stat['F, pass'] += 1
            else:
                director_stat['F, fail'] += 1
        else:
            if row['class'] == 'P':
                director_stat['M, pass'] += 1
            else:
                director_stat['M, fail'] += 1
    print(director_stat)

# with open('secondpass.csv') as secondpass:
#     reader = csv.DictReader(secondpass)
#     with open('ctrain.csv', 'w') as train:
#         train_w = csv.writer(train)
#         with open('ctest.csv', 'w') as test:
#             test_w = csv.writer(test)
#             train_w.writerow(['title', 'imdbid', 'year', 'class', 'Country', 'Fem Wordcount', 'Production', 'Rated', 'Genre', 'Writers F', 'Writers M', 'Director', 'imdbRating'])
#             test_w.writerow(['title', 'imdbid', 'year', 'class', 'Country', 'Fem Wordcount', 'Production', 'Rated', 'Genre', 'Writers F', 'Writers M', 'Director', 'imdbRating'])
#
#             for row in reader:
#                 if row['class'] == 'P':
#                     x = random.random()
#                     if x < 0.1472:
#                         y = random.random()
#                         if y < 0.7:
#                             train_w.writerow(row.values())
#                         else:
#                             test_w.writerow(row.values())
#                 else:
#                     z = random.random()
#                     if z < 0.7:
#                         train_w.writerow(row.values())
#                     else:
#                         test_w.writerow(row.values())

# with open('secondpass.csv') as secondpass:
#     reader = csv.DictReader(secondpass)
#     with open('btrain.csv', 'w') as train:
#         train_w = csv.writer(train)
#         with open('btest.csv', 'w') as test:
#             test_w = csv.writer(test)
#             train_w.writerow(['title', 'imdbid', 'year', 'class', 'Country', 'Fem Wordcount', 'Production', 'Rated', 'Genre', 'Writers F', 'Writers M', 'Director', 'imdbRating'])
#             test_w.writerow(['title', 'imdbid', 'year', 'class', 'Country', 'Fem Wordcount', 'Production', 'Rated', 'Genre', 'Writers F', 'Writers M', 'Director', 'imdbRating'])
#             for row in reader:
#                 x = random.random()
#                 if x > 0.7:
#                     test_w.writerow(row.values())
#                 else:
#                     train_w.writerow(row.values())

# with open('cleaner.csv') as clean:
#     reader = csv.DictReader(clean)
#     with open('secondpass.csv', 'w') as secondpass:
#         writer = csv.writer(secondpass)
#         writer.writerow(['title', 'imdbid', 'year', 'class', 'Country', 'Fem Wordcount', 'Production', 'Rated', 'Genre', 'Writers F', 'Writers M', 'Director', 'imdbRating'])
#         for row in reader:
#             if (row['rating'] == '0') or (row['rating'] == '3'):
#                 if row['rating'] == '0':
#                     bech_rate = 'F'
#                 else:
#                     bech_rate = 'P'
#                 fem_count = 0
#                 preprocess_plot = row['Plot'].lower().replace('.', '').replace("'", ' ').replace(',', '')
#                 preprocess_plot = preprocess_plot.split(' ')
#                 for w in fem_words:
#                     fem_count += preprocess_plot.count(w)
#                 if row['imdbRating'] == 'N/A':
#                     imdb_rating = None
#                 else:
#                     imdb_rating = float(row['imdbRating'])
#                 writer.writerow([row['title'].replace("'", ''), row['imdbid'], int(row['year']), bech_rate, row['Country'], fem_count, row['Production'].replace("'", ''), row['Rated'], row['Genre'], int(row['Writers F']), int(row['Writers M']), row['Director'], imdb_rating])

# directory = 'names'
# for f in os.listdir(directory):
#     path = directory + "/" + f
#     yob = open(path, "r")
#     for line in yob:
#         line = line.split(",")
#         if line[1] == "F":
#             girl_names.add(line[0]+'&')
#         else:
#             boy_names.add(line[0]+'&')
# with open('girl_names.txt', 'w') as f:
#     for n in girl_names:
#         f.write(n)
#         f.write(', ')
#
# with open('boy_names.txt', 'w') as b:
#     for n in boy_names:
#         b.write(n)
#         b.write(', ')

# with open('cleaner.csv') as okay:
#     reader = csv.DictReader(okay)
#     with open('firstpass.csv', 'w') as results:
#         writer = csv.writer(results)
#         writer.writerow(['imdbid', 'year', 'binary', 'Country', 'Production', 'Rated', 'Genre', 'Writers F', 'Writers M', 'Director'])#, 'imdbRating'])
#         for row in reader:
#             if row['binary'] == '1':
#                 binary = 'T'
#             else:
#                 binary = 'F'
#             writer.writerow([row['imdbid'], int(row['year']), binary, row['Country'], row['Production'].replace("'", ''), row['Rated'], row['Genre'], int(row['Writers F']), int(row['Writers M']), row['Director']]) #, float(row['imdbRating'])])

# with open('boy_names.csv') as boys:
#     reader = csv.reader(boys)
#     for row in reader:
#         boy_names.add(row[1].replace('"', ''))
# with open('girl_names.csv') as girls:
#     reader = csv.reader(girls)
#     for row in reader:
#         girl_names.add(row[1].replace('"', ''))
# with open('girl_names.txt', 'w') as f:
#     for n in girl_names:
#         f.write(n)
#         f.write(', ')
#
# with open('boy_names.txt', 'w') as b:
#     for n in boy_names:
#         b.write(n)
#         b.write(', ')
# print(girl_names)
# with open('raw_omdb_all.csv') as raw:
#     reader = csv.DictReader(raw)
#     with open('cleaner.csv', 'w') as results:
#         writer = csv.writer(results)
#         writer.writerow(['title', 'imdbid', 'year', 'rating', 'binary', 'Country', 'Plot', 'Production', 'Rated', 'Genre', 'Writers F', 'Writers M', 'Director', 'imdbRating'])
#         for row in reader:
#             country = row['Country'].split(',')[0]
#             genre = row['Genre'].split(',')[0]
#             all_writers = row['Writer'].split(',')
#             firsts = []
#             wf = 0
#             wm = 0
#             for w in all_writers:
#                 firsts.append(w.strip().split(' ')[0])
#             for f in firsts:
#                 if f in girl_names:
#                     wf += 1
#                 if f in boy_names:
#                     wm += 1
#             director_name = row['Director'].split(' ')[0]
#             if director_name in girl_names:
#                 director_likely_gender = 'F'
#             else:
#                 director_likely_gender = 'M'
#             writer.writerow([row['title'], row['imdbid'], row['year'], row['rating'], row['binary'], country, row['Plot'], row['Production'], row['Rated'], genre, wf, wm, director_likely_gender, row["imdbRating"]])

# with open('better_ii.csv') as old:
#     reader = csv.DictReader(old)
#     with open('raw_omdb.csv', 'w') as results:
#         writer = csv.writer(results)
#         writer.writerow(['title', 'imdbid', 'year', 'rating', 'binary', 'Country', 'Plot', 'Production', 'Rated', 'Genre', 'Writer', 'Director', 'imdbRating'])
#         for row in reader:
#             url = 'http://www.omdbapi.com/?i=' + row['imdbid'] + '&apikey=9d964e85'
#             response = requests.get(url)
#             data = response.json()
#             if data['Response'] == 'True':
#                 if 'Country' in data:
#                     country = data['Country']
#                 else:
#                     country = ''
#                 if 'Plot' in data:
#                     plot = data['Plot']
#                 else:
#                     plot = ''
#                 if 'Rated' in data:
#                     rated = data['Rated']
#                 else:
#                     rated = ''
#                 if 'Genre' in data:
#                     genre = data['Genre']
#                 else:
#                     genre = ''
#                 if 'Writer' in data:
#                     writers = data['Writer']
#                 else:
#                     writers = ''
#                 if 'Production' in data:
#                     prod = data['Production']
#                 else:
#                     prod = ''
#                 if 'Director' in data:
#                     director = data['Director']
#                 else:
#                     director = ''
#
#                 writer.writerow([row['title'], row['imdbid'], row['year'], row['rating'], row['binary'], country, plot, prod, rated, genre, writers, director, data['imdbRating']])


# with open('bech_copy.csv') as old:
#     reader = csv.DictReader(old)
#     with open('better.csv', 'w') as results:
#         writer = csv.writer(results)
#         writer.writerow(['title', 'imdbid', 'year', 'rating', 'binary'])
#         for row in reader:
#             if int(row['year']) >= 1960:
#                 imdb = 'tt' + row['imdbid']
#                 writer.writerow([row['title'], imdb, row['year'], row['rating'], row['binary']])


# with open('bech.csv', 'w') as results:
#     writer = csv.writer(results)
#     writer.writerow(['title', 'imdbid', 'year', 'rating', 'binary'])
#     url = 'http://bechdeltest.com/api/v1/getAllMovies'#base_url + imdbid
#     response = requests.get(url)
#     data = response.json()
#     for movie in data:
#         res = [movie['title'], movie['imdbid'], movie['year'], movie['rating']]
#         if movie['rating'] == '3':
#             binary = 1
#         else:
#             binary = 0
#         res.append(binary)
#         writer.writerow(res)
