class Card006():
    
    @staticmethod
    def all_cards():
        list_numbers_of_cards = list(range(1, 105))
        def str_and_ (a):
            return '_' + str(a)
        cards_with_ = list(map(str_and_, list_cards))
        def generate_card006 (name):
            name = Card006(int(name[1:]))
            return name
        return list(map(generate_card006, cards_with_))
    
    @staticmethod
    def type():
        return '<class \'__main__.Card006\'>'
    
    def __init__(self, number):
        def _det_score(number1):
            if number1 == 55:
                return 7
            elif number1 % 11 == 0:
                return 5
            elif number1 % 10 == 0:
                return 3
            elif number1 % 5 == 0:
                return 2
            else:
                return 1    
        self._validate(number)
        self.card_number = number    
        self.card_score = _det_score(number)

    def _validate(self, number):
        if not (number > 0 and number < 105):
            raise ValueError('Invalid card\'s number')
    
    def __eq__(self, other): #ѕровер€ть ли что other - card006???
        if self.card_number == other.card_number:
            return True
        else:
            return False
        
    def __ne__(self, other):
        return not (self == other)
    
    def __lt__(self, other):
        return self.card_number < other.card_number
    
    def __str__(self):
        return '{}'.format(self.card_number)
    
    def __repr__(self):
        return "Card006 with number {}".format(self.card_number)
    
    def score(self):
        return self.card_score
        
class Row():
    
    def __init__(self, card):
        self._validate(card)
        self.list_card = [card]    
        
    def _validate(self, card):
        if not (isinstance(card, Card006)):
            raise ValueError('Invalid type')
            
    def __str__(self):
        return '{}'.format(self.list_card)
    
    def add(self, card):
        self.list_card.append(card)
