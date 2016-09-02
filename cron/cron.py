from django.core.mail import send_mail

def my_scheduled_job():
    send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
    )
