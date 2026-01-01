# Angular Cheatsheet - Complete Guide with Practical Examples

## Table of Contents
- [Setup & Installation](#setup--installation)
- [Project Structure](#project-structure)
- [Components](#components)
- [Templates & Data Binding](#templates--data-binding)
- [Directives](#directives)
- [Services & Dependency Injection](#services--dependency-injection)
- [Routing](#routing)
- [Forms](#forms)
- [HTTP Client](#http-client)
- [State Management](#state-management)
- [Performance Optimization](#performance-optimization)
- [Testing](#testing)
- [Best Practices & Tricks](#best-practices--tricks)

## Setup & Installation

### Angular CLI Installation
```bash
# Install Angular CLI globally
npm install -g @angular/cli

# Check version
ng version

# Create new project
ng new my-angular-app

# Navigate to project
cd my-angular-app

# Serve the application
ng serve

# Build for production
ng build --prod
```

### Project Generation Commands
```bash
# Generate component
ng generate component user-profile
ng g c user-profile

# Generate service
ng generate service user
ng g s user

# Generate module
ng generate module shared
ng g m shared

# Generate directive
ng generate directive highlight
ng g d highlight

# Generate pipe
ng generate pipe custom-date
ng g p custom-date

# Generate guard
ng generate guard auth
ng g g auth

# Generate interface
ng generate interface user
ng g i user
```

### Essential Dependencies
```bash
# Angular Material
ng add @angular/material

# Bootstrap
npm install bootstrap
npm install @ng-bootstrap/ng-bootstrap

# RxJS operators
npm install rxjs

# Forms
npm install @angular/forms

# HTTP client
npm install @angular/common/http

# Router
npm install @angular/router

# Animations
npm install @angular/animations
```

## Project Structure

### Recommended Folder Structure
```
src/
├── app/
│   ├── core/                 # Singleton services, guards
│   │   ├── guards/
│   │   ├── interceptors/
│   │   └── services/
│   ├── shared/               # Shared components, pipes, directives
│   │   ├── components/
│   │   ├── directives/
│   │   ├── pipes/
│   │   └── models/
│   ├── features/             # Feature modules
│   │   ├── user/
│   │   ├── product/
│   │   └── dashboard/
│   ├── layout/               # Layout components
│   │   ├── header/
│   │   ├── footer/
│   │   └── sidebar/
│   └── app.component.ts
├── assets/                   # Static assets
├── environments/             # Environment configurations
└── styles/                   # Global styles
```

## Components

### Basic Component Structure
```typescript
// user-profile.component.ts
import { Component, OnInit, OnDestroy, Input, Output, EventEmitter } from '@angular/core';
import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss']
})
export class UserProfileComponent implements OnInit, OnDestroy {
  @Input() user: User | null = null;
  @Input() isEditable: boolean = false;
  @Output() userUpdated = new EventEmitter<User>();
  @Output() deleteUser = new EventEmitter<number>();

  private destroy$ = new Subject<void>();
  
  isLoading = false;
  errorMessage = '';

  constructor(private userService: UserService) {}

  ngOnInit(): void {
    this.loadUserData();
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }

  loadUserData(): void {
    if (!this.user?.id) return;
    
    this.isLoading = true;
    this.userService.getUser(this.user.id)
      .pipe(takeUntil(this.destroy$))
      .subscribe({
        next: (user) => {
          this.user = user;
          this.isLoading = false;
        },
        error: (error) => {
          this.errorMessage = 'Failed to load user data';
          this.isLoading = false;
        }
      });
  }

  onUpdateUser(): void {
    if (this.user) {
      this.userUpdated.emit(this.user);
    }
  }

  onDeleteUser(): void {
    if (this.user?.id) {
      this.deleteUser.emit(this.user.id);
    }
  }
}
```

### Component Template
```html
<!-- user-profile.component.html -->
<div class="user-profile" *ngIf="user">
  <!-- Loading State -->
  <div *ngIf="isLoading" class="loading-spinner">
    <mat-spinner></mat-spinner>
    <p>Loading user data...</p>
  </div>

  <!-- Error State -->
  <div *ngIf="errorMessage" class="error-message">
    <mat-icon>error</mat-icon>
    <p>{{ errorMessage }}</p>
    <button mat-button (click)="loadUserData()">Retry</button>
  </div>

  <!-- User Content -->
  <div *ngIf="!isLoading && !errorMessage" class="user-content">
    <div class="user-header">
      <img [src]="user.avatar || 'assets/default-avatar.png'" 
           [alt]="user.name + ' avatar'"
           class="user-avatar">
      
      <div class="user-info">
        <h2>{{ user.name }}</h2>
        <p class="user-email">{{ user.email }}</p>
        <span class="user-status" 
              [class.active]="user.isActive"
              [class.inactive]="!user.isActive">
          {{ user.isActive ? 'Active' : 'Inactive' }}
        </span>
      </div>
    </div>

    <div class="user-details">
      <div class="detail-item">
        <label>Phone:</label>
        <span>{{ user.phone || 'Not provided' }}</span>
      </div>
      
      <div class="detail-item">
        <label>Department:</label>
        <span>{{ user.department }}</span>
      </div>
      
      <div class="detail-item">
        <label>Join Date:</label>
        <span>{{ user.joinDate | date:'mediumDate' }}</span>
      </div>
    </div>

    <!-- Actions -->
    <div class="user-actions" *ngIf="isEditable">
      <button mat-raised-button 
              color="primary" 
              (click)="onUpdateUser()">
        Update Profile
      </button>
      
      <button mat-raised-button 
              color="warn" 
              (click)="onDeleteUser()"
              [disabled]="isLoading">
        Delete User
      </button>
    </div>
  </div>
</div>
```

### Component Styling
```scss
// user-profile.component.scss
.user-profile {
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  background: white;

  .loading-spinner {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 40px;
    
    p {
      margin-top: 16px;
      color: #666;
    }
  }

  .error-message {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 40px;
    color: #f44336;
    
    mat-icon {
      font-size: 48px;
      margin-bottom: 16px;
    }
  }

  .user-header {
    display: flex;
    align-items: center;
    margin-bottom: 24px;
    
    .user-avatar {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      margin-right: 20px;
      object-fit: cover;
    }
    
    .user-info {
      h2 {
        margin: 0 0 8px 0;
        color: #333;
      }
      
      .user-email {
        margin: 0 0 8px 0;
        color: #666;
      }
      
      .user-status {
        padding: 4px 12px;
        border-radius: 16px;
        font-size: 12px;
        font-weight: 500;
        
        &.active {
          background: #e8f5e8;
          color: #2e7d32;
        }
        
        &.inactive {
          background: #ffebee;
          color: #c62828;
        }
      }
    }
  }

  .user-details {
    margin-bottom: 24px;
    
    .detail-item {
      display: flex;
      margin-bottom: 12px;
      
      label {
        font-weight: 500;
        min-width: 120px;
        color: #555;
      }
      
      span {
        color: #333;
      }
    }
  }

  .user-actions {
    display: flex;
    gap: 12px;
    
    button {
      min-width: 120px;
    }
  }
}

// Responsive design
@media (max-width: 768px) {
  .user-profile {
    padding: 16px;
    
    .user-header {
      flex-direction: column;
      text-align: center;
      
      .user-avatar {
        margin-right: 0;
        margin-bottom: 16px;
      }
    }
    
    .user-actions {
      flex-direction: column;
      
      button {
        width: 100%;
      }
    }
  }
}
```## 
Templates & Data Binding

### Interpolation & Property Binding
```typescript
// component.ts
export class DataBindingComponent {
  title = 'Angular Data Binding';
  imageUrl = 'assets/logo.png';
  isDisabled = false;
  user = {
    name: 'John Doe',
    age: 30,
    email: 'john@example.com'
  };
  
  dynamicClass = 'highlight';
  styles = {
    color: 'blue',
    fontSize: '16px'
  };
}
```

```html
<!-- template.html -->
<div class="data-binding-examples">
  <!-- Interpolation -->
  <h1>{{ title }}</h1>
  <p>User: {{ user.name }} ({{ user.age }} years old)</p>
  <p>Email: {{ user.email.toLowerCase() }}</p>
  
  <!-- Property Binding -->
  <img [src]="imageUrl" [alt]="title">
  <button [disabled]="isDisabled">Click me</button>
  
  <!-- Class Binding -->
  <div [class]="dynamicClass">Dynamic class</div>
  <div [class.active]="!isDisabled">Conditional class</div>
  <div [ngClass]="{'active': !isDisabled, 'disabled': isDisabled}">Multiple classes</div>
  
  <!-- Style Binding -->
  <p [style.color]="styles.color">Colored text</p>
  <p [style.font-size.px]="16">Font size in pixels</p>
  <div [ngStyle]="styles">Multiple styles</div>
  
  <!-- Attribute Binding -->
  <input [attr.placeholder]="'Enter ' + user.name">
  <div [attr.data-user-id]="user.id">User data</div>
</div>
```

### Event Binding
```typescript
// component.ts
export class EventBindingComponent {
  message = '';
  clickCount = 0;
  
  onClick(): void {
    this.clickCount++;
    this.message = `Button clicked ${this.clickCount} times`;
  }
  
  onInputChange(event: Event): void {
    const target = event.target as HTMLInputElement;
    this.message = target.value;
  }
  
  onKeyUp(event: KeyboardEvent): void {
    if (event.key === 'Enter') {
      console.log('Enter key pressed');
    }
  }
  
  onSubmit(form: any): void {
    console.log('Form submitted:', form.value);
  }
}
```

```html
<!-- template.html -->
<div class="event-binding-examples">
  <!-- Click Events -->
  <button (click)="onClick()">Click me ({{ clickCount }})</button>
  
  <!-- Input Events -->
  <input (input)="onInputChange($event)" placeholder="Type something">
  <input (keyup)="onKeyUp($event)" placeholder="Press Enter">
  
  <!-- Form Events -->
  <form (ngSubmit)="onSubmit(userForm)" #userForm="ngForm">
    <input name="username" ngModel required>
    <button type="submit">Submit</button>
  </form>
  
  <!-- Custom Events -->
  <app-child-component (customEvent)="onCustomEvent($event)"></app-child-component>
  
  <!-- Event with template reference -->
  <input #userInput (keyup)="message = userInput.value">
  <p>{{ message }}</p>
</div>
```

### Two-Way Data Binding
```typescript
// component.ts
export class TwoWayBindingComponent {
  username = '';
  isChecked = false;
  selectedOption = 'option1';
  
  options = [
    { value: 'option1', label: 'Option 1' },
    { value: 'option2', label: 'Option 2' },
    { value: 'option3', label: 'Option 3' }
  ];
}
```

```html
<!-- template.html -->
<div class="two-way-binding-examples">
  <!-- Input field -->
  <input [(ngModel)]="username" placeholder="Username">
  <p>Hello, {{ username }}!</p>
  
  <!-- Checkbox -->
  <label>
    <input type="checkbox" [(ngModel)]="isChecked">
    Subscribe to newsletter
  </label>
  <p *ngIf="isChecked">Thank you for subscribing!</p>
  
  <!-- Select dropdown -->
  <select [(ngModel)]="selectedOption">
    <option *ngFor="let option of options" [value]="option.value">
      {{ option.label }}
    </option>
  </select>
  <p>Selected: {{ selectedOption }}</p>
  
  <!-- Custom two-way binding -->
  <app-custom-input [(value)]="username"></app-custom-input>
</div>
```

## Directives

### Structural Directives
```typescript
// component.ts
export class DirectivesComponent {
  users = [
    { id: 1, name: 'John', isActive: true, role: 'admin' },
    { id: 2, name: 'Jane', isActive: false, role: 'user' },
    { id: 3, name: 'Bob', isActive: true, role: 'user' }
  ];
  
  showUsers = true;
  currentUser = this.users[0];
  
  trackByUserId(index: number, user: any): number {
    return user.id;
  }
}
```

```html
<!-- template.html -->
<div class="directives-examples">
  <!-- *ngIf -->
  <div *ngIf="showUsers; else noUsers">
    <h3>User List</h3>
    
    <!-- *ngFor with trackBy -->
    <div *ngFor="let user of users; trackBy: trackByUserId; 
                 let i = index; let first = first; let last = last"
         class="user-item"
         [class.first]="first"
         [class.last]="last">
      
      <span>{{ i + 1 }}. {{ user.name }}</span>
      
      <!-- Nested *ngIf -->
      <span *ngIf="user.isActive" class="status active">Active</span>
      <span *ngIf="!user.isActive" class="status inactive">Inactive</span>
      
      <!-- *ngIf with else -->
      <span *ngIf="user.role === 'admin'; else regularUser" class="role admin">
        Administrator
      </span>
      <ng-template #regularUser>
        <span class="role user">User</span>
      </ng-template>
    </div>
  </div>
  
  <!-- ng-template for else condition -->
  <ng-template #noUsers>
    <p>No users found.</p>
  </ng-template>
  
  <!-- *ngSwitch -->
  <div [ngSwitch]="currentUser.role">
    <div *ngSwitchCase="'admin'" class="admin-panel">
      <h4>Admin Panel</h4>
      <p>Welcome, Administrator!</p>
    </div>
    
    <div *ngSwitchCase="'user'" class="user-panel">
      <h4>User Dashboard</h4>
      <p>Welcome, {{ currentUser.name }}!</p>
    </div>
    
    <div *ngSwitchDefault class="guest-panel">
      <h4>Guest Access</h4>
      <p>Please log in to continue.</p>
    </div>
  </div>
  
  <!-- ng-container for grouping -->
  <ng-container *ngIf="showUsers">
    <h4>Active Users</h4>
    <ng-container *ngFor="let user of users">
      <p *ngIf="user.isActive">{{ user.name }}</p>
    </ng-container>
  </ng-container>
</div>
```

### Custom Directive
```typescript
// highlight.directive.ts
import { Directive, ElementRef, HostListener, Input, Renderer2 } from '@angular/core';

@Directive({
  selector: '[appHighlight]'
})
export class HighlightDirective {
  @Input() appHighlight = 'yellow';
  @Input() defaultColor = 'transparent';

  constructor(
    private el: ElementRef,
    private renderer: Renderer2
  ) {}

  @HostListener('mouseenter') onMouseEnter() {
    this.highlight(this.appHighlight);
  }

  @HostListener('mouseleave') onMouseLeave() {
    this.highlight(this.defaultColor);
  }

  private highlight(color: string) {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', color);
  }
}
```

```html
<!-- Usage -->
<p appHighlight="lightblue" defaultColor="white">
  Hover over this text to see the highlight effect!
</p>

<div appHighlight="lightgreen">
  This div will be highlighted in light green.
</div>
```

## Services & Dependency Injection

### Basic Service
```typescript
// user.service.ts
import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, BehaviorSubject, throwError } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

export interface User {
  id: number;
  name: string;
  email: string;
  isActive: boolean;
  role: string;
}

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiUrl = 'https://api.example.com/users';
  private usersSubject = new BehaviorSubject<User[]>([]);
  
  // Public observable for components to subscribe to
  users$ = this.usersSubject.asObservable();

  constructor(private http: HttpClient) {
    this.loadUsers();
  }

  // Get all users
  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.apiUrl)
      .pipe(
        tap(users => this.usersSubject.next(users)),
        catchError(this.handleError)
      );
  }

  // Get user by ID
  getUser(id: number): Observable<User> {
    return this.http.get<User>(`${this.apiUrl}/${id}`)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Create new user
  createUser(user: Omit<User, 'id'>): Observable<User> {
    return this.http.post<User>(this.apiUrl, user)
      .pipe(
        tap(newUser => {
          const currentUsers = this.usersSubject.value;
          this.usersSubject.next([...currentUsers, newUser]);
        }),
        catchError(this.handleError)
      );
  }

  // Update user
  updateUser(id: number, user: Partial<User>): Observable<User> {
    return this.http.put<User>(`${this.apiUrl}/${id}`, user)
      .pipe(
        tap(updatedUser => {
          const currentUsers = this.usersSubject.value;
          const index = currentUsers.findIndex(u => u.id === id);
          if (index !== -1) {
            currentUsers[index] = updatedUser;
            this.usersSubject.next([...currentUsers]);
          }
        }),
        catchError(this.handleError)
      );
  }

  // Delete user
  deleteUser(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`)
      .pipe(
        tap(() => {
          const currentUsers = this.usersSubject.value;
          const filteredUsers = currentUsers.filter(u => u.id !== id);
          this.usersSubject.next(filteredUsers);
        }),
        catchError(this.handleError)
      );
  }

  // Search users
  searchUsers(query: string): Observable<User[]> {
    return this.users$.pipe(
      map(users => users.filter(user => 
        user.name.toLowerCase().includes(query.toLowerCase()) ||
        user.email.toLowerCase().includes(query.toLowerCase())
      ))
    );
  }

  // Get active users
  getActiveUsers(): Observable<User[]> {
    return this.users$.pipe(
      map(users => users.filter(user => user.isActive))
    );
  }

  private loadUsers(): void {
    this.getUsers().subscribe();
  }

  private handleError(error: HttpErrorResponse): Observable<never> {
    let errorMessage = 'An unknown error occurred';
    
    if (error.error instanceof ErrorEvent) {
      // Client-side error
      errorMessage = `Error: ${error.error.message}`;
    } else {
      // Server-side error
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    
    console.error(errorMessage);
    return throwError(() => new Error(errorMessage));
  }
}
```

### Service with State Management
```typescript
// notification.service.ts
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

export interface Notification {
  id: string;
  message: string;
  type: 'success' | 'error' | 'warning' | 'info';
  duration?: number;
}

@Injectable({
  providedIn: 'root'
})
export class NotificationService {
  private notificationsSubject = new BehaviorSubject<Notification[]>([]);
  notifications$ = this.notificationsSubject.asObservable();

  show(message: string, type: Notification['type'] = 'info', duration = 5000): void {
    const notification: Notification = {
      id: this.generateId(),
      message,
      type,
      duration
    };

    const currentNotifications = this.notificationsSubject.value;
    this.notificationsSubject.next([...currentNotifications, notification]);

    if (duration > 0) {
      setTimeout(() => {
        this.remove(notification.id);
      }, duration);
    }
  }

  success(message: string, duration?: number): void {
    this.show(message, 'success', duration);
  }

  error(message: string, duration?: number): void {
    this.show(message, 'error', duration);
  }

  warning(message: string, duration?: number): void {
    this.show(message, 'warning', duration);
  }

  info(message: string, duration?: number): void {
    this.show(message, 'info', duration);
  }

  remove(id: string): void {
    const currentNotifications = this.notificationsSubject.value;
    const filteredNotifications = currentNotifications.filter(n => n.id !== id);
    this.notificationsSubject.next(filteredNotifications);
  }

  clear(): void {
    this.notificationsSubject.next([]);
  }

  private generateId(): string {
    return Math.random().toString(36).substr(2, 9);
  }
}
```

## Routing

### Basic Routing Setup
```typescript
// app-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './core/guards/auth.guard';
import { AdminGuard } from './core/guards/admin.guard';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { 
    path: 'dashboard', 
    component: DashboardComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'users',
    canActivate: [AuthGuard],
    children: [
      { path: '', component: UserListComponent },
      { path: 'new', component: UserFormComponent },
      { path: ':id', component: UserDetailComponent },
      { path: ':id/edit', component: UserFormComponent }
    ]
  },
  {
    path: 'admin',
    canActivate: [AuthGuard, AdminGuard],
    loadChildren: () => import('./features/admin/admin.module').then(m => m.AdminModule)
  },
  { path: '**', component: NotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {
    enableTracing: false, // Set to true for debugging
    preloadingStrategy: PreloadAllModules
  })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

### Route Guards
```typescript
// auth.guard.ts
import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from '../services/auth.service';
import { map, take } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<boolean> {
    return this.authService.isAuthenticated$.pipe(
      take(1),
      map(isAuthenticated => {
        if (isAuthenticated) {
          return true;
        } else {
          this.router.navigate(['/login'], { 
            queryParams: { returnUrl: state.url } 
          });
          return false;
        }
      })
    );
  }
}

// can-deactivate.guard.ts
export interface CanComponentDeactivate {
  canDeactivate: () => Observable<boolean> | Promise<boolean> | boolean;
}

@Injectable({
  providedIn: 'root'
})
export class CanDeactivateGuard implements CanDeactivate<CanComponentDeactivate> {
  canDeactivate(component: CanComponentDeactivate): Observable<boolean> | Promise<boolean> | boolean {
    return component.canDeactivate ? component.canDeactivate() : true;
  }
}
```

### Navigation Component
```typescript
// navigation.component.ts
import { Component, OnInit } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';
import { filter } from 'rxjs/operators';

@Component({
  selector: 'app-navigation',
  template: `
    <nav class="navigation">
      <div class="nav-brand">
        <a routerLink="/">MyApp</a>
      </div>
      
      <ul class="nav-links">
        <li>
          <a routerLink="/dashboard" 
             routerLinkActive="active"
             [routerLinkActiveOptions]="{exact: true}">
            Dashboard
          </a>
        </li>
        <li>
          <a routerLink="/users" 
             routerLinkActive="active">
            Users
          </a>
        </li>
        <li *ngIf="isAdmin">
          <a routerLink="/admin" 
             routerLinkActive="active">
            Admin
          </a>
        </li>
      </ul>
      
      <div class="nav-actions">
        <button (click)="logout()">Logout</button>
      </div>
    </nav>
    
    <!-- Breadcrumb -->
    <div class="breadcrumb" *ngIf="breadcrumbs.length > 0">
      <span *ngFor="let crumb of breadcrumbs; let last = last">
        <a *ngIf="!last" [routerLink]="crumb.url">{{ crumb.label }}</a>
        <span *ngIf="last">{{ crumb.label }}</span>
        <span *ngIf="!last"> / </span>
      </span>
    </div>
  `
})
export class NavigationComponent implements OnInit {
  isAdmin = false;
  breadcrumbs: Array<{label: string, url: string}> = [];

  constructor(
    private router: Router,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    // Listen to route changes for breadcrumbs
    this.router.events.pipe(
      filter(event => event instanceof NavigationEnd)
    ).subscribe(() => {
      this.buildBreadcrumbs();
    });
  }

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/login']);
  }

  private buildBreadcrumbs(): void {
    // Implementation for building breadcrumbs based on current route
    const urlSegments = this.router.url.split('/').filter(segment => segment);
    this.breadcrumbs = urlSegments.map((segment, index) => ({
      label: this.formatSegment(segment),
      url: '/' + urlSegments.slice(0, index + 1).join('/')
    }));
  }

  private formatSegment(segment: string): string {
    return segment.charAt(0).toUpperCase() + segment.slice(1);
  }
}
```

## Forms

### Reactive Forms
```typescript
// user-form.component.ts
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, FormArray } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-user-form',
  templateUrl: './user-form.component.html'
})
export class UserFormComponent implements OnInit {
  userForm: FormGroup;
  isEditMode = false;
  userId: number | null = null;
  
  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private userService: UserService
  ) {
    this.userForm = this.createForm();
  }

  ngOnInit(): void {
    this.userId = this.route.snapshot.params['id'];
    this.isEditMode = !!this.userId;
    
    if (this.isEditMode) {
      this.loadUser();
    }
  }

  createForm(): FormGroup {
    return this.fb.group({
      name: ['', [Validators.required, Validators.minLength(2)]],
      email: ['', [Validators.required, Validators.email]],
      phone: ['', [Validators.pattern(/^\d{10}$/)]],
      address: this.fb.group({
        street: ['', Validators.required],
        city: ['', Validators.required],
        zipCode: ['', [Validators.required, Validators.pattern(/^\d{5}$/)]]
      }),
      skills: this.fb.array([]),
      isActive: [true],
      role: ['user', Validators.required]
    });
  }

  get skills(): FormArray {
    return this.userForm.get('skills') as FormArray;
  }

  addSkill(): void {
    const skillGroup = this.fb.group({
      name: ['', Validators.required],
      level: ['beginner', Validators.required]
    });
    this.skills.push(skillGroup);
  }

  removeSkill(index: number): void {
    this.skills.removeAt(index);
  }

  loadUser(): void {
    if (this.userId) {
      this.userService.getUser(this.userId).subscribe(user => {
        this.userForm.patchValue(user);
        
        // Load skills
        if (user.skills) {
          user.skills.forEach(skill => {
            const skillGroup = this.fb.group({
              name: [skill.name, Validators.required],
              level: [skill.level, Validators.required]
            });
            this.skills.push(skillGroup);
          });
        }
      });
    }
  }

  onSubmit(): void {
    if (this.userForm.valid) {
      const formValue = this.userForm.value;
      
      if (this.isEditMode) {
        this.userService.updateUser(this.userId!, formValue).subscribe(() => {
          this.router.navigate(['/users']);
        });
      } else {
        this.userService.createUser(formValue).subscribe(() => {
          this.router.navigate(['/users']);
        });
      }
    } else {
      this.markFormGroupTouched();
    }
  }

  private markFormGroupTouched(): void {
    Object.keys(this.userForm.controls).forEach(key => {
      const control = this.userForm.get(key);
      control?.markAsTouched();
      
      if (control instanceof FormGroup) {
        this.markFormGroupTouched();
      }
    });
  }

  // Helper methods for template
  isFieldInvalid(fieldName: string): boolean {
    const field = this.userForm.get(fieldName);
    return !!(field && field.invalid && (field.dirty || field.touched));
  }

  getFieldError(fieldName: string): string {
    const field = this.userForm.get(fieldName);
    if (field?.errors) {
      if (field.errors['required']) return `${fieldName} is required`;
      if (field.errors['email']) return 'Invalid email format';
      if (field.errors['minlength']) return `Minimum length is ${field.errors['minlength'].requiredLength}`;
      if (field.errors['pattern']) return `Invalid ${fieldName} format`;
    }
    return '';
  }
}
```### Form Tem
plate
```html
<!-- user-form.component.html -->
<div class="user-form-container">
  <h2>{{ isEditMode ? 'Edit User' : 'Create User' }}</h2>
  
  <form [formGroup]="userForm" (ngSubmit)="onSubmit()" novalidate>
    <!-- Basic Information -->
    <div class="form-section">
      <h3>Basic Information</h3>
      
      <div class="form-field">
        <label for="name">Name *</label>
        <input id="name" 
               type="text" 
               formControlName="name"
               [class.error]="isFieldInvalid('name')">
        <div class="error-message" *ngIf="isFieldInvalid('name')">
          {{ getFieldError('name') }}
        </div>
      </div>
      
      <div class="form-field">
        <label for="email">Email *</label>
        <input id="email" 
               type="email" 
               formControlName="email"
               [class.error]="isFieldInvalid('email')">
        <div class="error-message" *ngIf="isFieldInvalid('email')">
          {{ getFieldError('email') }}
        </div>
      </div>
      
      <div class="form-field">
        <label for="phone">Phone</label>
        <input id="phone" 
               type="tel" 
               formControlName="phone"
               placeholder="1234567890"
               [class.error]="isFieldInvalid('phone')">
        <div class="error-message" *ngIf="isFieldInvalid('phone')">
          {{ getFieldError('phone') }}
        </div>
      </div>
    </div>

    <!-- Address Information -->
    <div class="form-section" formGroupName="address">
      <h3>Address</h3>
      
      <div class="form-field">
        <label for="street">Street *</label>
        <input id="street" 
               type="text" 
               formControlName="street"
               [class.error]="isFieldInvalid('address.street')">
        <div class="error-message" *ngIf="isFieldInvalid('address.street')">
          Street is required
        </div>
      </div>
      
      <div class="form-row">
        <div class="form-field">
          <label for="city">City *</label>
          <input id="city" 
                 type="text" 
                 formControlName="city"
                 [class.error]="isFieldInvalid('address.city')">
          <div class="error-message" *ngIf="isFieldInvalid('address.city')">
            City is required
          </div>
        </div>
        
        <div class="form-field">
          <label for="zipCode">Zip Code *</label>
          <input id="zipCode" 
                 type="text" 
                 formControlName="zipCode"
                 placeholder="12345"
                 [class.error]="isFieldInvalid('address.zipCode')">
          <div class="error-message" *ngIf="isFieldInvalid('address.zipCode')">
            Valid zip code required
          </div>
        </div>
      </div>
    </div>

    <!-- Skills Section -->
    <div class="form-section">
      <h3>Skills</h3>
      
      <div formArrayName="skills">
        <div *ngFor="let skill of skills.controls; let i = index" 
             [formGroupName]="i" 
             class="skill-item">
          
          <div class="form-row">
            <div class="form-field">
              <label>Skill Name</label>
              <input type="text" formControlName="name" placeholder="e.g., Angular">
            </div>
            
            <div class="form-field">
              <label>Level</label>
              <select formControlName="level">
                <option value="beginner">Beginner</option>
                <option value="intermediate">Intermediate</option>
                <option value="advanced">Advanced</option>
                <option value="expert">Expert</option>
              </select>
            </div>
            
            <button type="button" 
                    class="remove-btn" 
                    (click)="removeSkill(i)">
              Remove
            </button>
          </div>
        </div>
      </div>
      
      <button type="button" 
              class="add-btn" 
              (click)="addSkill()">
        Add Skill
      </button>
    </div>

    <!-- User Settings -->
    <div class="form-section">
      <h3>Settings</h3>
      
      <div class="form-field">
        <label>
          <input type="checkbox" formControlName="isActive">
          Active User
        </label>
      </div>
      
      <div class="form-field">
        <label for="role">Role *</label>
        <select id="role" formControlName="role">
          <option value="user">User</option>
          <option value="admin">Admin</option>
          <option value="moderator">Moderator</option>
        </select>
      </div>
    </div>

    <!-- Form Actions -->
    <div class="form-actions">
      <button type="button" 
              class="btn-secondary" 
              (click)="router.navigate(['/users'])">
        Cancel
      </button>
      
      <button type="submit" 
              class="btn-primary"
              [disabled]="userForm.invalid">
        {{ isEditMode ? 'Update' : 'Create' }} User
      </button>
    </div>
  </form>
  
  <!-- Form Debug Info (Development only) -->
  <div class="debug-info" *ngIf="!environment.production">
    <h4>Form Debug</h4>
    <p>Form Valid: {{ userForm.valid }}</p>
    <p>Form Value: {{ userForm.value | json }}</p>
    <p>Form Errors: {{ userForm.errors | json }}</p>
  </div>
</div>
```

### Custom Validators
```typescript
// validators.ts
import { AbstractControl, ValidationErrors, ValidatorFn } from '@angular/forms';

export class CustomValidators {
  // Password strength validator
  static passwordStrength(): ValidatorFn {
    return (control: AbstractControl): ValidationErrors | null => {
      const value = control.value;
      if (!value) return null;

      const hasNumber = /[0-9]/.test(value);
      const hasUpper = /[A-Z]/.test(value);
      const hasLower = /[a-z]/.test(value);
      const hasSpecial = /[#?!@$%^&*-]/.test(value);
      const isLengthValid = value.length >= 8;

      const passwordValid = hasNumber && hasUpper && hasLower && hasSpecial && isLengthValid;

      return passwordValid ? null : {
        passwordStrength: {
          hasNumber,
          hasUpper,
          hasLower,
          hasSpecial,
          isLengthValid
        }
      };
    };
  }

  // Confirm password validator
  static confirmPassword(passwordField: string): ValidatorFn {
    return (control: AbstractControl): ValidationErrors | null => {
      const password = control.parent?.get(passwordField);
      const confirmPassword = control.value;

      if (!password || !confirmPassword) return null;

      return password.value === confirmPassword ? null : { confirmPassword: true };
    };
  }

  // Age range validator
  static ageRange(min: number, max: number): ValidatorFn {
    return (control: AbstractControl): ValidationErrors | null => {
      const age = control.value;
      if (!age) return null;

      return age >= min && age <= max ? null : { ageRange: { min, max, actual: age } };
    };
  }

  // Async email uniqueness validator
  static emailUnique(userService: UserService): ValidatorFn {
    return (control: AbstractControl): Observable<ValidationErrors | null> => {
      if (!control.value) {
        return of(null);
      }

      return userService.checkEmailExists(control.value).pipe(
        map(exists => exists ? { emailExists: true } : null),
        catchError(() => of(null))
      );
    };
  }
}
```

## HTTP Client

### HTTP Interceptor
```typescript
// auth.interceptor.ts
import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, switchMap } from 'rxjs/operators';
import { AuthService } from '../services/auth.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor(private authService: AuthService) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // Add auth token to requests
    const authToken = this.authService.getToken();
    
    if (authToken) {
      req = req.clone({
        setHeaders: {
          Authorization: `Bearer ${authToken}`
        }
      });
    }

    return next.handle(req).pipe(
      catchError((error: HttpErrorResponse) => {
        if (error.status === 401) {
          // Token expired, try to refresh
          return this.authService.refreshToken().pipe(
            switchMap(() => {
              // Retry the original request with new token
              const newToken = this.authService.getToken();
              const newReq = req.clone({
                setHeaders: {
                  Authorization: `Bearer ${newToken}`
                }
              });
              return next.handle(newReq);
            }),
            catchError(() => {
              // Refresh failed, redirect to login
              this.authService.logout();
              return throwError(() => error);
            })
          );
        }
        
        return throwError(() => error);
      })
    );
  }
}

// loading.interceptor.ts
@Injectable()
export class LoadingInterceptor implements HttpInterceptor {
  constructor(private loadingService: LoadingService) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    this.loadingService.setLoading(true);

    return next.handle(req).pipe(
      finalize(() => this.loadingService.setLoading(false))
    );
  }
}
```

### HTTP Service with Error Handling
```typescript
// api.service.ts
import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry, timeout } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'https://api.example.com';

  constructor(
    private http: HttpClient,
    private notificationService: NotificationService
  ) {}

  // Generic GET method
  get<T>(endpoint: string, params?: any): Observable<T> {
    let httpParams = new HttpParams();
    
    if (params) {
      Object.keys(params).forEach(key => {
        if (params[key] !== null && params[key] !== undefined) {
          httpParams = httpParams.set(key, params[key].toString());
        }
      });
    }

    return this.http.get<T>(`${this.baseUrl}/${endpoint}`, { params: httpParams })
      .pipe(
        timeout(10000), // 10 second timeout
        retry(2), // Retry failed requests twice
        catchError(this.handleError.bind(this))
      );
  }

  // Generic POST method
  post<T>(endpoint: string, data: any): Observable<T> {
    return this.http.post<T>(`${this.baseUrl}/${endpoint}`, data)
      .pipe(
        timeout(10000),
        catchError(this.handleError.bind(this))
      );
  }

  // Generic PUT method
  put<T>(endpoint: string, data: any): Observable<T> {
    return this.http.put<T>(`${this.baseUrl}/${endpoint}`, data)
      .pipe(
        timeout(10000),
        catchError(this.handleError.bind(this))
      );
  }

  // Generic DELETE method
  delete<T>(endpoint: string): Observable<T> {
    return this.http.delete<T>(`${this.baseUrl}/${endpoint}`)
      .pipe(
        timeout(10000),
        catchError(this.handleError.bind(this))
      );
  }

  // File upload
  uploadFile(endpoint: string, file: File, additionalData?: any): Observable<any> {
    const formData = new FormData();
    formData.append('file', file);
    
    if (additionalData) {
      Object.keys(additionalData).forEach(key => {
        formData.append(key, additionalData[key]);
      });
    }

    return this.http.post(`${this.baseUrl}/${endpoint}`, formData, {
      reportProgress: true,
      observe: 'events'
    }).pipe(
      catchError(this.handleError.bind(this))
    );
  }

  private handleError(error: HttpErrorResponse): Observable<never> {
    let errorMessage = 'An unknown error occurred';
    
    if (error.error instanceof ErrorEvent) {
      // Client-side error
      errorMessage = `Error: ${error.error.message}`;
    } else {
      // Server-side error
      switch (error.status) {
        case 400:
          errorMessage = 'Bad Request: Please check your input';
          break;
        case 401:
          errorMessage = 'Unauthorized: Please log in again';
          break;
        case 403:
          errorMessage = 'Forbidden: You do not have permission';
          break;
        case 404:
          errorMessage = 'Not Found: The requested resource was not found';
          break;
        case 500:
          errorMessage = 'Internal Server Error: Please try again later';
          break;
        default:
          errorMessage = `Error ${error.status}: ${error.message}`;
      }
    }
    
    this.notificationService.error(errorMessage);
    return throwError(() => new Error(errorMessage));
  }
}
```

## Performance Optimization

### OnPush Change Detection
```typescript
// optimized.component.ts
import { Component, ChangeDetectionStrategy, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-optimized',
  template: `
    <div class="optimized-component">
      <!-- Using async pipe for automatic subscription management -->
      <div *ngIf="data$ | async as data">
        <h3>{{ data.title }}</h3>
        <p>{{ data.description }}</p>
      </div>
      
      <!-- Trackby function for ngFor -->
      <div *ngFor="let item of items; trackBy: trackByFn" class="item">
        {{ item.name }}
      </div>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class OptimizedComponent implements OnInit {
  @Input() items: any[] = [];
  data$: Observable<any>;

  constructor(private dataService: DataService) {}

  ngOnInit(): void {
    this.data$ = this.dataService.getData();
  }

  trackByFn(index: number, item: any): any {
    return item.id || index;
  }
}
```

### Lazy Loading Module
```typescript
// feature.module.ts
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [
    FeatureComponent,
    FeatureListComponent,
    FeatureDetailComponent
  ],
  imports: [
    CommonModule,
    RouterModule.forChild([
      { path: '', component: FeatureListComponent },
      { path: ':id', component: FeatureDetailComponent }
    ])
  ]
})
export class FeatureModule {}

// In app-routing.module.ts
{
  path: 'feature',
  loadChildren: () => import('./features/feature/feature.module').then(m => m.FeatureModule)
}
```

### Virtual Scrolling
```typescript
// virtual-scroll.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-virtual-scroll',
  template: `
    <cdk-virtual-scroll-viewport itemSize="50" class="viewport">
      <div *cdkVirtualFor="let item of items; trackBy: trackByFn" class="item">
        {{ item.name }}
      </div>
    </cdk-virtual-scroll-viewport>
  `,
  styles: [`
    .viewport {
      height: 400px;
      width: 100%;
    }
    .item {
      height: 50px;
      display: flex;
      align-items: center;
      padding: 0 16px;
      border-bottom: 1px solid #ccc;
    }
  `]
})
export class VirtualScrollComponent {
  items = Array.from({ length: 10000 }, (_, i) => ({ id: i, name: `Item ${i}` }));

  trackByFn(index: number, item: any): number {
    return item.id;
  }
}
```

## Best Practices & Tricks

### Smart vs Dumb Components Pattern
```typescript
// Smart Component (Container)
@Component({
  selector: 'app-user-container',
  template: `
    <app-user-list
      [users]="users$ | async"
      [loading]="loading$ | async"
      (userSelected)="onUserSelected($event)"
      (userDeleted)="onUserDeleted($event)">
    </app-user-list>
  `
})
export class UserContainerComponent {
  users$ = this.userService.users$;
  loading$ = this.userService.loading$;

  constructor(private userService: UserService) {}

  onUserSelected(user: User): void {
    this.router.navigate(['/users', user.id]);
  }

  onUserDeleted(userId: number): void {
    this.userService.deleteUser(userId).subscribe();
  }
}

// Dumb Component (Presentational)
@Component({
  selector: 'app-user-list',
  template: `
    <div class="user-list">
      <div *ngIf="loading" class="loading">Loading...</div>
      
      <div *ngFor="let user of users; trackBy: trackByUserId" 
           class="user-item"
           (click)="userSelected.emit(user)">
        <span>{{ user.name }}</span>
        <button (click)="$event.stopPropagation(); userDeleted.emit(user.id)">
          Delete
        </button>
      </div>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class UserListComponent {
  @Input() users: User[] | null = null;
  @Input() loading: boolean | null = false;
  @Output() userSelected = new EventEmitter<User>();
  @Output() userDeleted = new EventEmitter<number>();

  trackByUserId(index: number, user: User): number {
    return user.id;
  }
}
```

### Error Handling Strategy
```typescript
// error-handler.service.ts
import { Injectable, ErrorHandler } from '@angular/core';
import { HttpErrorResponse } from '@angular/common/http';

@Injectable()
export class GlobalErrorHandler implements ErrorHandler {
  constructor(private notificationService: NotificationService) {}

  handleError(error: any): void {
    console.error('Global error:', error);

    if (error instanceof HttpErrorResponse) {
      // HTTP error
      this.handleHttpError(error);
    } else if (error instanceof TypeError) {
      // JavaScript error
      this.notificationService.error('A technical error occurred. Please refresh the page.');
    } else {
      // Other errors
      this.notificationService.error('An unexpected error occurred.');
    }
  }

  private handleHttpError(error: HttpErrorResponse): void {
    switch (error.status) {
      case 0:
        this.notificationService.error('Network error. Please check your connection.');
        break;
      case 500:
        this.notificationService.error('Server error. Please try again later.');
        break;
      default:
        this.notificationService.error(`Error ${error.status}: ${error.message}`);
    }
  }
}

// In app.module.ts
providers: [
  { provide: ErrorHandler, useClass: GlobalErrorHandler }
]
```

### Environment Configuration
```typescript
// environment.ts
export const environment = {
  production: false,
  apiUrl: 'http://localhost:3000/api',
  features: {
    enableLogging: true,
    enableAnalytics: false,
    maxFileSize: 5 * 1024 * 1024 // 5MB
  },
  auth: {
    tokenKey: 'auth_token',
    refreshTokenKey: 'refresh_token'
  }
};

// environment.prod.ts
export const environment = {
  production: true,
  apiUrl: 'https://api.myapp.com',
  features: {
    enableLogging: false,
    enableAnalytics: true,
    maxFileSize: 10 * 1024 * 1024 // 10MB
  },
  auth: {
    tokenKey: 'auth_token',
    refreshTokenKey: 'refresh_token'
  }
};
```

### Utility Functions and Helpers
```typescript
// utils.ts
export class Utils {
  // Debounce function
  static debounce<T extends (...args: any[]) => any>(
    func: T,
    delay: number
  ): (...args: Parameters<T>) => void {
    let timeoutId: ReturnType<typeof setTimeout>;
    return (...args: Parameters<T>) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => func.apply(null, args), delay);
    };
  }

  // Deep clone object
  static deepClone<T>(obj: T): T {
    return JSON.parse(JSON.stringify(obj));
  }

  // Generate unique ID
  static generateId(): string {
    return Math.random().toString(36).substr(2, 9);
  }

  // Format file size
  static formatFileSize(bytes: number): string {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }

  // Validate email
  static isValidEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
}

// Custom pipes
@Pipe({ name: 'fileSize' })
export class FileSizePipe implements PipeTransform {
  transform(bytes: number): string {
    return Utils.formatFileSize(bytes);
  }
}

@Pipe({ name: 'truncate' })
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit = 25, completeWords = false, ellipsis = '...'): string {
    if (completeWords) {
      limit = value.substr(0, limit).lastIndexOf(' ');
    }
    return value.length > limit ? value.substr(0, limit) + ellipsis : value;
  }
}
```

This comprehensive Angular cheatsheet covers all essential concepts with practical, real-world examples. Each section includes working code that you can directly use in your projects, along with best practices and performance optimization techniques used in production applications.