import { Component, signal } from '@angular/core';
import {RouterLink, RouterOutlet} from '@angular/router';
import {Home} from './home/home';
import {About} from './about/about';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Home, About, RouterLink],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('demo-router-http');
}
