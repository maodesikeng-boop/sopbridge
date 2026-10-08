from fastapi import FastAPI

from sopbridge_api.routes import health

app = FastAPI(title="Sopbridge API")
app.include_router(health.router)
