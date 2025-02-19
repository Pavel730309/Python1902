import random

def get_user_choice():
    user_input = input("Выберите камень, ножницы или бумагу: ").lower()
    while user_input not in ['камень', 'ножницы', 'бумага']:
        print("Неверный ввод. Попробуйте еще раз.")
        user_input = input("Выберите камень, ножницы или бумага: ").lower()
    return user_input

def get_computer_choice():
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "ничья"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return "пользователь"
    else:
        return "компьютер"

def play_game():
    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "пользователь":
            print("Вы выиграли этот раунд!")
            user_score += 1
        elif winner == "компьютер":
            print("Компьютер выиграл этот раунд!")
            computer_score += 1
        else:
            print("Этот раунд в ничью!")

        print(f"Счет: Вы - {user_score}, Компьютер - {computer_score}\n")

    if user_score == 3:
        print("Поздравляем! Вы победили!")
    else:
        print("Компьютер победил. Попробуйте снова!")

if __name__ == "__main__":
    play_game()