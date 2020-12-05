"""     Гральні карти мають 2 поля:
        масть - піки, хрести, бубни, чирви та
        значення - шість, сім, вісім, дев`ять, десять, валет, дама, король,
        туз;
        Скласти програму, яка перевіряє, чи "б’є" карта K1 карту K2 враховуючи те,
        що масть KM є козирною.
"""
import random as rn
tpl_trump_suit = tuple(('пики', 'трефы', 'бубей', 'черви'))
tpl_value_cards = tuple(('шесть', 'сем', 'восем', 'девять', 'десять', 'валет', 'дама', 'король', 'туз'))


find_trump = str(tpl_trump_suit[rn.randint(0, 3)])
Card1 = tpl_value_cards[rn.randint(0, 8)], tpl_trump_suit[rn.randint(0, 3)]
Card2 = tpl_value_cards[rn.randint(0, 8)], tpl_trump_suit[rn.randint(0, 3)]

print("Козырь:", find_trump)

if Card1[1] == Card2[1]:
    if tpl_value_cards.index(Card1[0]) < tpl_value_cards.index(Card2[0]):
        print(*Card1, "не бъет", *Card2)
    else:
        print(*Card1, "бъет", *Card2)

elif Card1[1] == find_trump:
       print(*Card1, "бъет", *Card2)

elif Card2[1] == find_trump:
       print(*Card2, "бъет", *Card1)

else:
    print(*Card1, "не бъет", *Card2,)











