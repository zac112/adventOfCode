from collections import Counter

class Hand:
    def __init__(self, hand, bid) -> None:
        self.hand = hand
        self.bid = bid

    def rank(self):
        cards = Counter(self.hand)
        if 5 in cards.values():
            return 6
        if 4 in cards.values():
            return 5
        if 3 in cards.values():
            if 2 in cards.values():
                return 4
            return 3
        if 2 in Counter(cards.values()).values():
            return 2
        if 2 in cards.values():
            return 1
        return 0
    
    def __lt__(self, o):        
        if o.rank()==self.rank():
            t = str.maketrans({'T':'a','J':'b','Q':'c','K':'d','A':'e'})        
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
print(winnings)
