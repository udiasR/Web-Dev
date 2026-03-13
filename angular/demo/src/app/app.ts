import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {NgForOf} from '@angular/common';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, NgForOf, FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('demo');
  num:number;
  message:string;
  nums:number[];
  students:any[];
  ok:boolean;
  cnt:number;
  items:any[];

  constructor(){
    this.num = 20;
    console.log(this.num);
    console.log("hello world");

    this.items = [];
    this.cnt = 0;
    this.ok = true;

    this.message = "Hello everyone";
    this.nums = [1,2,3,4,5];

    console.log(this.nums);
    console.log(this.message);
    this.students = [1,2,3,4,"dsfg"];
  }
  btnIncrease():number{
    this.cnt++;
    if(this.cnt > this.nums.length){
      this.cnt--;
    }
    return this.cnt;
  }


  addItem(x: string):void{
    if(x == ""){
      return;
    }

    this.items.push(x);
    this.message = "";
  }


  removeItem(index:number):void{
    this.items.splice(index, 1);
  }
}
