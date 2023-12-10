import sqlite3
import itertools

conn = sqlite3.connect('task1.sqlite')
cursor = conn.cursor()

cursor.execute('''
    SELECT film_title, actors
    FROM actor_films
''')

data = cursor.fetchall()

actor_pairs = []
for entry in data:
    actors = entry[1].split(', ')
    pairs = list(itertools.combinations(actors, 2))
    actor_pairs.extend(pairs)


pair_counts = {}
for pair in actor_pairs:
    pair = tuple(sorted(pair))
    if pair in pair_counts:
        pair_counts[pair] += 1
    else:
        pair_counts[pair] = 1


most_frequent_pair = max(pair_counts, key=pair_counts.get)
appearance_count = pair_counts[most_frequent_pair]

print("Самая частая пара актеров:", most_frequent_pair, "кол-во появленй:", appearance_count)

conn.close()