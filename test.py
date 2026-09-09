def count_words(s):
    s=s.split()
    count=0
    for word in s:
        count+=1
    return count
print(count_words("One two three four, five SIX seven two eight nine ten TEN."))