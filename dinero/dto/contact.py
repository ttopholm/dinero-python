from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass_json
@dataclass
class Contact:

    Name: str
    IsDebitor: bool = False
    IsCreditor: bool = False
    CreatedAt: str = None
    UpdatedAt: Optional[str] = None
    DeletedAt: Optional[str] = None
    ContactGuid: str = None
    ExternalReference: Optional[str] = None
    Street: Optional[str] = None
    ZipCode: Optional[str] = None
    City: Optional[str] = None
    CountryKey: str = "DK"
    Phone: Optional[str] = None
    Email: Optional[str] = None
    Webpage: Optional[str] = None
    AttPerson: Optional[str] = None
    VatNumber: Optional[str] = None
    EanNumber: Optional[str] = None
    PaymentConditionType: str = None
    PaymentConditionNumberOfDays: int = 8
    IsPerson: bool = True
    isMember: bool = False
    MemberNumber: Optional[str] = None
    UseCvr: bool = False
    CompanyTypeKey: Optional[str] = None

    @staticmethod
    def get_id_field():
        return "ContactGuid"
