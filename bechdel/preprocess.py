import csv
# mv = open("movies.csv")
# for test in mv:
#     test = test.split(",")
#     print(test[0])
with open("movies.csv") as csvfile:
    reader = csv.reader(open('movies.csv', 'rU'), dialect=csv.excel_tab)
    with open("processed_movies.csv", 'wb') as results:
        writer = csv.writer(results)
        for row in reader:
            row = row[0].split(",")
            att = []
            for a in row:
                if a != '':
                    att.append(a)
                else:
                    att.append('?')
            if len(att) == 15:
                writer.writerow(att)
