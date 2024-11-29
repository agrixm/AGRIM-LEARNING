import re

# Sample text
text = "The rain in Spain falls mainly in the plain."

# findall: Find all occurrences of a pattern
pattern = r'\bin\b'
findall_result = re.findall(pattern, text)
print("findall result:", findall_result)

# match: Check if the pattern matches at the beginning of the string
pattern = r'The'
match_result = re.match(pattern, text)
if match_result:
    print("match result:", match_result.group())
else:
    print("match result: No match")

# search: Search for the first occurrence of the pattern
pattern = r'Spain'
search_result = re.search(pattern, text)
if search_result:
    print("search result:", search_result.group())
else:
    print("search result: No match")