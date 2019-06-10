from django.apps import AppConfig


class TodoConfig(AppConfig):
    name = 'todo'
    import todo.tasks
