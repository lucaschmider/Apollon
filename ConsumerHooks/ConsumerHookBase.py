from threading import Thread


class ConsumerHookBase(Thread):
    def before_consumers_started(self):
        pass

    def after_consumers_finished(self):
        pass
