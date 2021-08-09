# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:19:47 2019

@author: $PACEkiRK
"""

# -*- coding: utf-8 -*-
"""

    Create a deck of 52 cards
    Shuffle the deck
    Ask the Player for their bet
    Make sure that the Player's bet does not exceed their available chips
    Deal two cards to the Dealer and two cards to the Player
    Show only one of the Dealer's cards, the other remains hidden
    Show both of the Player's cards
    Ask the Player if they wish to Hit, and take another card
    If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
    If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
    Determine the winner and adjust the Player's chips accordingly
    Ask the Player if they'd like to play again

"""
import random
"""
import random choice, select dictionaries from the cards and then 
randomint(between 1 and 13) also use randomint(between 1 and 4) for suit value

this way you select a card... then have another card selected, but make sure it cannot
be of the same combnation of one previously created.

or use random choice to select a random number from the sequence and then throw it back if you 
have a selection that is matched.
"""
class card(object):
    
    def __init__(self):
        "This object initilizes a random card"
        
        face_value_dic = {1:'Ace',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Jack',12:'Queen',13:'King'}
        suit_value_dic = {1:'Hearts',2:'Diamonds',3:'Clubs',4:'Spades'}
        card.face_value = face_value_dic[random.randint(1,13)]
        card.suit_value = suit_value_dic[random.randint(1,4)]
        #return [face_value,suit_value];
   #def str(self):
        """
        write the card out for the user
        """
#        pass
    
#class deck(object):  #don't need to create a deck, cards are created randoms and then
                    #checked for duplicates
    
    """
    consider making a deck class that initiatise card instances
    this deck should also have the ablity to be shuffled
    and print out the cards in the deck
    """  
#    def __init__(self):
#        self.deck = [] 
        
class deal_card(object):
    
    global card_count
    global dealed_cards
    
    def __init__(self):
        pass
    
    #def assign_random_value(self): #random value of card already created in card class
        #face_value = random.randint(1,13)
        #suit_value = random.randint(1,4)
        #card_dealed = card()
        #dealed_cards.append([card_dealed.face_value_dic[face_value],card_dealed.suit_value_dic[suit_value]]) #list as
        #invalid syntax, figure out why, dealed cards is not being passed correctly for some rason.
        
#NEED to figure out way to accesses face_value and suit value         
    #def check_random_value(self):
     
    #try placing assign_random_value and check random value in one method
       
    def deal_card_out(dealed_cards):
        #print("this is a test print statement inside deal_card_out that prints the list dealed_cards first to show it is passed correctly")
        #print(dealed_cards)
        card_one = card()
        
        for _ in dealed_cards:
            if card_one.face_value == _[0]:
                #print(f"This is a test print statement inside the for loop within deal_card out, it willl print out _[0] inside this for loop: {_[0]}")
                if card_one.suit_value == _[1]: #adjusted [_[1]] from dealed_cards[_[1]] which wasn't registering properly
                    #print(f"this is a test print statement inside the for loop within deal_card out it will print out dealed_cards _[1] to show what is happening inside this loop: {_[1]}")
                    deal_card.deal_card_out(dealed_cards)
                else:
                   #print(f"This is a test print statement inside the for loop within deal_card out, it willl print out [_[0]] inside this for loop: {[_[0]]}") 
                   pass
            else:
               #print(f"this is a test print statement inside the for loop within deal_card out it will print out dealed_cards[_[1]] to show what is happening inside this loop: {[_[1]]}")
               pass
        dealed_cards.append([card_one.face_value,card_one.suit_value])
                
        #print("This is a test print inside of deal_card_out, it prints list dealed_cards")
        #print(dealed_cards)
        #self.card_face_value = card_one.face_value
        #self.card_suit_value = card_one.suit_value
        return [dealed_cards,card_one.face_value,card_one.suit_value] #method passes back dealed_cards list so that dealed_cards can be kept track of and duplicates are not dealed
                
                
#deal_card.assign_random_value()
#deal_card.check_random_value()

class deal_round(deal_card):
    
    def __init__(self):
        
        dealed_cards = [['Place','holder']]
        self.dealer_hand = []
        self.player_hand = []
        players_first_card = deal_card.deal_card_out(dealed_cards)
        self.player_hand.append([players_first_card[1],players_first_card[2]])
        #print("This is a print statement inside of deal_round function, it will print dealed_cards list")
        dealed_cards = players_first_card[0]
        #print(dealed_cards)
        dealers_first_card = deal_card.deal_card_out(dealed_cards)
        self.dealer_hand.append([dealers_first_card[1],dealers_first_card[2]])
        dealed_cards = dealers_first_card[0]
        #print("This is the secound printing of dealed_cards within method deal_round")
        #print("In order to show that dealed_cards has been updated after the dealer is dealt a card")
        #print(dealed_cards)
        players_secound_card = deal_card.deal_card_out(dealed_cards)
        self.player_hand.append([players_secound_card[1],players_secound_card[2]])
        dealed_cards = players_secound_card[0]
        #print("This is a printing of list dealed cards inside of method deal_round to show updated list after player one is dealed a secound card")
        #print(dealed_cards)
        dealers_secound_card = deal_card.deal_card_out(dealed_cards)
        self.dealer_hand.append([dealers_secound_card[1],dealers_secound_card[2]])
        dealed_cards = dealers_secound_card[0]
        #print("This is a test printing of list dealed cards inside of method deal_round to show updated list after player is dealt a secound card")
        #print(dealed_cards)
        player_one_hs = self.hit_or_stay(dealed_cards, self.player_hand)
        dealed_cards = player_one_hs[0]
        #print("this is a test print statement inside deal_round that prints updated dealed_cards list after hit_or_stay method in order to show it has been updated")
        #print(dealed_cards)
        self.player_hand = player_one_hs[1]
        dealer_draw = self.dealer_draw_seventeen(dealed_cards, self.dealer_hand) #call dealer draw seventeen method to end the round
        dealed_cards = dealer_draw[0]
        self.dealer_hand = dealer_draw[1]        #re-update dealed_cards and dealer_hand for record keeping
        
        
    def hit_or_stay(self,dealed_cards,player_hand):
        
        hand_score = self.hand_value(player_hand)
        print(f"The value of Player one's hand is {hand_score}") #make sure you print out player one's cards so they can see if the have a soft ace
        print(f"Player one's cards are: {player_hand}")
        if hand_score > 21:
            print("Player one busts")
            player_one_wins = False
        elif hand_score == 21:
            print("BlackJack! Player one wins")
            player_one_wins = True
        elif hand_score < 21:
            #player_one_wins = 'null'
            hit_stay = input("Player would you like to hit or stay? h or s: ")
            player_one_wins = 'null'
            if hit_stay.lower() == 'h':
                hit_card = deal_card.deal_card_out(dealed_cards)
                player_hand.append([hit_card[1],hit_card[2]])
                dealed_cards = hit_card[0]
                #print("This is a test print function inside of hit_or_stay method, first we will print player_hand and then dealed_cards list to show that they have been appended correctly")
                #print(player_hand)
                #print(dealed_cards)
                print(f"Payer one's new card is {hit_card[1]} of {hit_card[2]}")
                #print(f"Player one's new score is {self.hand_value(player_hand)}")
                self.hit_or_stay(dealed_cards,player_hand)  
                
                
                
                
                #player_one_wins = 'null'
                
            else:
                print("Player one has chossen to stay")
                pass
        return [dealed_cards,player_hand, player_one_wins] #dealed_cards list needs to be returned so that it can be passed to 
                                          #to deal_draw_seventeen method and the cards that are drawn from the 
                                          #deck can be kept track of, player_hand is also passed in order to keep record
                                          #inside deal_round __init__
   
    def dealer_draw_seventeen(self, dealed_cards, dealer_hand): #do I need to call dealer_hand as self.dealer_hand? investigate further
        
        dealer_hand_value = self.hand_value(dealer_hand)
        print(f"This print statement is inside dealer_draw_seventeen method and prints the value of the dealer's hand: {dealer_hand_value}")
#        
        #while loop that will have the dealer draw until he recahes seventeen
        
        while dealer_hand_value < 17:
            print(f"Dealer's hand: {dealer_hand}")
            dealer_hand_value = self.hand_value(dealer_hand)
            print(f"Value of Dealer's hand: {dealer_hand_value}")
            dealer_hit_card = deal_card.deal_card_out(dealed_cards)
            dealer_hand.append([dealer_hit_card[1],dealer_hit_card[2]])
            dealed_cards = dealer_hit_card[0]
            dealer_hand_value = self.hand_value(dealer_hand)
            print("This is a test print statemnet inside of dealer_draw_seventeen while loop that first prints the dealer_hand to show that it has been updated and then prints the last dealed_cards to show that has been updated as well")
            print(f"dealer_hand: {dealer_hand}")
            print(f"dealed_cards: {dealed_cards}")
        
        return [dealed_cards,dealer_hand] #return these list to deal_round __init__ for record keeping
   
    def hand_value(self, hand):
        
        ace_count = 0
        player_score = 0
        
        for _ in hand:              #now we will evaluate the value of each card in the hand passed
            if _[0] == 'Ace':       #to method hand_value, it will evaluate to the variable player_score
                ace_count += 1      #and then it will return the value.
            elif _[0] == 'Two':     #ace values will be held in the place holder ace_count, and then the
                player_score += 2   #score of the given aces will be evaluated in relation to the total
            elif _[0] == 'Three':   #player_score as in blackjack
                player_score += 3
            elif _[0] == 'Four':
                player_score += 4
            elif _[0] == 'Five':
                player_score += 5
            elif _[0] == 'Six':
                player_score += 6
            elif _[0] == 'Seven':
                player_score += 7
            elif _[0] == 'Eight':
                player_score += 8
            elif _[0] == 'Nine':
                player_score += 9
            elif _[0] == 'Ten' or 'Jack' or 'Queen' or 'King':
                player_score += 10
                
        if ace_count == 1:
            if player_score <= 10:
                player_score += 11
            else:
                player_score += 1
        elif ace_count == 2:
            if player_score <= 9:
                player_score += 12
            else:
                player_score += 2
        elif ace_count == 3:
            if player_score <= 8:
                player_score += 13
            else:
                player_score += 3
        elif ace_count == 4:
            if player_score <= 7:
                player_score += 14
            else:
                player_score += 4
        
        return player_score
            
            
        
    def game_eval(self, player_hand, dealer_hand):
        """this method evaluates who won, the dealer or the player"""
        player_hand_value = self.hand_value(player_hand)
        dealer_hand_value = self.hand_value(dealer_hand)
        
        if player_hand_value > dealer_hand_value and player_hand_value <= 21:
            print("Player One has won the game")
            player_one_wins = True
        elif dealer_hand_value > player_hand_value and dealer_hand_value <= 21:
            print("Dealer has won the game")
            player_one_wins = False
            
        return player_one_wins
        
        
    #def deal_dealer(self): 
        
        
    #    self.assign_random_value() #figure out how to pass this value to dealer_hand[]
    #    self.check_random_value()  #so now dealed_cards is appended, from this point
                                        # we need to assign value to dealer_hand
        #self.__init__.dealer_hand.append(dealed_cards[card_count])
    #    dealer_hand.append(dealed_cards[card_count])
    
#main
        
#dealed_cards =[['place','holder']]
#card_count = 0

first_round = deal_round()

#dealer_hand = []

#first_deal = deal_table()#you need to reveiw instiatiating a class
#first_deal.deal_dealer()
#deal_table.deal_dealer() #should call out a card for the dealer
#deal_table.deal_dealer() #call it twice
#dealing it like this is going to call out dealer_hand twice and make it.
#have to assign outside the function so it stays global.

print("Now we are printing out the dealers hand.")
print(first_round.dealer_hand) #dealer hand is not written too.

print("Now we are printing out the players hand.")
print(first_round.player_hand)

#print("Now we are printing out dealed cards list")
#print(dealed_cards)

