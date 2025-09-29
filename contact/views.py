import os
from email.mime.image import MIMEImage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # --- Préparation des emails ---
            form_data = form.cleaned_data
            context = {
                'nom': form_data['nom'],
                'email': form_data['email'],
                'sujet': form_data['sujet'],
                'message': form_data['message'],
            }

            # 1. Email de notification pour vous
            admin_html_content = render_to_string('emails/contact_notification.html', context)
            admin_text_content = f"Nouveau message de {context['nom']} ({context['email']})..."
            admin_sujet = f"Nouveau message de {context['nom']}: {context['sujet']}"
            admin_email = EmailMultiAlternatives(admin_sujet, admin_text_content, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            admin_email.attach_alternative(admin_html_content, "text/html")

            # 2. Email de confirmation pour l'utilisateur
            user_html_content = render_to_string('emails/user_confirmation.html', context)
            user_text_content = f"Bonjour {context['nom']}, merci de nous avoir contactés..."
            user_sujet = "Confirmation de votre message à l'École Telema Ngenga"
            user_email = EmailMultiAlternatives(
                subject=user_sujet, 
                body=user_text_content, 
                from_email=settings.EMAIL_HOST_USER, 
                to=[form_data['email']],
                reply_to=[settings.EMAIL_HOST_USER]
            )
            user_email.attach_alternative(user_html_content, "text/html")

            # Attacher le logo aux deux emails
            try:
                logo_path = os.path.join(settings.MEDIA_ROOT, 'Img_logo', 'logo.png')
                with open(logo_path, 'rb') as f:
                    logo_data = f.read()
                logo_image = MIMEImage(logo_data)
                logo_image.add_header('Content-ID', '<logo>')
                
                admin_email.attach(logo_image)
                logo_image_clone = MIMEImage(logo_data)
                logo_image_clone.add_header('Content-ID', '<logo>')
                user_email.attach(logo_image_clone)

            except FileNotFoundError:
                pass

            # Envoyer les emails
            try:
                admin_email.send()
                user_email.send()
                messages.success(request, 'Votre message a bien été envoyé.')
            except Exception as e:
                messages.error(request, f"Une erreur est survenue lors de l'envoi de l'email: {e}")

            return redirect('contact:contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
