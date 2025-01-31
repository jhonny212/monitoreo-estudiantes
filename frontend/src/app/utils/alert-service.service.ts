import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AlertServiceService {
  constructor() {}

  private messageSubject = new BehaviorSubject<{
    message: string;
    type: 'success' | 'error' | 'info' | 'warning';
  } | null>(null);
  message$ = this.messageSubject.asObservable();

  showMessage(
    message: string,
    type: 'success' | 'error' | 'info' | 'warning' = 'info'
  ) {
    this.messageSubject.next({ message, type });
    setTimeout(() => this.messageSubject.next(null), 3000);
  }
}
