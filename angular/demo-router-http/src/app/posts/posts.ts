import {Component, OnInit} from '@angular/core';
import {Post} from '../models';
import {POSTS} from '../fake-db';

@Component({
  selector: 'app-posts',
  imports: [],
  templateUrl: './posts.html',
  styleUrl: './posts.css',
})
export class Posts implements OnInit {
  posts: Post[] | undefined;
  constructor() {
  }

  ngOnInit() {
    this.posts = POSTS;
  }

}
