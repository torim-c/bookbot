def word_counter(filecontents):
    list_of_words = filecontents.split()
    return len(list_of_words)

def char_counter(filecontents):
    indiv_counter = {}
    for char in filecontents:
        char = char.lower()
        if char in indiv_counter:
            indiv_counter[char] += 1
        else:
            indiv_counter[char] = 1
    return indiv_counter #{'t': 29493, 'h': 19176, 'e': 44538, ' ': 70480, 'p': 5952} etc

def sort_on(items):
    return items ["num"]

def freq_sorter(filecontents):
    list_tuple = [] 
    list_tuple = filecontents.items()
    list_to_sort = []
    for x, y in list_tuple:
        list_to_sort.append({"char": x, "num": y})
    list_to_sort.sort(reverse = True, key=sort_on)
    return list_to_sort


def print_sorted(list_to_sort):
    for pairs in list_to_sort:
        if pairs["char"].isalpha() and pairs["char"].isascii():
            print(f"{pairs['char']}: {pairs['num']}") # \n adds extra blank lines, not needed