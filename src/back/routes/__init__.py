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
async def my_profile(data: WellModelCalcRequest):
    return {
  "vlp": {
    "q_liq": [
      0,
      30,
      60,
      90,
      120,
      150
    ],
    "p_wf": [
      200,
      190,
      180,
      175,
      185,
      200
    ]
  },
  "ipr": {
    "q_liq": [
      0,
      30,
      60,
      90,
      120,
      150
    ],
    "p_wf": [
      200,
      180,
      160,
      140,
      120,
      100
    ]
  },
  "nodal": [
    {
      "p_wf": 150,
      "q_liq": 100
    },
    {
      "p_wf": 160,
      "q_liq": 90
    }
  ]
}
