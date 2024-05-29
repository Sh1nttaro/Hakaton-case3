from django.shortcuts import render, get_object_or_404
from .models import Specialist, Service, Review, FAQ, Doctor


def index(request):
    return render(request, 'index.html')


def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


def specialists(request):
    specialists = Specialist.objects.all()
    return render(request, 'specialists.html', {'specialists': specialists})


def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service_detail.html', {'service': service})


def specialist_detail(request, specialist_id):
    specialist = get_object_or_404(Specialist, id=specialist_id)
    return render(request, 'specialist_detail.html', {'specialist': specialist})


def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})


def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})


def contact(request):
    return render(request, 'contacts.html')


def vacancies(request):
    return render(request, 'vacancies.html')


def tips(request):
    return render(request, 'tips.html')


def login(request):
    return render(request, 'login.html')


def appointment(request):
    return render(request, 'appointment.html')


def clinic(request):
    return render(request, 'clinic.html')

def dentistry(request):
    return render(request, 'dentistry.html')


def search(request):
    query = request.GET.get('query')
    doctors = []
    services = []

    if query:
        doctors = Doctor.objects.filter(name__icontains=query)
        services = Service.objects.filter(name__icontains=query)

    return render(request, 'search_results.html', {'doctors': doctors, 'services': services, 'query': query})