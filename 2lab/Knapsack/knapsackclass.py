class KnapSack():
    id = 0
    def __init__(self, weight, price):
        self.id = KnapSack.id
        self.weight = weight
        self.price = price
        KnapSack.id += 1