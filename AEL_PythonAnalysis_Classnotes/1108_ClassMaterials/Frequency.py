# © Chung-Ang University 2024 (응용영어학탐색)


import os
import pathlib
import re

directory_name ='C:\\Users\\jordi\\Downloads\\Python'
data_files = pathlib.Path(directory_name).glob("*.txt")

frequency = {}
for file in data_files:
    get_file = open(file, 'r')
    text = get_file.read().lower()
    match_pattern = re.findall(r'\b[a-z]+\b', text)
    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1

word_list = frequency.keys()
for word in word_list:
    print(word, frequency[word])
    
savename = os.path.join(directory_name, 'Output.csv')

f = open(savename, 'w')
for word in frequency.keys():
    f.write('%s,%d\n'%(word,frequency[word]))
f.close()
