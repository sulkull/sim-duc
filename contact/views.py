from django.shortcuts import render
from .models import LienHe
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from user.models import CustomerUser


# Create your views here.
def home(request):
    Data = {
    }

    if request.method == 'POST':
        hoten = request.POST.get('name')
        email = request.POST.get('email')
        sdt = request.POST.get('sdt')
        tinnhan = request.POST.get('message')

        lienhe_obj = LienHe(HoTen=hoten, Email=email, SDT=sdt, TinNhan=tinnhan)
        lienhe_obj.save()

        mail_subject_admin = 'Bạn có một tin nhắn mới.'
        message_admin = render_to_string('simso/chitiettinnhan.html', {
            'HoTen': hoten,
            'Email': email,
            'SDT': sdt,
            'TinNhan': tinnhan,
        })
        to_email_admins = CustomerUser.objects.get(is_superuser=True).email
        email_admin = EmailMessage(
            mail_subject_admin, message_admin, to=[to_email_admins]
        )
        email_admin.content_subtype = 'html'
        email_admin.mixed_subtype = 'related'
        email_admin.send()

        return render(request, 'simso/guitinnhanthanhcong.html', Data)

    return render(request, 'simso/contact.html', Data)
