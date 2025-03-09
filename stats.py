def get_text(string):
    with open(string) as f:
        return f.read()

def get_num_words(string):
    words = get_text(string)
    return len(words.split())

#takes the text from a book as a string
#returns the number of times each characters (including symbols and spaces
#appear)
#convert any character to lower
#use a dictionary of string -> integer
def character_count(text):
    char_count = {} 
    for char in text:
        c_lower_case = char.lower()
        if c_lower_case in char_count:
            char_count[c_lower_case] += 1
        else:
            char_count[c_lower_case] = 1
    return char_count

#takes in a dictionary of characters and their counts
#sort from greatest to least by the count:
#if character is non alphabetical, skip
#capture in main and print the report
def sort_on(d):
    return d["num"]

def sorted_list(dictionary):
    dict_list = []
    for char in dictionary:
        dict_list.append({"char": char, "num": dictionary[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
