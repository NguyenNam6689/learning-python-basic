# Viết một hàm để đếm số lần xuất hiện của một từ trong chuỗi nhập vào từ bàn phím
def count_word_occurrences(string, word):
    count = 0
    words = string.split()
    for w in words:
        if w == word:
            count += 1
    return count

input_string = input("Enter a string: ")
word_to_count = input("Enter a word to count: ")

occurrences = count_word_occurrences(input_string, word_to_count)
print("Number of occurrences:", occurrences)