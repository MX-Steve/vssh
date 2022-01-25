from django.urls import path
from chat.ws_server import WebSSHService
from chat.views import putHostView, getHostView

websocket_url = [path("web/<int:id>/", WebSSHService.as_asgi())]

urlpatterns = [
    path('p-host', putHostView, name="p-host"),
    path('g-host', getHostView, name="g-host"),
]
