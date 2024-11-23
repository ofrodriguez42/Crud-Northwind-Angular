// src/app/components/delete-card/delete-card.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-delete-card',
  templateUrl: './delete-card.component.html',
  styleUrls: ['./delete-card.component.css'],
  standalone: true,
  imports: [CommonModule, FormsModule] // Importar los módulos necesarios
})
export class DeleteCardComponent {
  orderId: string = '';

  constructor(private apiService: ApiService, private toastr: ToastrService) {}

  handleDeleteOrder() {
    // Convertir el `orderId` en número y llamar a la API para eliminar la orden
    this.apiService.deleteOrder(parseInt(this.orderId, 10)).subscribe(
      () => {
        this.toastr.success('Orden eliminada con éxito');
        this.orderId = ''; // Limpiar el campo después de eliminar la orden
      },
      error => {
        this.toastr.error('Error al eliminar la orden');
      }
    );
  }
}
