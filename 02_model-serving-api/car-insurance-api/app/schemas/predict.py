from typing import Any, List, Optional

from pydantic import BaseModel

from app.carinsurance_model.processing.validation import CarInsuranceDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[int]]


class MultipleCarInsuranceDataInputs(BaseModel):
    inputs: List[CarInsuranceDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "Age": 20,
                        "Job": "admin.",
                        "Marital": "single",
                        "Education": "secondary",
                        "Default": 0,
                        "Balance": 1,
                        "HHInsurance": 1,
                        "CarLoan": 1,
                        "Communication": "",
                        "LastContactDay": 12,
                        "LastContactMonth": "may",
                        "NoOfContacts": 12,
                        "DaysPassed": -1,
                        "PrevAttempts": 0,
                        "Outcome": "",
                        "CallStart": "17:17:42",
                        "CallEnd": "17:18:06",
                    }
                ]
            }
        }
