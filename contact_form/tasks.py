from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.utils.log import get_task_logger

from django.core.mail import send_mail, BadHeaderError
from celery_project.settings import DEFAULT_FROM_EMAIL

from django.conf import settings
logger = get_task_logger(__name__)


@shared_task(bind=True)
def send_email_task(self, to, subject, message):
    #logger.info(f"from={EMAIL_HOST_USER}, to={to}, subject={subject}, message={message}")
    try:
        #logger.info("About to send_mail")
        send_mail(subject, message, settings.EMAIL_HOST_USER, [to])
    except BadHeaderError:
        logger.info("BadHeaderError")
    except Exception as e:
        logger.error(e)
