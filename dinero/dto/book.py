from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass_json
@dataclass
class Book:
    Timestamp: str
    Number: Optional[int] = None
