import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { share } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent {
  sidebarOpen: boolean = false;
  searchData: Observable<any>;
  searchInput: string;

  constructor(private http: HttpClient){

  }
 
  toggleSidebar() {
    this.sidebarOpen = !this.sidebarOpen;
    this.searchApi();
  }

  onSearchSubmit(){
    this.searchApi(this.searchInput);
  }

  private async searchApi(query: string = "default", page: number = 1){
    const uri = `http://localhost:5000/search?query=${query}&page=${page}`;
    this.searchData = this.http.get(uri).pipe(share());
  }
}
