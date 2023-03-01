import random
VISELICA = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |      
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
      ===''']
words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()
def getRandomWord(wordList):
    # Эта функция возвращает случайную строку из списка
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(VISELICA[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        # Заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:
        # Показывает секретное слово с пробелами между буквами
        print(letter, end=' ')
    print()
def getGuess(alreadyGuessed):
    #Возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну и букву и ничего больше.
    while True:
        print('Введите букву')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Слишком много букв, введите только одну')
        elif guess in alreadyGuessed:
            print('Эта буква уже была, назовите другую')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Это не буква, попробуйте ещё раз')
        else:
            return guess
def playAgain():
    #Эта функция возвращает значение True, если игрок хочет сыграть заново; в противном случае возвращает False
    print('Хотите сыграть еще раз? (да или нет)')
    return input().lower().startswith('да')
print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False
while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Позволяет игроку ввести букву
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Проверяет, выиграл ли игрок
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('----------------------------------------------------')
            print('Да!!! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Проверяет, превысил ли  игрок лимит попыток и програл
        if len(missedLetters) == len(VISELICA) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('----------------------------------------------------')
            print('Вы исчерпали все попытки!')
            print('Не угадано букв: ' + str(len(missedLetters)) + ' и угадано букв: ' + str(len(correctLetters)))
            print('Было загадано слово - ' + secretWord)
            gameIsDone = True
            # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена)
            if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord = getRandomWord(words)
            else:
                break