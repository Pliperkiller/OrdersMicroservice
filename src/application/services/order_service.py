from src.domain.ports.input.create_order_usecase import CreateOrderUsecase
from src.domain.ports.input.delete_order_usecase import DeleteOrderUseCase
from src.domain.ports.input.get_order_usecase import GetOrderUsecase
from src.domain.ports.input.update_order_usecase import UpdateOrderUsecase
from typing_extensions import override

class OrderService(CreateOrderUsecase,DeleteOrderUseCase,GetOrderUsecase,UpdateOrderUsecase):
    def __init__(self,
                 create_order_usecase: CreateOrderUsecase,
                 delete_order_usecase: DeleteOrderUseCase,
                 get_order_usecase: GetOrderUsecase,
                 update_order_usecase: UpdateOrderUsecase):
        super().__init__()
        self.create_order_usecase = create_order_usecase
        self.delete_order_usecase = delete_order_usecase
        self.get_order_usecase = get_order_usecase
        self.update_order_usecase = update_order_usecase

    @override
    def create_order(self, order):
        return self.create_order_usecase.create_order(order)
    
    @override
    def delete_order(self, order_id):
        return self.delete_order_usecase.delete_order(order_id)
    
    @override
    def get_order(self, order_id):
        return self.get_order_usecase.get_order(order_id)
    
    @override
    def get_all_orders(self):
        return self.get_order_usecase.get_all_orders()
    
    @override
    def update_order(self, order_id, order):
        return self.update_order_usecase.update_order(order_id, order)
    
    @override
    def update_order_status(self, order_id, new_status):
        return self.update_order_usecase.update_order_status(order_id, new_status)