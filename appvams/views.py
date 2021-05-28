from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View

from appvams.forms import SignUpForm
from appvams.models import Vaccine


class Staff(View):
    def get(self, request):
        return render(request, 'vams/staff.html')


class Base(View):
    def get(self, request):
        return render(request, 'vams/base.html')


class Index(View):
    def get(self, request):
        return render(request, 'vams/index.html')


class Patient(View):
    def get(self, request):
        return render(request, 'vams/patient.html')


class About(View):
    def get(self, request):
        return render(request, 'vams/about.html')


class Blog(View):
    def get(self, request):
        return render(request, 'vams/blog.html')


class BlogSingle(View):
    def get(self, request):
        return render(request, 'vams/blog-single.html')


class Contact(View):
    def get(self, request):
        return render(request, 'vams/contact.html')


class Doctors(View):
    def get(self, request):
        return render(request, 'vams/doctors.html')


class Services(View):
    def get(self, request):
        return render(request, 'vams/services.html')


class Navbar(View):
    def get(self, request):
        return render(request, 'vams/navbar.html')


def error404(request, exception):
    return render(request, 'vams/404.html')


class Vaccines(View):
    def get(self, request):
        v = Vaccine.objects.all()
        return render(request, 'vams/vaccine.html', {'vaccine': v})


class Vaccination(View):
    def get(self, request):
        return render(request, 'vams/vaccination.html')


class VaccineStock(View):
    def get(self, request):
        return render(request, 'vams/stock.html')


class Report(View):
    def get(self, request):
        return render(request, 'vams/report.html')


class Signup(View):
    def get(self, request):
        return render(request, 'vams/signup.html')

    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)

        customer_group, created = Group.objects.get_or_create(name='Customer')

        # print(SignUpForm)
        # print(form.fields)
        # print(form.errors.as_json())
        print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            customer_group.user_set.add(user)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('vams/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]

            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            # form = SignUpForm()
            return render(request, 'vams/signup.html', {'form': form})


# def activate(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = get_user_model()._default_manager.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and default_token_generator.check_token(user, token):
#         user.active = True
#         user.save()
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')


class ActivateURL(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_user_model()._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')


