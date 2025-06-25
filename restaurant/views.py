from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import BookingForm
from .models import Menu

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # You can customize this logic to send email or store messages in DB
        print(f"Contact form submitted by {name} ({email}): {message}")

        messages.success(request, "Thank you for reaching out! We'll get back to you soon.")
        return render(request, 'contact.html')

    return render(request, 'contact.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking submitted successfully!")
            form = BookingForm()  # Clear the form after submission
    context = {'form': form}
    return render(request, 'book.html', context)

def menu(request):
    category = request.GET.get('category')
    if category:
        menu_data = Menu.objects.filter(category=category)
    else:
        menu_data = Menu.objects.all()
    return render(request, 'menu.html', {
        'main_data': menu_data,
        'selected_category': category
    })

def display_menu_item(request, pk=None):
    menu_item = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_item.html', {'menu_item': menu_item})
