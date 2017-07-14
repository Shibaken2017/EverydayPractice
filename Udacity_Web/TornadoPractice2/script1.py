def map_by_first_letter(text):
    mapped = dict()
    for line in text.split("\r\n"):
        for word in [x for x in line.split(' ') if len(x) > 0]:
            if word[0] not in mapped:
                mapped[word[0]] = []
            mapped[word[0]].append(word)
    return mapped


print map_by_first_letter("aiueok akikukeko sasisus sasi soviet udon utubyou")