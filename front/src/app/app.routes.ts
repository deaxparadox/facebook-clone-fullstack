import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ProfileComponent } from './components/profile/profile.component';
import { LoginComponent } from './auth/login/login.component';

export const routes: Routes = [
    {
        path: "",
        component: LoginComponent
    },
    {
        path: 'home',
        component: HomeComponent
    },
    {
        path: 'profile',
        component: ProfileComponent
    },
    {
        path: "",
        redirectTo: "",
        pathMatch: "full"
    }
];
