from django.shortcuts import get_object_or_404, redirect, render
from .models import CarAd


# Ana səhifə funksiyası
def home_view(request):
  cars = CarAd.objects.all().order_by('-created_at')
  return render(request, 'polls/index.html', {'cars': cars})


# Elan əlavə etmə funksiyası
def add_car(request):
  if request.method == 'POST':
    brand = request.POST.get('brand')
    model = request.POST.get('model')
    price = request.POST.get('price')
    city = request.POST.get('city')
    year = request.POST.get('year')
    mileage = request.POST.get('mileage')
    image = request.FILES.get('image')

    CarAd.objects.create(
        brand=brand,
        model=model,
        price=price,
        city=city,
        year=year,
        mileage=mileage,
        image=image,
    )
    return redirect('home')

  return render(request, 'polls/add_car.html')


# Ətraflı elan səhifəsi funksiyası
def car_detail(request, car_id):
  car = get_object_or_404(CarAd, pk=car_id)
  return render(request, 'polls/car_detail.html', {'car': car})