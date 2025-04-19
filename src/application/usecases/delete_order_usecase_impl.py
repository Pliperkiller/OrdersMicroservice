
from src.domain.ports.input.delete_order_usecase import DeleteOrderUseCase
from src.domain.ports.output.order_repository import OrderRepository
from src.domain.ports.output.order_item_repository import OrderItemRepository
from typing_extensions import override

class DeleteOrderUseCaseImpl(DeleteOrderUseCase):
    def __init__(self,
                 order_repository:OrderRepository,
                 order_item_repository:OrderItemRepository):
        self.order_repository = order_repository
        self.order_item_repository = order_item_repository

    @override
    def delete_order(self, order_id):
        self.order_item_repository.delete_by_order_id(order_id)
        self.order_repository.delete(order_id)