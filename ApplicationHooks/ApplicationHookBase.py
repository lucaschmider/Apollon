from threading import Thread


class ApplicationHookBase(Thread):
    def __init__(self):
        super().__init__()
        self.start()

    def before_consumers_started(self):
        pass

    def after_consumers_finished(self):
        pass

    def application_ready(self):
        pass

    def report_generation_started(self):
        pass
