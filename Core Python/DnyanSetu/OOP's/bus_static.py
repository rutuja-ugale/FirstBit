class BusDriver:
    # Static Variable
    companyName = "MSRTC"

    def __init__(self, depotName, driverName, busNo):
        self.depotName = depotName        
        self._driverName = driverName     
        self.__busNo = busNo              

    # Getter Method
    def getBusNo(self):
        return self.__busNo

    # Setter Method
    def setBusNo(self, busNo):
        self.__busNo = busNo

    def display(self):
        print("Company Name :", BusDriver.companyName)
        print("Depot Name   :", self.depotName)
        print("Driver Name  :", self._driverName)
        print("Bus No       :", self.__busNo)

b = BusDriver("Shrirampur", "Ramesh Patil", "MH17 AB 1234")
b.display()

print("\nAccessing Public & Protected Members")
print("Depot Name :", b.depotName)
print("Driver Name :", b._driverName)

# Getter
print("\nBus No (Getter) :", b.getBusNo())

# Setter
b.setBusNo("MH17 XY 5678")

print("\nAfter Updating Bus Number")
b.display()