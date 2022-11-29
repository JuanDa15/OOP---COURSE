from car import Car

class CarBasic(Car):
  brand = str
  model = str
  
  def __init__(self, license, driver, passengers, brand, model):
    super(CarBasic, self).__init__(license, driver, passengers)
    self.brand = brand
    self.model = model
    
    
    
class UberX(CarBasic):
  
  def __init__(self, license, driver, passengers, brand, model):
    super(UberX, self).__init__(license, driver, passengers, brand, model)
    

class UberPool(CarBasic):
  
  def __init__(self, license, driver, passengers, brand, model):
    super(UberPool, self).__init__(license, driver, passengers, brand, model)