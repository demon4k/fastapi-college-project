from fastapi import FastAPI
from prometheus_client import Gauge
from prometheus_fastapi_instrumentator import Instrumentator
from sqlalchemy import select, func

from app.api.router import api_router
from app.db.session import AsyncSessionLocal
from app.models.order import Order

app = FastAPI(title="FastAPI College Project")

app.include_router(api_router)

Instrumentator().instrument(app).expose(app)

total_orders_price_metric = Gauge(
    "total_orders_price",
    "Total price of all orders"
)


@app.get("/")
async def root():
    return {"message": "FastAPI CRUD project is working"}


@app.get("/custom-metrics/total-orders-price")
async def get_total_orders_price():
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(func.sum(Order.total_price)))
        total_price = result.scalar() or 0

    total_orders_price_metric.set(total_price)

    return {"total_orders_price": total_price}