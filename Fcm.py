import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials

#cred = credentials.Certificate("/content/drive/MyDrive/Colab_Notebooks/code/pixie-b4bf8-firebase-adminsdk-cdjsi-09a89665de.json")
#firebase_admin.initialize_app(cred)

def send_to_firebase_cloud_messaging(title, body):
    registration_token = 'cBRwgIapRVyv7r4t5CfekZ:APA91bH-K3PutC9OECT-29Knkh-QLybNCC9_38KjC0N5P3rDL83c4AJLwEOhoWU5kpP-8ge3RXOAlms0f9khMiNE2bkSj5kBDueSxRPHdQdsitxGPizrTiPWsSys43ZwBRiHlM41NlCr'

    message = messaging.Message(
    notification=messaging.Notification(
        title=title,
        body=body,
    ),
    token=registration_token,
    )

    response = messaging.send(message)
    print('성공적으로 보낸 알림:', response)