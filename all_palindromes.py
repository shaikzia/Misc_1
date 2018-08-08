class User(object):
    def all_palindromes(cls, text):
        results = set()
        text_length = len(text)

        for idx, char in enumerate(text):
            start, end = idx - 1, idx + 1
            while start >= 0 and end < text_length and text[start] == text[end]:
                results.add(text[start:end + 1])
                start -= 1
                end += 1

            # Check for longest even palindrome(s)
            start, end = idx, idx + 1
            while start >= 0 and end < text_length and text[start] == text[end]:
                results.add(text[start:end + 1])
                start -= 1
                end += 1

        return results

# Removed the comments - updated the comments now at 2138
c = User()
res = c.all_palindromes('malayalam')
print(res)