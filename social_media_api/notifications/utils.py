from .models import Notification

def create_notification(actor, recipient, verb, target=None):
    if actor == recipient:
        return  # don't notify yourself
    Notification.objects.create(
        actor=actor,
        recipient=recipient,
        verb=verb,
        target=target
    )
