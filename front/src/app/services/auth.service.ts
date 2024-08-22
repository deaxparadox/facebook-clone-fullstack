import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';


const AUTH_ENDPOINTS = {
  "login": "http://localhost:8000/api/v1/auth/login/",
  "logout": "http://localhost:8000/api/v1/auth/logout/"
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  login(username: String, password: String) {
    console.log(username, password);
    this.http.get(AUTH_ENDPOINTS.login).subscribe(e => {
      console.log(e);
    })
    
  }
}
