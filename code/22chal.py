data = open("22chal.txt").readlines()
data = [i.replace("\n", "") for i in data if i!='\n']
from collections import deque

idx_p1 = data.index('Player 1:')
idx_p2 = data.index('Player 2:')
cards_p1 = data[(idx_p1+1):(idx_p2)]
cards_p2 = data[(idx_p2+1):]
deck_p1 = deque([int(i) for i in cards_p1[::-1]])
deck_p2 = deque([int(i) for i in cards_p2[::-1]])
###popleft for bottom, pop for top
def play_game(decks, recursive=True):
    count=0
    deck_tracks = [[],[]]
    min_len = min([len(deck) for deck in decks])
    while min_len>0:
        if list(decks[0]) in deck_tracks[0] and list(decks[1]) in deck_tracks[1]:
            print("RECURSION TRAP")
            print(count)
            game_winner = 0
            return game_winner
        else:
            for i in range(2):
                deck_tracks[i].append(list(decks[i]))
        cards = [deck.pop() for deck in decks]
        deck_lens = [len(deck) for deck in decks]
        if all([_len>=card for card, _len in zip(cards, deck_lens)]) and recursive:
            copy_decks = [deck.copy() for deck in decks]
            ##Pop off elements to make the decks the length of the 'card'
            [[copy_deck.popleft() for k in range(len(copy_deck)-card)] for card, copy_deck in zip(cards,copy_decks)]
            assert all([len(copy_deck)==card for card,copy_deck in zip(cards, copy_decks)])
            which_won = play_game(copy_decks)
            which_lost = [1,0][which_won]
            ## First the higher, then the lower
            decks[which_won].appendleft(cards[which_won])
            decks[which_won].appendleft(cards[which_lost])
        else:
            winning_card = max(cards)
            winner = [i == winning_card for i in cards]
            if all(winner):
                print('TIE') ##never happens
                for deck, card in zip(decks, cards):
                    deck.append(card)
            which_won = winner.index(True)
            cards.sort()
            ## First the higher, then the lower
            decks[which_won].appendleft(cards[1])
            decks[which_won].appendleft(cards[0])
        min_len = min([len(deck) for deck in decks])
        count+=1
        if min_len==0:
            game_winner = [len(deck)>0 for deck in decks].index(True)
    return game_winner
    
def score_deck(deck):
    p = deck.copy()
    sum=0
    for i,card in enumerate(deck):
        sum+=(i+1)*card
    return(sum)


decks = [deck_p1, deck_p2]
copy_decks = [deck.copy() for deck in decks]
winner_p1 = play_game(copy_decks, recursive=False)
print(winner_p1)
print([score_deck(deck) for deck in copy_decks])
winner_p2 = play_game(decks)
print([score_deck(deck) for deck in decks])

###Too low 11000
###Too high 34555