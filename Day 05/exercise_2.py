def distinct_letter(word):
    distinct = list(dict.fromkeys(word))
    distinct.sort()
    return distinct


print(distinct_letter('entretenido'))
