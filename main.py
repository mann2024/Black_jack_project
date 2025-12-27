import random
from art import logo

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
you = []
comp = []

def play_game(n1 = int(random.choice(cards)), n2 = int(random.choice(cards))):
    print(logo)
    you.clear()
    comp.clear()
    you.append(n1)
    you.append(n2)
    t1 = int(random.choice(cards))
    comp.append(t1)

    sum1 = n1 + n2
    sum2 = t1
    get_another_card = True

    while(get_another_card):
        print(f"Your cards: {you}, current score: {sum1}")
        print(f"Computer's first card: {sum2}")

        choice1 = input("Type 'y' to get another card, type 'n' to pass: ")
        if(choice1 == 'y'):
            temp = int(random.choice(cards))
            sum1 += temp
            if(temp == 11):
                if(sum1 > 21):
                    sum1 -= 10
                    temp = 1
            you.append((temp))
            if(sum1 > 21):
                break

        elif(choice1 == 'n'):
            break
        else:
            print("Please enter a valid choice.")

    while(sum2 < 16):
        temp1 = int(random.choice(cards))
        sum2 += temp1
        if (temp1 == 11):
            if (sum2 > 21):
                sum2 -= 10
                temp1 = 1
        comp.append(temp1)
        if (sum2 > 21):
            break

    print(f"Your final hand: {you}, final score: {sum1}")
    print(f"Computer's final hand: {comp}, final score: {sum2}")
    if(sum1 > 21):
        print("You went over. You lose 😭")
        choice2 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if (choice2 == "y"):
            print("\n" * 10)
            play_game(n1=int(random.choice(cards)), n2=int(random.choice(cards)))
        else:
            exit()

    if(sum2 > 21):
        print("Opponent went over. You win 😁")
        choice2 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if (choice2 == "y"):
            print("\n" * 10)
            play_game(n1=int(random.choice(cards)), n2=int(random.choice(cards)))
        else:
            exit()

    if(sum1 > sum2):
        print("You Won!")
    elif(sum1 < sum2):
        print("You loose!")
    else:
        print("Draw 🙃")


    choice2 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if(choice2 == "y"):
        print("\n" * 10)
        play_game(n1 = int(random.choice(cards)), n2 = int(random.choice(cards)))
    else:
        exit()





play_game()