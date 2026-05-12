from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.api.v1.schemas.item_schema import ItemCreateSchema
from app.domain.entities.item_entity import ItemCreateEntity
from app.domain.exceptions.product_exceptions import ProductNotFoundError
from app.domain.exceptions.tab_exceptions import TabNotFoundError
from app.infrastructure.database.models.item_model import ItemModel
from app.infrastructure.database.models.product_model import ProductModel
from app.infrastructure.database.models.tab_model import TabModel


class ItemService:

    # CREATE

    @staticmethod
    def add_item_to_tab(db: Session, data: ItemCreateSchema):

        tab = (
            db.query(TabModel)
            .filter(and_(TabModel.number == data.tab_number, TabModel.is_open))
            .first()
        )

        if not tab:
            raise TabNotFoundError("Tab is not open")

        product = (
            db.query(ProductModel).filter(ProductModel.id == data.product_id).first()
        )

        if not product:
            raise ProductNotFoundError("Product not found")

        item = (
            db.query(ItemModel)
            .filter(
                and_(
                    ItemModel.tab_id == tab.id,
                    ItemModel.product_id == data.product_id,
                )
            )
            .first()
        )

        if item:
            item.quantity += data.quantity
            db.commit()
            db.refresh(item)
            return item

        entity = ItemCreateEntity(tab.id, data.product_id, data.quantity)

        db_model = ItemModel(
            tab_id=entity.tab_id,
            product_id=entity.product_id,
            quantity=entity.quantity,
        )

        db.add(db_model)
        db.commit()
        db.refresh(db_model)

        return db_model

    # READ

    @staticmethod
    def list_tab_items(db: Session, tab_number: int):
        tab = (
            db.query(TabModel)
            .filter(and_(TabModel.number == tab_number, TabModel.is_open))
            .first()
        )

        if not tab:
            raise TabNotFoundError("Tab is not open")

        items = db.query(ItemModel).filter(ItemModel.tab_id == tab.id).all()

        return items

    # UPDATE

    # DELETE
