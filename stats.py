def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    text = text.lower()
    char_count_dict = {char: text.count(char) for char in set(text)}
    return {char: count for char, count in char_count_dict.items() if char.isalpha()}

"""
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
"""
# Sort the character count dictionary by frequency in descending order
def char_sort(char_count_dict):
    return dict(sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True))