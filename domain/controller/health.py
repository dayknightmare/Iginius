from fastapi import APIRouter

router_health = APIRouter()

@router_health.get('/health')
async def health():
    return {"success": True}