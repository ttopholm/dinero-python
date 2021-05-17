from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional, List
from .enums import PaymentConditionType
from .productline import ProductLine


@dataclass_json
@dataclass
class Invoice:
    PaymentConditionType: PaymentConditionType
    ProductLines: List[ProductLine]
    ContactGuid: str
    PaymentConditionNumberOfDays: Optional[int] = None
    ShowLinesInclVat: Optional[bool] = False
    InvoiceTemplateId: Optional[str] = None
    Currency: Optional[str] = "DKK"
    Language: Optional[str] = "da-DK"
    ExternalReference: Optional[str] = None
    Description: Optional[str] = None
    Comment: Optional[str] = None
    Date: Optional[str] = None
    Address: Optional[str] = None
    Guid: str = None
    TimeStamp: Optional[str] = None
    #Timestamp: Optional[str] = None

    @staticmethod
    def get_id_field():
        return "Guid"
