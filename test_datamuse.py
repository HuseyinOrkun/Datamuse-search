import datamuse

def test_clue(clue, length, answer):

    len = ""
    for i in range(length) :
        len += '?'

    guess = datamuse.search_datamuse_wordenp(clue, max_res=10, sp=len)

    guessList = []

    for el in guess:
        guessList.append(el["word"].lower())

    return answer.lower() in guessList


def test_all(data):

    # first column is clue, second column is length, third cloumn is answer

    for row in data:
        row.append(test_clue(row[0], row[1], row[2]))

    return data


data = [["Seasoning on an everything bagel", 4, "salt"],["Veggie bit on an everything bagel", 5, "Onion"], ["Seed on an everything bagel", 5, "Poppy"]]
print(test_all(data))