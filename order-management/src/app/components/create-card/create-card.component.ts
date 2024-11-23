// src/app/components/create-card/create-card.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-create-card',
  templateUrl: './create-card.component.html',
  styleUrls: ['./create-card.component.css'],
  standalone: true,
  imports: [CommonModule, FormsModule]
})
export class CreateCardComponent {
  orderData: any = {
    CustomerID: '',
    EmployeeID: '',
    OrderDate: '',
    RequiredDate: '',
    ShippedDate: '',
    ShipVia: '',
    Freight: '',
    ShipName: '',
    ShipAddress: '',
    ShipCity: '',
    ShipRegion: '',
    ShipPostalCode: '',
    ShipCountry: ''
  };

  orderDetailData: any = {
    ProductID: '',
    UnitPrice: '',
    Quantity: '',
    Discount: ''
  };

  constructor(private apiService: ApiService, private toastr: ToastrService) {}

  // Método para formatear la fecha en el formato adecuado para SQL Server
  formatDateForSql(dateString: string): string {
    if (!dateString) return ''; // Devolver una cadena vacía si no hay fecha
    const date = new Date(dateString);
    return `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')} ${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}:${date.getSeconds().toString().padStart(2, '0')}`;
  }

  handleCreateOrderAndDetail() {
    // Convertir las fechas al formato adecuado antes de enviar la solicitud
    this.orderData.OrderDate = this.formatDateForSql(this.orderData.OrderDate);
    this.orderData.RequiredDate = this.formatDateForSql(this.orderData.RequiredDate);
    this.orderData.ShippedDate = this.formatDateForSql(this.orderData.ShippedDate);

    // Primero se crea la orden
    this.apiService.createOrder(this.orderData).subscribe(
      (newOrder) => {
        this.toastr.success('Orden creada con éxito');

        // Obtener el OrderID de la orden recién creada
        const newOrderDetail = {
          ...this.orderDetailData,
          OrderID: newOrder.OrderID, // Asignar el OrderID de la orden creada
        };

        // Luego se crea el detalle de la orden
        this.apiService.createOrderDetail(newOrderDetail).subscribe(
          () => {
            this.toastr.success('Detalle de la orden creado con éxito');
          },
          (error) => {
            this.toastr.error('Error al crear el detalle de la orden');
          }
        );
      },
      (error) => {
        this.toastr.error('Error al crear la orden');
      }
    );
  }
}
