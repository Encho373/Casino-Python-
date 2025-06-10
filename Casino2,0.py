import random
import time
from collections import Counter

emojis = ['🍒', '🍋', '🍉', '🍇', '💎', '🪙', '🍎']

money = float(input("Баланс- "))

if money <= 1:
    print("Твърде си беден💸")
    exit()

spins = []

while money > 0:
    print(f"You have ${money:.2f}")

    bet = float(input("Залог- "))

    if bet <= 1 or bet > money:
        print("Нещо се обърка. Опитай отново по-късно.")
        continue

    for i in range(20):
        spin = [random.choice(emojis) for i in range(5)]
        print(*spin, end='\r')
        time.sleep(0.1)

    final_spin = [random.choice(emojis) for i in range(5)]
    print("Final result:", *final_spin)

    spins.append(final_spin)

    counts = Counter(final_spin)
    values = list(counts.values())

    winnings = 0

    if 5 in values:
        winnings = bet * 2
        print(f"🪙Jackpot🪙 Печелиш ${winnings:.2f}")
    elif 4 in values:
        winnings = bet * 1.5
        print(f"4 Еднакви!🥳 Печелиш ${winnings:.2f}")
    elif sorted(values) == [2, 3]:
        winnings = bet * 1.7
        print(f"Full House! 💥 Печелиш ${winnings:.2f}")
    elif values.count(2) == 2:
        winnings = bet * 1.4
        print(f"Два чифта! 🤑 Печелиш ${winnings:.2f}")
    elif 3 in values:
        winnings = bet * 1.3
        print(f"3 Еднакви!🎉 Печелиш ${winnings:.2f}")
    elif 2 in values:
        winnings = bet * 1.1
        print(f"2 Еднакви!🎊 Печелиш ${winnings:.2f}")
    else:
        print("😞 Хазартът убива. Започнете сега 😞")

    money += winnings - bet

    print(f"Общ брой завъртания: {len(spins)}")

    if money <= 1:
        print("You ran out of money.")
        break

