#Tìm từ dài nhất trong một xâu, các từ cách nhau bởi một dấu cách
def longest_substring(string):
    sub_strings = string.split()
    longest = ""
    for sub in sub_strings:
        if len(sub) > len(longest):
            longest = sub
    return longest
string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
print("Tu dai nhat trong chuoi la: " + longest_substring(string))