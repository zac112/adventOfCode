from collections import Counter

class Hand:
    def __init__(self, hand, bid) -> None:
        self.hand = hand
        self.bid = bid

    def countCards(self, cards=None):
        if cards == None:
            cards = self.hand

        cards = Counter(cards)
        jokers = cards.get('J',0)        
        for k in cards:
            if k=='J': continue
            cards[k] += jokers

        return cards

    def removeCards(self, card, hand=None):
        if not hand:
            hand = str(self.hand)
        newHand = list(hand.replace(card,""))
        rem = self.hand.count(card)
        while rem < 3:
            newHand.remove("J")
            rem += 1
        return "".join(newHand)


    def rank(self):
        cards = self.countCards()
        for c,num in cards.most_common():
            if num == 5:
                return 6
            if num == 4:
                return 5
            if num == 3:
                newHand = self.removeCards(c,self.hand)
                if 2 in self.countCards(newHand).values():
                    return 4                
                return 3
            if 2 in Counter(cards.values()).values():
                return 2
            if 2 in cards.values():
                return 1
        return 0
    
    def __lt__(self, o):        
        if o.rank()==self.rank():
            t = str.maketrans({'T':'a','J':'1','Q':'c','K':'d','A':'e'})        
            return self.hand.translate(t) < o.hand.translate(t)
        return self.rank()<o.rank()
    
    def __repr__(self) -> str:
        return self.hand
                
with open('data.txt') as f:
    data = f.read().split('\n')
    data = [(hand, int(bid)) for hand, bid in map(lambda a:a.split(" "),data)]

data = list(map(lambda a:Hand(*a),data))
data.sort()

winnings = sum(map(lambda a:a[0]*a[1].bid, enumerate(data,start=1)))
print("Winnings:",winnings, end=" ")