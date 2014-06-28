""" Utilitary functions module """

from django.core.mail import EmailMessage


def send_album_email(sender, instance, **kwargs):
    """ sends email showing the album number of pictures when it has multiple
        of 100 pictures and less then 501 pictures """

    num_pics = len(instance.pictures)
    if num_pics and not num_pics % 100 and num_pics < 501:
        email_from = 'Eversnap Hashtag <Hashtag@EversnapApp.com>'
        email_to = ['ivan.cr.neto@gmail.com']
        bcc = ['davide@geteversnap.com']
        # TODO: remove this bcc dev setting
        bcc = ['ivan@becom.com.br']
        subject = '#carnival has {} photos'.format(num_pics)
        message = 'I\'m awesome!'

        mail = EmailMessage(subject, message, email_from, email_to, bcc=bcc)
        mail.send(fail_silently=False)
