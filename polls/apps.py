from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'
    def ready(self):
        print "ready calling"
        import polls.signals.handlers