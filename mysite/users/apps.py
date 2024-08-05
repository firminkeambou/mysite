from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    # below function is added in the perspective of / in view of using django signal within this app
    def ready(self):
        import users.signals