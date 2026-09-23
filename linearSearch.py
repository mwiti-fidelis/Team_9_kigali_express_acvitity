from clean_data import remove_duplicates

def linear_search(target):
    sortedArray= remove_duplicates()
    for name in sortedArray:
        if name == target:
            target_index = sortedArray.index(name)
            return target_index

    return -1


print(linear_search("Liliane Mugabo"))
