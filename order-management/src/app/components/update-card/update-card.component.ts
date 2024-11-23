// src/app/components/update-card/update-card.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-update-card',
  templateUrl: './update-card.component.html',
  styleUrls: ['./update-card.component.css'],
  standalone: true,
  imports: [CommonModule, FormsModule]
})
export class UpdateCardComponent {
  orderId: number | null = null; // OrderID para la búsqueda de la orden y detalle
  productId: number | null = null; // ProductID para la búsqueda del detalle de la orden
  orderData: any = null; // Datos de la orden inicializados como `null`
  orderDetailData: any = null; // Datos del detalle de la orden inicializados como `null`

  constructor(private apiService: ApiService, private toastr: ToastrService) {}

  // Método para buscar la orden existente
  handleSearchOrder() {
    if (this.orderId !== null) {
      this.apiService.getOrderById(this.orderId).subscribe(
        (data) => {
          // Convertir fechas al formato adecuado para mostrarlas en el formulario
          data.OrderDate = this.formatDateToInput(data.OrderDate);
          data.RequiredDate = this.formatDateToInput(data.RequiredDate);
          data.ShippedDate = this.formatDateToInput(data.ShippedDate);
          this.orderData = data;
          this.toastr.success('Orden encontrada');
        },
        (error) => {
          this.toastr.error('Orden no encontrada');
        }
      );
    } else {
      this.toastr.error('Por favor ingrese un OrderID');
    }
  }

  // Método para buscar el detalle de la orden
  handleSearchOrderDetail() {
    if (this.orderId !== null && this.productId !== null) {
      this.apiService.getOrderDetailById(this.orderId, this.productId).subscribe(
        (data) => {
          this.orderDetailData = data;
          this.toastr.success('Detalle de la orden encontrado');
        },
        (error) => {
          this.toastr.error('Detalle de la orden no encontrado');
        }
      );
    } else {
      this.toastr.error('Por favor ingrese OrderID y ProductID');
    }
  }

  // Método para actualizar la orden
  handleUpdateOrder() {
    if (this.orderData && this.orderId !== null) {
      // Convertir las fechas al formato adecuado antes de enviar la solicitud
      this.orderData.OrderDate = this.formatDateForSql(this.orderData.OrderDate);
      this.orderData.RequiredDate = this.formatDateForSql(this.orderData.RequiredDate);
      this.orderData.ShippedDate = this.formatDateForSql(this.orderData.ShippedDate);

      // Pasar el valor de `orderId` con seguridad, ya que no es `null` aquí
      this.apiService.updateOrder(this.orderId, this.orderData).subscribe(
        () => {
          this.toastr.success('Orden actualizada con éxito');
        },
        (error) => {
          this.toastr.error('Error al actualizar la orden');
        }
      );
    } else {
      this.toastr.error('No se ha encontrado una orden para actualizar');
    }
  }

  // Método para actualizar el detalle de la orden
  handleUpdateOrderDetail() {
    if (this.orderDetailData && this.orderId !== null && this.productId !== null) {
      this.apiService.updateOrderDetail(this.orderId, this.productId, this.orderDetailData).subscribe(
        () => {
          this.toastr.success('Detalle de la orden actualizado con éxito');
        },
        (error) => {
          this.toastr.error('Error al actualizar el detalle de la orden');
        }
      );
    } else {
      this.toastr.error('No se ha encontrado un detalle de orden para actualizar');
    }
  }

  // Método para formatear la fecha en el formato adecuado para SQL Server
  formatDateForSql(dateString: string): string {
    if (!dateString) return ''; // Devolver una cadena vacía si no hay fecha
    const date = new Date(dateString);
    return `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')} ${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}:${date.getSeconds().toString().padStart(2, '0')}`;
  }

  // Método para formatear la fecha para ser utilizada en el input de tipo datetime-local
  formatDateToInput(dateString: string): string {
    if (!dateString) return '';
    const date = new Date(dateString);
    return `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}T${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}`;
  }
}
