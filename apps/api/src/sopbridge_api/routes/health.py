from fastapi import APIRouter

from sopbridge_api.schemas.health import HealthCheckResponse

router = APIRouter(tags=["health"])


@router.get("/healthz")
def healthz() -> HealthCheckResponse:
    """Liveness probe: returns 200 as long as the process is up."""
    return HealthCheckResponse(status="ok")
