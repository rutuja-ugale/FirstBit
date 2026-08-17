class Time:
    # def__add
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    def __add__(self, other):
        hR = self.hr+other.hr
        mIn = self.min+other.min
        sEc = self.sec+other.sec
        return Time(hR, mIn, sEc)

    def __str__(self):
        return f"{self.hr} : {self.min}: {self.sec}"
# Create Object
t1 = Time(1, 2, 33)
t2 = Time(2, 4, 30)
print(t1 + t2)