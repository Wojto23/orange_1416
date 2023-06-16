class Bike:
    """
    Class representing a bike
    """
    ilosc_egzemplarzy = 0

    def __init__(self, colour: str, model: str, represents):
        self.colour = colour
        self.model = model
        self.represents = represents
        Bike.ilosc_egzemplarzy += 1

    def brake(self):
        """
        Method to brake the bike :)
        :return: print()
        """
        print("Braking")

    def __repr__(self):
        """
        Method to represent the bike
        :return: repr()
        """
        if self.represents:
            return f"Rower {self.model} w kolorze {self.colour}"
        else:
            return super().__repr__()

