// src/app/services/api.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private readonly API_BASE_URL = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }

  createOrder(orderData: any): Observable<any> {
    return this.http.post(`${this.API_BASE_URL}/orders/`, orderData);
  }

  createOrderDetail(orderDetailData: any): Observable<any> {
    return this.http.post(`${this.API_BASE_URL}/order-details/`, orderDetailData);
  }

  getOrderById(orderId: number): Observable<any> {
    return this.http.get(`${this.API_BASE_URL}/orders/${orderId}`);
  }

  getOrderDetailById(orderId: number, productId: number): Observable<any> {
    return this.http.get(`${this.API_BASE_URL}/order-details/${orderId}/${productId}`);
  }

  updateOrder(orderId: number, orderData: any): Observable<any> {
    return this.http.put(`${this.API_BASE_URL}/orders/${orderId}`, orderData);
  }

  updateOrderDetail(orderId: number, productId: number, orderDetailData: any): Observable<any> {
    return this.http.put(`${this.API_BASE_URL}/order-details/${orderId}/${productId}`, orderDetailData);
  }

  deleteOrder(orderId: number): Observable<any> {
    return this.http.delete(`${this.API_BASE_URL}/orders/${orderId}`);
  }

  deleteOrderDetail(orderId: number, productId: number): Observable<any> {
    return this.http.delete(`${this.API_BASE_URL}/order-details/${orderId}/${productId}`);
  }
}
