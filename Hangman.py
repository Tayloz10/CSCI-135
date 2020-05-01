import random
print("Welcome to hangman")
play = "y"
answers = ["PYTHON", "RUBY", "JAVASCRIPT", "JAVA", "COBOL", "SWIFT", "KOTLIN"]
j = 0
n = 0
while play == "y":
    input_x = []
    m = random.randint(0,6)
    answers_h = answers[m]
    print("Pick letter #{}" .format(j+1))
    input_x.append(input())
    list_1 = list(answers_h)
    while n <= 6:
        k = 0
        while k < len(list_1):
            if input_x[j] == list_1[k]:
                print("You guess was right")
                k = (len(list_1)-1)
                if n == 0:
                    n = 0
                else:
                    n -= 1
            elif k == len(list_1) - 1:
                print("Guess Agian")
                k += 1
            else:
                k += 1
        print(input_x)
        print("Guess {} was {}" .format(j + 1, input_x[j]))
        j += 1
        n + 1
    play = input("Play agian (y/n)")


