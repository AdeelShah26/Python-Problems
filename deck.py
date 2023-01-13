###-------------Program for picking random 4 cards from the deck--------------###

deck=[x for x in range(52)]
suits=["Spade","Heart","Diamond","Clubs"]
ranks=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen', 'King']
cards=[]
for i in range(4):
    for j in range(13):
        cards.append(ranks[j]+" of "+suits[i])
random.shuffle(deck)
print(deck)
for i in range(4):
    suit=suits[deck[i]//13]
    rank=ranks[deck[i]%13]
    print(f"Card Number {deck[i]} is the {rank} of {suit}")
