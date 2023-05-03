def is_palindrome_recursive(word, low_index, high_index):
    print("call")
    if not len(word):
        return False
    if low_index >= high_index or word[low_index] != word[high_index]:
        return False
    if word[low_index] == word[high_index]:
        low_index += 1
        high_index -= 1
        is_palindrome_recursive(word, low_index, high_index)


print(is_palindrome_recursive("agua", 0, 3))
