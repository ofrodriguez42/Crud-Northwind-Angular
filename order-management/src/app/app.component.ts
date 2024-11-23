// src/app/app.component.ts
import { Component } from '@angular/core';
import { CreateCardComponent } from './components/create-card/create-card.component';
import { UpdateCardComponent } from './components/update-card/update-card.component';
import { DeleteCardComponent } from './components/delete-card/delete-card.component';
import { ViewCardComponent } from './components/view-card/view-card.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true,
  imports: [
    CreateCardComponent,
    UpdateCardComponent,
    DeleteCardComponent,
    ViewCardComponent
  ]
})
export class AppComponent { }
