import requests
from fastapi import APIRouter
from urllib.parse import urljoin

from back.models.models import (NodalCalcResponse, VlpIprCalcResponse,
                                WellModelCalcRequest, WellModelCalcResponse)
from back.routes.request_formers import (form_ipr_request,
                                         form_nodal_request,
                                         form_vlp_request)
from back.config import Settings

main_router = APIRouter(prefix="/well_model", tags=["WellModel"])


@main_router.put("/calc", response_model=WellModelCalcResponse)
async def put_well(data: WellModelCalcRequest):
    vlp_data = form_vlp_request(data)
    ipr_data = form_ipr_request(data)
    vlp_response = requests.post('http://localhost:8001/vlp/calc', json=vlp_data)
    ipr_response = requests.post('http://localhost:8002/ipr/calc', json=ipr_data)
    nodal_data = form_nodal_request(vlp_response.json(), ipr_response.json())
    nodal_response = requests.post('http://localhost:8003/nodal/calc', json=nodal_data)
    return WellModelCalcResponse(ipr=ipr_response.json(), vlp=vlp_response.json(), nodal=nodal_response.json())
