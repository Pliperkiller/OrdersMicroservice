from src.domain.ports.input.create_order_usecase import CreateOrderUsecase
from src.domain.ports.output.order_repository import OrderRepository
from src.domain.entities.order import Order
from typing import override

class CreateOrderUsecaseImpl(CreateOrderUsecase):
    def __init__(self, order_repository:OrderRepository):
        self.order_repository = order_repository

    @override
    def create_order(self, order:Order):
        self.order_repository.create(order)

