class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = int(hyp)
        self.a = int(leg_1)
        self.b = int(leg_2)
        # calculate the area here
        self.get_area()

    def get_area(self):
        area = (1 / 2 * self.a) * self.b
        if self.c * self.c == (self.a * self.a) + (self.b * self.b):
            print(area)
        else:
            print("Not right")


tr_hyp = input().split()
tr = RightTriangle(tr_hyp[0], tr_hyp[1], tr_hyp[2])
