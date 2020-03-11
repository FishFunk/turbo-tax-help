import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent {
  title = 'turbo-tax-help';
  _opened: boolean = false;
 
  toggleSidebar() {
    this._opened = !this._opened;
  }


  private async searchApi(query: string = "default", page: number = 1): Promise<any>{
    const uri = `http://localhost:5000/search?query=${query}&page=${page}`;
    
  }
}
