from django.db.models.signals import post_save
# receiver use for signal receive
from django.dispatch import receiver 
from .models import StudentRecord,SponsershipDetail
from django.core.mail import send_mail

# For Emailing
@receiver(post_save,sender = StudentRecord)  # Studentrecord maa new data save huda assesment_result send garraw.
def on_assesment_results_created (sender, instance, **kwargs):
    print ('assesment_results_created')
    send_mail(
        subject = 'course deadlines and Assessment results',
        message = 'Dear Students this meassage is about your course deadlines and assessment results',
        from_email = 'chygautam02@gmail.com',
        recipient_list=['test@example.com'],
        )
    
@receiver(post_save,sender = SponsershipDetail)
def on_assesment_results_created (sender, instance, **kwargs):
    print ('assesment_results_created')
    send_mail(
        subject = 'Progress reports',
        message = 'Dear sponsers this meassage is about students progress reports',
        from_email = 'chygautam02@gmail.com',
        recipient_list=['test@example.com'],
        )

