def single_root_words(root_word, *other_words):
    same_words = []
    count = 0
    for word in other_words:
        if root_word in word in other_words:
            same_words.append(word)

    return same_words


result1 = single_root_words('умный', 'самый умный', 'заумный', 'ура', 'умненькие')
print(result1)
result2 = single_root_words('дождь', 'дождливый', 'телефон', 'дождик', 'персик')
print(result2)


result3 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result4 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result3)
print(result4)


