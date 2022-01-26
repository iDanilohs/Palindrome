def palindrome(word):
    word = word.replace(" ", "").lower()
    inverse = word[::-1]
    if word == inverse:
        return True
    else:
        return False

def run():
    word = input("Pasame una palabra: ")
    word_is_palindrome = palindrome(word)
    if word_is_palindrome == True:
        print(f'{word} es un palíndromo.')
    else:
        print(f'{word} no es un palíndromo.')


if __name__ == '__main__':
    run()