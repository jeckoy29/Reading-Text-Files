# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as f:
        text = f.read()
    return text


def count_words():
    text = read_file_content("./story.txt")
    stored_text=text.split()
    word_counter = dict()
    for x in stored_text:
        try:
            word_counter[x] += 1
        except:
            word_counter[x] = 1
    return word_counter

print(count_words())