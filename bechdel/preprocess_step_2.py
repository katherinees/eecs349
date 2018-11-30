import csv
import random

with open('PreprocessedMovies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    with open('train.csv', 'wb') as train:
        writer = csv.writer(train)
        with open('test.csv', 'wb') as test:
            testwriter = csv.writer(test)
            # writer.writerow(['year', 'imdb', 'title', 'binary', 'budget', 'domgross', 'intgross', 'budget_2013$', 'domgross_2013$', 'intgross_2013$'])
            # testwriter.writerow(['year', 'imdb', 'title', 'binary', 'budget', 'domgross', 'intgross', 'budget_2013$', 'domgross_2013$', 'intgross_2013$'])
            for row in reader:
                att = [row['year'], row['binary'], row['budget'], row['domgross'], row['intgross']]
                if "#N/A" not in att:
                    x = random.random()
                    if x > 0.7:
                        testwriter.writerow(att)
                    else:
                        writer.writerow(att)
