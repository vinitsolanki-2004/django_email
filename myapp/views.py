from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']

            # Send email to admin
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            sender_email = 'vinit2004solanki@gmail.com'
            sender_password = 'flwp zrcy jmrc trxq'
            receiver_email = 'agrobusy12@gmail.com'

            subject = f'New Contact Form Submission from {name}'
            body = f'Email : {email}\nComment : {comment}'

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = subject

            # Add body to email
            message.attach(MIMEText(body, 'plain'))

            # Create SMTP session for sending the email
            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(sender_email, sender_password)
                text = message.as_string()
                server.sendmail(sender_email, receiver_email, text)
                print('Email sent successfully!')
            except Exception as e:
                print(f'Error: {e}')
            finally:
                server.quit()

            return render(request, 'success.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def index_view(request):
    return render(request, 'index.html')
