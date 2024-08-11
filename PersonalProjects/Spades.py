import random

# a team system, taking turns, THEN rules

game_on = True

card_deck = []
p1_hand = []
p2_hand = []
p3_hand = []
p4_hand = []

round_counter = 0 # TEMP, only shows how many times a sucessful loop occurs FOR TESTING
team_a_score = 0 # Total number of books
team_b_score = 0 # Total number of books

my_deck = """h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14"""
x = my_deck.split(", ")
random.shuffle(x)

# DEAL THE DECK
for y in range(0, 13):
    p1_hand.append(x[0])
    x.remove(x[0])
    p2_hand.append(x[0])
    x.remove(x[0])
    p3_hand.append(x[0])
    x.remove(x[0])
    p4_hand.append(x[0])
    x.remove(x[0])


