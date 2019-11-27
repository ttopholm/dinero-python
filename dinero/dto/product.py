from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass
@dataclass_json
class Product:
    Name: str
    BaseAmountValue: float
    ProductNumber: str
    Unit: str = 'parts'
    Quantity: int = 1
    AccountNumber: int = 1000
    CreatedAt: str = None
    UpdatedAt: str = None
    DeletedAt: Optional[str] = None
    ProductGuid: str = None
    BaseAmountValueInclVat: float = None
    TotalAmount: float = None
    TotalAmountInclVat: float = None
    ExternalReference: Optional[str] = None
    Comment: Optional[str] = None

    @staticmethod
    def get_id_field():
        return 'ProductGuid'






