# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as file:
        return file.read()


def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    split_text = text.split()
    text_freq = dict()

    for word in split_text:
        if word in text_freq:
            text_freq[word] = text_freq[word] + 1
        else:
            text_freq[word] = 1
    
    return text_freq


#test code
print(count_words())

#@George Akor
#theStormGod

