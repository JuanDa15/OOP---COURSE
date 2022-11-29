class CarPremium extends Car {

  typeCarAccepted;
  seatsMaterial;

  constructor(license, driver, passenger, typeCarAccepted, seatsMaterial) {
    super(license, driver, passenger);
    this.typeCarAccepted = typeCarAccepted;
    this.seatsMaterial = seatsMaterial;
  }
}

class UberBlack extends CarPremium {

  constructor(license, driver, passenger, typeCarAccepted, seatsMaterial){
    super(license, driver, passenger, typeCarAccepted, seatsMaterial);
  }
}

class UberVan extends CarPremium {

  constructor(license, driver, passenger, typeCarAccepted, seatsMaterial){
    super(license, driver, passenger, typeCarAccepted, seatsMaterial);
  }
}