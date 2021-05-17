from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass_json
@dataclass
class Payment:
    Timestamp: str
    Description: str
    Amount: float
    DepositAccountNumber: Optional[int] = None
    RemainderIsFee: Optional[bool] = False
    ExternalReference: Optional[str] = None
    PaymentDate: Optional[str] = None
    AmountInForeignCurrency: Optional[float] = None
