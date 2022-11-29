class Account {
  id;
  name;
  document;
  email;
  password;

  constructor(name, document, email, password){
    this.id = new Date().getDate();
    this.name = name;
    this.document = document;
    this.email = email;
    this.password = password;
  }
}

class Driver extends Account {
  constructor(name, document, email, password) {
    super(name, document, email, password)
  }
}

class User extends Account {
  constructor(name, document, email, password) {
    super(name, document, email, password)
  }
}