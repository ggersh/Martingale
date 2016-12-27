from random import randint

first_card = randint(1,13)
sec_card = randint(1,13)
third_card = randint(1,13)

amt = 100

pot = 25

bet = 20

while amt != 0:
    subtract = abs(first_card-sec_card-1)
    if subtract/13 > .5:
        if sec_card > first_card:
            if third_card < sec_card and third_card > first_card:
                amt = amt + bet
                print amt
            else:
                amt = amt - bet
                bet=bet*2
                print amt
        if sec_card < first_card:
            if third_card > sec_card and third_card < first_card:
                amt = amt + bet
                print amt
            else:
                amt = amt - bet
                bet = bet*2
                print amt
    first_card = randint(1,13)
    sec_card = randint(1,13)
    third_card = randint(1,13)
