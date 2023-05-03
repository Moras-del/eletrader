from django.contrib import messages
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six  
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)
        )

def send_email(request, user):
    account_activation_token = TokenGenerator()
    mail_subject = 'Activate your account in Eletrader!'
    message = render_to_string('account/activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[user.email])
    if email.send():
        messages.success(request, f'Please go to your e-mail ({user.email}) inbox and click on \
            received activation link to complete registration process.')
    else:
        messages.error(request, f'Problem sending confirmation email to {user.email}. Please check if your email adress is correct')
