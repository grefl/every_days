LEVENSHTEIN_MODE = True 

def check_word_levenshtein(words: [str, str]) -> str:
    word1, word2 = words
    matrix = [[0 for _ in range(len(word2))] for _ in range(len(word1))]
    for i in range(len(matrix[0])):
            matrix[0][i] = i 
    for i in range(len(matrix)):
            matrix[i][0] = i 
    for i in range(1,len(word1)):
        for j in range(1,len(word2)):
            cost = 1 
            if word1[i-1] == word2[j-1]:
                cost = 0 
            matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + cost)

    return matrix[-1][-1]

def check_word(words: [str, str]) -> str:
    word1, word2 = words
    matrix = [[0 for _ in range(len(word2))] for _ in range(len(word1))]
    for i in range(0,len(word1)):
        for j in range(0,len(word2)):
            if word1[i] == word2[j]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    return matrix[-1][-1]

def spell_checker(word, words):
    best_match = [float('inf'), None]
    for word_to_check in words:
        match_rating = None
        if LEVENSHTEIN_MODE:
            match_rating = check_word_levenshtein([word, word_to_check])
            if best_match[0] > match_rating: 
                best_match[0] = match_rating
                best_match[1] = word_to_check
        else:
            exit(0)
            match_rating = check_word([word, word_to_check])
            if best_match[0] < match_rating: 
                best_match[0] = match_rating
                best_match[1] = word_to_check

    return best_match[1]

def main():
    words = ['fort', 'bosh', 'resveratrol', 'fishing', 'kissing', 'wishing', 'fish', 'duck', 'luck', 'valadimir levenshtein', 'harry', 'twitter', 'putin']
    word = 'vladimir levenshstein'
    best_match = spell_checker(word, words)
    print(best_match)


if __name__ == "__main__":
    main()
