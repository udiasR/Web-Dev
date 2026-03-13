import { Component } from '@angular/core';
import {Post} from '../models';

@Component({
  selector: 'app-post-detail',
  imports: [],
  templateUrl: './post-detail.html',
  styleUrl: './post-detail.css',
})
export class PostDetail {
  post: Post;
  constructor() {
  }

  ngOnInit() {}

}
