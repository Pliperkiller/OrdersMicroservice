from src.domain.ports.input.create_order_usecase import CreateOrderUsecase
from src.domain.ports.output.order_repository import OrderRepository
from src.domain.ports.output.order_item_repository import OrderItemRepository
from src.domain.ports.output.product_repository import ProductRepository
from src.domain.entities.order_item import OrderItem
from src.domain.entities.factories.order_builder import OrderBuilder
from src.domain.entities.order import Order
from typing_extensions import override
from typing import List, Dict

class CreateOrderUsecaseImpl(CreateOrderUsecase):
    def __init__(self,
                 order_repository : OrderRepository,
                 order_item_repository : OrderItemRepository,
                 product_repository : ProductRepository
                 ):
        self.order_repository = order_repository
        self.order_item_repository = order_item_repository
        self.product_repository = product_repository

    @override
    def create_order(self, client_id: int, order_items: List[Dict[str, int]]):
        
        builder = OrderBuilder()
        builder.set_client_id(client_id)

        for item in order_items:
            product_id = item['product_id']
            amount = item['amount']
            product = self.product_repository.get_by_id(product_id)

            order_item = OrderItem(product, amount)

            self.order_item_repository.create(order_item)
            builder.add_item(item)

        builder.calculate_total()
        order = builder.build()
        self.order_repository.create(order)