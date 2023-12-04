with open("data.txt") as f:
    data = f.read().split("\n")

score = 0
cards = {}

for card in data:
    winNums,nums = card.split(":")[1].split("|")
    
    empty = lambda a:len(a.strip())>0
    winNums = set(map(int, filter(empty, winNums.split(" "))))
    nums = set(map(int, filter(empty, nums.split(" "))))
    score = len(winNums.intersection(nums))
    cardID = card.split(":")[0].replace("Card","")
    cards[int(cardID)] = [score,1]

for cardID, scores in cards.items():
    for i in range(0,cards[cardID][0]):
        if cardID+i>len(cards):break
        cards[cardID+i+1][1] += cards[cardID][1]

print(sum(map(lambda a:a[1],cards.values())))