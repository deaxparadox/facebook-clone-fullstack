import { Component, Inject, OnInit } from '@angular/core';
import { FooterComponent } from '../../layout/footer/footer.component';
import { NavbarComponent } from '../../layout/navbar/navbar.component';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { DOCUMENT } from '@angular/common';
import { privateDecrypt } from 'crypto';
import { AuthService } from '../../services/auth.service';


@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    ReactiveFormsModule
  ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent{
  
  constructor(private authService: AuthService) {

  }

  siteName = "facebook"
  siteMessage = "Facebook helps you connect and share with the people in your life."
  siteLogo = "assets/facebook.svg"

  copyRight = "Meta@2024"

  loginForm = new FormGroup({
    usernameForm: new FormControl(""),
    passwordForm: new FormControl("")
  })

  onSubmit() {
    console.log(this.loginForm.value)
    this.login(this.loginForm.value['usernameForm']!, this.loginForm.value['passwordForm']!);
  }


  login(username: String, password: String) {
    this.authService.login(username, password);
  }
}
