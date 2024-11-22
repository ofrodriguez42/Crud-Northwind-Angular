from fastapi import FastAPI
from routes.orders import router as orders_router
from routes.order_details import router as order_details_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Include routers
app.include_router(orders_router, prefix="/orders", tags=["Orders"])
app.include_router(order_details_router, prefix="/order-details", tags=["Order Details"])

# En tu archivo principal (por ejemplo, main.py)

# Añadir middleware para permitir CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL de tu aplicación React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)