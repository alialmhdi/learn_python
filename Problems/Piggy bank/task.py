class PiggyBank:
    # create __init__ and add_money methods
    dollars = 1
    cents = 1
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
    def add_money(self, deposit_dollars, deposit_cents):
        if self.cents + deposit_cents <= 99:
            self.dollars += deposit_dollars
            self.cents += deposit_cents
        else:
            self.dollars += deposit_dollars
            cent_reminig = ((self.cents + deposit_cents) % 100) / 100
            cent_divi = (self.cents + deposit_cents) / 100
            self.dollars += int(cent_divi - cent_reminig)
            if cent_reminig == 0:
                self.cents = int(cent_reminig)
            self.cents += int(cent_reminig)