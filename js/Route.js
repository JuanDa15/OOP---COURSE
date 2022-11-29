class RouteClass {
  id;
  init;
  end;

  constructor(init,end){
    this.id = new Date().getDate();
    this.init = init;
    this.end = end;
  }
}