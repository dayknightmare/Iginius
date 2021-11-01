from fastapi import APIRouter, Response


router_health = APIRouter()


@router_health.get('/health', status_code=200)
async def health(response: Response):
    return {"success": True}