class Car {
  id;
  license;
  driver;
  passenger;

  constructor(license, driver, passenger) {
    this.id = new Date().getDate();
    this.license = license;
    this.driver = driver;
    this.passenger = passenger;
  }

  printDataCar() {
    console.log(`License: ${this.license}, driver: ${this.driver.name}, passengers: ${this.passenger}`)
  }
}