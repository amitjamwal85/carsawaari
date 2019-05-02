from fcm_django.models import FCMDevice
from django.contrib.auth.models import User
from fcm_django.models import FCMDevice


def send(request):
    from pyfcm import FCMNotification

    push_service = FCMNotification(api_key="AAAA3x9GumM:APA91bHzzZWsFiND_0clAPmKvQkBI1gsMSEKv7WbZ7LUKBJ1OWkHMyj09yYxpX8hLTnZoHZ4TiZqo1NB4K5CBViLLT_dqKr6Vwz6GGiggb6sdel8kZ1S2wfTEcgMqgRAD82BSkaJsDwq")
    # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
    registration_id = "<device registration_id>"
    message_title = "Uber update"
    message_body = "Hi john, your customized news for today is ready"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body)

    device = FCMDevice.objects.all()
    responseT=device.send_message({
    "to" : "/topics/18dd4734ab951d5b",
    "data": {
    "message": "This is a GCM Topic Message!",
    }
})
    return responseT