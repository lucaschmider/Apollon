class ConsumerBase:
    """Acts as an interface for classes that consume a finished report"""

    def prepare_consumption(self, message: str) -> None:
        """Prepares the class so that the consume methods effects are instantly noticeable by the user"""
        pass
    
    def consume(self, message: str) -> None:
        """Consumes the report"""
        pass
