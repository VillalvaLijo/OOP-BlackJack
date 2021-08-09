# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:58:13 2019

@author: $PACEkiRK
"""

class deal_card(object):
    
    def __init__():
        pass
    def deal_card_out( dealed_cards): #= []): #(self, *dealed_cards): #(self, dealed_cards): # (self, dealed_cards = [], *args):
        #if I list it as (self, dealed_cards) I get error "TypeError deal_card_out() missing 1 required positional argument: 'dealed_cards'
        # With (self, dealed_cards = [], *args it at least works) but dosen't nescarily pass the list correctly
       #with (self, *dealed_cards) this returns the list as a tuple and dosen't pass it correct.
       #try with (self, dealed_cards = []), result: still not passing in the list dealed_cards from inside the function
        print("This is a test print statement at the beginning of this method to test that dealed_cards was passed in correctly.")
        print(dealed_cards)
        card_one_face_value = 'Seven'
        card_one_suit_value = 'Clubs'
        
        for _ in dealed_cards:
            #print("This is a test statement inside the for lop within deal_card_out in order to test it works")
            #print(f"dealed_cards [_[0]] = {_[0]}")
            #print(f"dealed cards [_[1]] = {_[1]}")
            #print(f"card_one_face_value = {card_one_face_value}")
            #print(f"card_one_suit_value = {card_one_suit_value}")
            if card_one_face_value == _[0]:
                print(f"This is a test print statement inside the for loop within deal_card out, it willl print out _[0] inside this for loop: {_[0]}")
                if card_one_suit_value == _[1]: #adjusted [_[1]] from dealed_cards[_[1]] which wasn't registering properly
                    print(f"this is a test print statement inside the for loop within deal_card out it will print out dealed_cards _[1] to show what is happening inside this loop: {_[1]}")
                    print("test loop successful")
                        #self.deal_card_out(dealed_cards)
                    
                else:
                   print(f"This is a test print statement inside the for loop within deal_card out, it willl print out _[0] inside this for loop: {_[0]}") 
            #       pass
            #else:
               #print(f"this is a test print statement inside the for loop within deal_card out it will print out dealed_cards[_[1]] to show what is happening inside this loop: {[_[1]]}")
            #   pass
        dealed_cards.append([card_one_face_value,card_one_suit_value])
        #args.append([card_one_face_value, card_one_suit_value])
                
        print("This is a test print inside of deal_card_out, it prints list dealed_cards")
        #print(args)
        print(dealed_cards)
        #self.card_face_value = card_one.face_value
        #self.card_suit_value = card_one.suit_value
        return [dealed_cards,card_one_face_value,card_one_suit_value]
        #return [args, card_one_face_value, card_one_suit_value]
        
dealed_cards = [['Place','Holder'],['Seven','Clubs']]
print("this is a test print statement outside of the method to test that dealed_cards is being passed in correctly")
print(dealed_cards)
test_run = deal_card.deal_card_out(dealed_cards)