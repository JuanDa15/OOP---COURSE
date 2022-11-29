from car import Car

class CarPremium(Car): 
  
  typeCarAccepted = []
  seatsMaterial = []
  
  def __init__(self, license, driver, passengers, typeCarAccepted, seatsMaterial):
    super(CarPremium, self).__init__(license, driver, passengers)
    self.typeCarAccepted = typeCarAccepted
    self.seatsMaterial = seatsMaterial
    
    
class UberBlack(CarPremium):
  def __init__(self, license, driver, passengers, typeCarAccepted, seatsMaterial):
    super(UberBlack, self).__init__(license, driver, passengers)
    self.typeCarAccepted = typeCarAccepted
    self.seatsMaterial = seatsMaterial
    
class UberVan(CarPremium):
  def __init__(self, license, driver, passengers, typeCarAccepted, seatsMaterial):
    super(UberVan, self).__init__(license, driver, passengers)
    self.typeCarAccepted = typeCarAccepted
    self.seatsMaterial = seatsMaterial