def sort_on(dict):
     return dict["num"]

def main ():
     
    char = {}
    words = []
    wordcount = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split ()
        for word in words:
            wordcount += 1
        file_contents = file_contents.lower()
        for letter in file_contents:
            if letter in char:
               char[letter] += 1
            else:
                char[letter] = 1

    char_list = []
    for letter, num in char.items():
        if letter.isalpha() == True:
            char_list.append({"letter": letter, "num": num})

    char_list.sort (reverse=True, key=sort_on)

    print ("--- Begin report of books/frankenstein.txt ---")
    print (f"{wordcount} words found in the document")
    print ()
    for char_dict in char_list:
        print (f"The '{char_dict['letter']}' character was found {char_dict['num']} times")
    print ("--- End report ---")
main ()