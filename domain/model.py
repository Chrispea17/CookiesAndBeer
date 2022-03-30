from dataclasses import dataclass


from dataclasses import dataclass

@dataclass(frozen=True)
class Recommendation:
    ItemID: str
    ItemName: str

class Recommend:
    def __init__(ItemId,ItemName):
        self.ItemID
        self.ItemName   
