from dataclasses import dataclass

from app.domain.validators.base_validator import BaseValidator


@dataclass
class ItemBaseEntity:
    tab_id: int
    product_id: int
    quantity: int

    def __post_init__(self):
        self.validate()

    def validate(self) -> None:
        self.tab_id = BaseValidator.validate_positive_int(self.tab_id, "tab_id")
        self.product_id = BaseValidator.validate_positive_int(
            self.product_id, "product_id"
        )
        self.quantity = BaseValidator.validate_positive_int(self.quantity, "quantity")


@dataclass
class ItemCreateEntity(ItemBaseEntity):
    pass


@dataclass
class ItemUpdateEntity(ItemBaseEntity):
    pass
