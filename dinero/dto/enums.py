from enum import Enum


class PaymentConditionType(Enum):
    NETTO = "Netto"
    NETTOCASH = "NettoCash"
    CURRENTMONTHOUT = "CurrentMonthOut"
    PAID = "Paid"


class Unit(Enum):
    HOURS = "hours"
    PARTS = "parts"
    KM = "km"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    KILOGRAM = "kilogram"
    CUBICMETRE = "cubicMetre"
    SET = "set"
    LITRE = "litre"
    BOX = "box"
    CASE = "case"
    CARTON = "carton"
    METRE = "metre"
    PACKAGE = "package"
    SHIPMENT = "shipment"
    SQUAREMETRE = "squareMetre"
    SESSION = "session"
    TONNE = "tonne"


class LineType(Enum):
    PRODUCT = "Product"
    TEXT = "Text"
