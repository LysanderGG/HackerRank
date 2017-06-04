#!/bin/python3
import sys
import itertools


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
   topic_t = str(input().strip())
   topic.append(topic_t)

team_topics = [int(a, 2) | int(b, 2) for (a, b) in itertools.combinations(topic, 2)]
max_topics = max([bin(t).count("1") for t in team_topics])
nb_teams = sum([bin(t).count("1") == max_topics for t in team_topics])

print(max_topics)
print(nb_teams)