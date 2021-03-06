authors = [
    ['Тагирова Наиля Фаридовна', 'ФГБОУ ВО «СГЭУ», Кафедра философии и истории, профессор'],
    ['Сумбурова Елена Ивановна', 'ФГБОУ ВО «СГЭУ», Кафедра философии и истории, доцент'],
    ['Соленцова Елена Алексеевна', 'ФГБОУ ВО «СГЭУ», Кафедра философии и истории, доцент'],
    ['Солдатова Ольга Евгеньевна', 'ФГБОУ ВО «СГЭУ», Музей истории , директор'],
    ['Семенова Екатерина Юрьевна', 'ФГБОУ ВО «Самарский государственный технический университет», '
                                   'Кафедра «Социология, политология и история Отечества», профессор'],
    ['Жердева Юлия Александровна', 'НИУ ВО «Самарский национальный исследовательский университет», '
                                   'Кафедра документоведения, профессор'],
]


def author_short():
    author_list = ""
    for author in authors:
        names = author[0].split(" ")
        author_list += names[0] + " " + names[1][0] + "." + names[2][0] + "., "
    return author_list[0:len(author_list)-2]


print(author_short())