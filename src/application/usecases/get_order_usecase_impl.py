from src.domain.ports.input.get_order_usecase import GetOrderUsecase
from src.domain.ports.output.order_repository import OrderRepository
from typing import override

class GetOrderUsecaseImpl(GetOrderUsecase):
    def __init__(self, order_repository:OrderRepository):
        self.order_repository = order_repository

    @override
    def get_order(self, order_id:int):
        return self.order_repository.get_by_id(order_id)

