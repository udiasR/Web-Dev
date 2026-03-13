import {RouterModule, Routes} from '@angular/router';
import {NgModule} from '@angular/core';
import {Home} from './home/home';
import {About} from './about/about';
import {NotFound} from './not-found/not-found';
import {Posts} from './posts/posts';

export const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: Home },
  { path: 'about', component: About },
  {path: 'posts', component: Posts},
  { path: '**', component: NotFound}, // must be implemented last (because, order is matter)
];

@NgModule(
  {
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
  }
)

export class AppRoutingModule {}

