from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional
from .enums import Unit, LineType


@dataclass_json
@dataclass
class ProductLine:
    BaseAmountValue: float
    Description: str
    Unit: Unit
    LineType: LineType
    Quantity: Optional[int] = 1
    AccountNumber: Optional[int] = 1000
    ProductGuid: Optional[str] = None
    Comment: Optional[str] = None
    Discount: Optional[str] = 0
