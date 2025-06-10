import random
import time

emojis = ['🍒', '🍋', '🍉', '🍇', '💎', '🪙', '🍎']

money = int(input("Баланс- "))

if money <= 1:
    print("Твърде си беден💸")
    exit()

while money > 0:
    print(f"You have ${money}")
    
    bet = int(input("Залог- "))
    
    if bet <= 1 or bet > money:
        print("Нещо се обърка. Опитай отново по късно.")

    for i in range(20):
        spin = [random.choice(emojis) for i in range(5)]
        print(' '.join(spin), end='\r')
        time.sleep(0.1)

    final_spin = [random.choice(emojis) for i in range(5)]
    print("Final result:", final_spin)

    if final_spin[0] == final_spin[1] == final_spin[2] == final_spin[3] == final_spin[4]:
        winnings = bet * 2
        print(f"🪙Jackpot🪙 You win ${winnings}")
    elif (final_spin[0] == final_spin[1] == final_spin[2] == final_spin[3] or
          final_spin[0] == final_spin[1] == final_spin[2] == final_spin[4] or
          final_spin[0] == final_spin[1] == final_spin[3] == final_spin[4] or
          final_spin[0] == final_spin[2] == final_spin[3] == final_spin[4] or
          final_spin[1] == final_spin[2] == final_spin[3] == final_spin[4]):
        winnings = bet * 1.5
        print(f"4 Еднакви!🥳 You win ${winnings}")
    elif (final_spin[0] == final_spin[1] == final_spin[2] or
          final_spin[0] == final_spin[1] == final_spin[3] or
          final_spin[0] == final_spin[1] == final_spin[4] or
          final_spin[0] == final_spin[2] == final_spin[3] or
          final_spin[0] == final_spin[2] == final_spin[4] or
          final_spin[0] == final_spin[3] == final_spin[4] or
          final_spin[1] == final_spin[2] == final_spin[3] or
          final_spin[1] == final_spin[2] == final_spin[4] or
          final_spin[1] == final_spin[3] == final_spin[4] or
          final_spin[2] == final_spin[3] == final_spin[4]):
        winnings = bet * 1.3
        print(f"3 Еднакви!🎉 You win ${winnings}")
    elif (final_spin[0] == final_spin[1] or
          final_spin[0] == final_spin[2] or
          final_spin[0] == final_spin[3] or
          final_spin[0] == final_spin[4] or
          final_spin[1] == final_spin[2] or
          final_spin[1] == final_spin[3] or
          final_spin[1] == final_spin[4] or
          final_spin[2] == final_spin[3] or
          final_spin[2] == final_spin[4] or
          final_spin[3] == final_spin[4]):
        winnings = bet * 1.1
        print(f"2 Еднакви!🎊 You win ${winnings}")
    else:
        print("😞За това не се играе хазарт😞")
        winnings = 0

    money += winnings - bet

    if money <= 1:
        print("You ran out of money.")
        break
