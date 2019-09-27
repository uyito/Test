def is_pal(word):
    if len(word)==0 or len(word)==1:
        return True
    return word[0] == word[-1] and is_pal(word[1:len(word)-1])




text = "momom"

print(is_pal(text))