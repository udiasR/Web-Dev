import { Component } from '@angular/core';
import {Task} from './task';
import {FormsModule} from '@angular/forms';
import {TaskItem} from '../task-item/task-item';

@Component({
  selector: 'app-task-list',
  imports: [
    FormsModule,
    TaskItem
  ],
  templateUrl: './task-list.html',
  styleUrl: './task-list.css',
})
export class TaskList {
  tasks: Task[];
  currentTask: Task;
  cnt:number
  doneTasks: Task[];

  constructor() {
    this.tasks = [];
    this.cnt = 0;
    this.doneTasks = [];
    this.currentTask = new Task(1, "");
  }


  addTask():void{
    this.cnt++;
    this.currentTask.id = this.cnt;
    this.tasks.push(this.currentTask);
    this.currentTask = new Task();
  }

  onRemoveTask(id:number):void{
    this.tasks = this.tasks.filter((x)=> x.id !== id);
  }

  addDone(task:Task):void{
    this.doneTasks.push(task);
  }

}
