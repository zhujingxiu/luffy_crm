from django.apps import AppConfig


class XstarkConfig(AppConfig):
    name = 'xstark'

    def ready(self):
        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules(self.name)