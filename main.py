def get_file_content(path):
    with open(path) as file:
        content = file.read()
    return content

def get_counts_of_words(content):
    return len(content.split())

def get_counts_of_character(content):
    lcontent = content.lower()
    char_dict = {}

    for char in lcontent:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
            
    return char_dict

def main():
    from pathlib import Path
    fpath = Path('/home/omona/workspace/github.com/OMONa-E/bookbot/books/frankenstein.txt')
    content = get_file_content(fpath)
    print(f'--- Begin report of books/frankenstein.txt ---')
    print(f'{get_counts_of_words(content)} words found in the document')
    dict_cont = get_counts_of_character(content)

    for k,v in dict_cont.items():
        print(f"The '{k}' character was found {v} times")
    print(f'--- End report ---')


main()