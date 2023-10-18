from django.apps import AppConfig


class AdvertisementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "advertisement"

    def ready(self):
        from .signals import notify_user_reply
