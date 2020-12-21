def check_word(word):
    for num in range(1, len(word) + 1):
        if word[:num] in wordDict:
            if len(word) == len(s):
                sentences.append("separator")
            sentences.append(word[:num])
            check_word(word[num:])


def check_move(rows, cols, letter_position):
    global output2
    char = board[rows][cols]
    if char == word2[letter_position] and output2 != word2:
        output2 += char
        if char == word2[letter_position] and output2 == word2:
            result2.append(output2)
            output2 = ""
            return True
    else:
        # terminate wrong moves
        return False
    if rows < len(board) - 1:
        check_move(rows + 1, cols, letter_position + 1)
    if rows > 0:
        check_move(rows - 1, cols, letter_position + 1)
    if cols < len(board[0]) - 1:
        check_move(rows, cols + 1, letter_position + 1)
    if cols > 0:
        check_move(rows, cols - 1, letter_position + 1)


if __name__ == '__main__':
    # Cau 1
    s = "catsanddogxyz"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    sentences = []
    output = []
    check_word(s)
    string_sentences = " ".join(sentences[1:]).split("separator")
    string_sentences = map(lambda x: x.strip(), string_sentences)
    for n in string_sentences:
        output.append(n)
    print(output)

    # Cau 2
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    output2 = ""
    result2 = []
    for word2 in words:
        for row in range(len(board)):
            for col in range(len(board[0])):
                output2 = ""
                check_move(row, col, 0)
    print(result2)
