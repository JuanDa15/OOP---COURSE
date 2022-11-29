class CarBasic extends Car {
  brand;
  model;

  constructor(license, driver, passenger, brand, model) {
    super(license, driver, passenger);
    this.brand = brand;
    this.model = model;
  }
}

class UberX extends CarBasic {

  constructor(license, driver, passenger, brand, model){
    super(license, driver, passenger, brand, model);
  }
}

class UberPool extends CarBasic {

  constructor(license, driver, passenger, brand, model){
    super(license, driver, passenger, brand, model);
  }
}