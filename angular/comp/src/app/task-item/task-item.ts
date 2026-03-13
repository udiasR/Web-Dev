import {Component, Input, model, Output, EventEmitter} from '@angular/core';
import {Task} from '../task-list/task';
import {NgClass} from '@angular/common';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-task-item',
  imports: [
    NgClass,
    FormsModule
  ],
  templateUrl: './task-item.html',
  styleUrl: './task-item.css',
})
export class TaskItem {

  @Input() task!: Task;
  @Output() remove = new EventEmitter<number>();
  @Output() done = new EventEmitter();


  removeTask(id:number):void{
    this.remove.emit(id);
  }


  isDoneChanged(){
    this.done.emit(this.task);
  }

}
