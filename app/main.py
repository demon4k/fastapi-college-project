from fastapi import FastAPI
from prometheus_client import Gauge
from prometheus_fastapi_instrumentator import Instrumentator
from sqlalchemy import select, func

from app.api.router import api_router
from app.db.session import AsyncSessionLocal
from app.models.order import Order
from app.models.product import Product
from app.models.user import User

app = FastAPI(title="FastAPI College Project")

app.include_router(api_router)

Instrumentator().instrument(app).expose(app)

total_orders_price_metric = Gauge(
    "total_orders_price",
    "Total price of all orders"
)

total_users_count_metric = Gauge(
    "total_users_count",
    "Total number of users"
)

total_products_count_metric = Gauge(
    "total_products_count",
    "Total number of products"
)


@app.get("/")
async def root():
    return {"message": "FastAPI CRUD project is working"}


@app.get("/custom-metrics/summary")
async def get_custom_metrics_summary():
    async with AsyncSessionLocal() as db:
        orders_price_result = await db.execute(select(func.sum(Order.total_price)))
        total_orders_price = orders_price_result.scalar() or 0

        users_count_result = await db.execute(select(func.count(User.id)))
        total_users_count = users_count_result.scalar() or 0

        products_count_result = await db.execute(select(func.count(Product.id)))
        total_products_count = products_count_result.scalar() or 0

    total_orders_price_metric.set(total_orders_price)
    total_users_count_metric.set(total_users_count)
    total_products_count_metric.set(total_products_count)

    return {
        "total_orders_price": total_orders_price,
        "total_users_count": total_users_count,
        "total_products_count": total_products_count,
    }