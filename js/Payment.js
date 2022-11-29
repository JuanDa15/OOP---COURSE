class Payment {
  id;

  constructor(){
    this.id = new Date().getDate();
  }
}

class Card extends Payment {
  number;
  cvv;
  date;

  constructor(number, cvv, date){
    super();
    this.number = number;
    this.cvv = cvv;
    this.date = date;
  }
}

class Paypal extends Payment {

  email;

  constructor(email) {
    super();
    this.email = email;
  }
}

class Cash extends Payment {

  constructor(){
    super();
  }
}