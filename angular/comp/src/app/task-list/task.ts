export class Task{
  static current:number=0;
  id:number;
  name:string;
  isDone:boolean;

  constructor(id:number=1, name:string=""){
    Task.current++;
    this.id = Task.current;
    this.name = name;
    this.isDone = false;
  }
}
