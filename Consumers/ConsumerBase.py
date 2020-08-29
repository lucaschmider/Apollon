class ConsumerBase:
    def prepare_consumption(self, message: str) -> None:
        pass
    
    def consume(self, message: str) -> None:
        pass
