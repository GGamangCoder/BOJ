from collections import deque

N = int(input())

def card(n):
    cards = deque([i for i in range(1, n+1)])
    while len(cards) > 1:
        cards.popleft()
        card1 = cards.popleft()
        cards.append(card1)

    return cards[0]
    
print(card(N))