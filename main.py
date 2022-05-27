# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string
from this import d
def read_file_content(filename):
    file1 = open("story.txt","r")
    
    return file1


def count_words():
    text = read_file_content("F:\2022 code file\Zuri+internship+tasks+2022\task8+reading+text+file\Reading-Text-Files\story.txt")
    d = dict()
    for line in text:
        line = line.strip()
        words = line.split()
        

    for word in words:
        if word in d:
            d[word] = 0
            d[word] = d[word] +1 
        else:
            d[word] = 1

    return d
print(count_words())
