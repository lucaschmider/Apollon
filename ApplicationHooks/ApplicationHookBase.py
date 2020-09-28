from threading import Thread


class ApplicationHookBase(Thread):
    """Acts as an interface for classes that react to certain events in the application"""
    def __init__(self):
        super().__init__()
        self.start()

    def before_consumers_started(self):
        """This method gets called before the consumers start their consuming phase"""
        pass

    def after_consumers_finished(self):
        """This method gets called after all consumers have finished"""
        pass

    def application_ready(self):
        """This method gets called after the application startup is complete"""
        pass

    def report_generation_started(self):
        """This method gets called before the report generators start to prepare their reports"""
        pass
