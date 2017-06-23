
# ord('B') - 64 --help for you
# Text file(p22_names.txt) containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth
# 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
# obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?
names = []
with open('p22_names.txt') as f:
    for line in f:
        names.append([i for i in line.split(",")])

names = names[0]
names = sorted(names)
namescores = 0
name_score = 0
for i in range(len(names)):
    for j in names[i]:
        name_score += int(ord(j)) - 64
    namescores += ((name_score + 60) * (i + 1))
    name_score = 0

print(namescores)

