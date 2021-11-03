from domain.use_cases.currencies import get_api_currency, process_and_store_currencies, get_json_currencies
from helpers.currencies import validate_and_tranform_date_str
from fastapi import APIRouter, Response, status


router_currencies = APIRouter()


@router_currencies.get('/{id_currency}/{start_date}/{final_date}', status_code=200, responses={
    200: {"description": "Ok"},
    400: {"description": "Wrong or missing values"},
})
async def get_currency(
    id_currency: int,
    start_date: str,
    final_date: str,
    response: Response
):
    start_date = validate_and_tranform_date_str(start_date)
    final_date = validate_and_tranform_date_str(final_date)

    if start_date == "" or final_date == "":
        response.status_code = status.HTTP_400_BAD_REQUEST
        
        return {
            'success': False,
            'msg': 'Wrong values'
        }
 
    data = await get_api_currency(id_currency, start_date, final_date)

    if len(data) > 0 and data[0] == -1:
        response.status_code = status.HTTP_400_BAD_REQUEST
        
        return {
            'success': False,
            'msg': 'Wrong values'
        }

    await process_and_store_currencies(data)

    return {
        'success': True,
        'currency': data
    }


@router_currencies.get("/currencies", status_code=200, responses={
    200: {"description": "Ok"},
})
async def get_all_currencies():
    return {
        'success': True,
        'currencies': get_json_currencies()
    }