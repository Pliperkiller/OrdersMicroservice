from src.domain.ports.input.create_order_item_usecase import CreateOrderItemUsecase
from src.domain.ports.output.order_item_repository import OrderItemRepository
from src.domain.entities.order_item import OrderItem
from typing import override

class CreateOrderItemUsecaseImpl(CreateOrderItemUsecase):
    def __init__(self, order_item_repository:OrderItemRepository):
        self.order_item_repository = order_item_repository

    @override
    def create_order_item(self, order_id: int ,order_item:OrderItem):
        self.order_item_repository.create( order_id ,order_item)