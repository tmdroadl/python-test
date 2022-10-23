from typing import List
AI = []
Player = []
class Card:
    def __init__(self,number : int, kind : str):
        self.number :int = number
        self.kind : str = kind
class Card_List:
    def __init__(self) -> None:
        self.deck  : List[Card] = []

    def init_deck(self) -> None: # 덱을 만드는 함수임
        deck_info = [(1,5),(2,3)]
        for fruit in ["바나나","사과","포도", "샤인머스켓"]:
            for fruit_num, card_num in deck_info:
                for i in range(card_num):
                    self.deck.append()