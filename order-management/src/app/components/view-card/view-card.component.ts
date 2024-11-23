// src/app/components/view-card/view-card.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-view-card',
  templateUrl: './view-card.component.html',
  styleUrls: ['./view-card.component.css'],
  standalone: true,
  imports: [CommonModule, FormsModule] // Importar módulos necesarios
})
export class ViewCardComponent {
  orderId: string = '';
  orderData: any = null;

  constructor(private apiService: ApiService, private toastr: ToastrService) {}

  handleSearchOrder() {
    this.apiService.getOrderById(parseInt(this.orderId, 10)).subscribe(
      (data) => {
        this.orderData = data;
        this.toastr.success('Orden encontrada');
      },
      (error) => {
        this.toastr.error('Orden no encontrada');
        this.orderData = null; // Limpiar datos de la orden si no se encuentra
      }
    );
  }
}
