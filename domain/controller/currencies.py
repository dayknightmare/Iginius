from domain.use_cases.currencies import get_api_currency
from fastapi import APIRouter


router_currencies = APIRouter()


@router_currencies.get('/')
async def get_currency():
    data = get_api_currency()

    if len(data) > 0 and data[0] == -1:
        return {
            'success': False,
            'msg': 'Wrong values'
        }

    return {
        'success': True,
        'currency': data
    }