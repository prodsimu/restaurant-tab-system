import re
import unicodedata
from dataclasses import dataclass

from app.domain.validators.base_validator import BaseValidator


@dataclass
class ProductBaseEntity:
    name: str
    price: float

    def __post_init__(self):
        self.validate()
        self.normalize()

    def validate(self) -> None:
        self.name = BaseValidator.validate_string(self.name, "name")
        self.price = BaseValidator.validate_positive_float(self.price, "price")

    def normalize(self) -> None:
        self.name = unicodedata.normalize("NFKD", self.name)
        self.name = self.name.encode("ASCII", "ignore").decode("utf-8")
        self.name = self.name.lower()
        self.name = re.sub(r"[^a-z0-9]+", "-", self.name).strip("-")


@dataclass
class ProductCreateEntity(ProductBaseEntity):
    pass


@dataclass
class ProductUpdateEntity(ProductBaseEntity):
    id: int

    def validate(self) -> None:
        super().validate()
        self.id = BaseValidator.validate_positive_int(self.id, "id")
