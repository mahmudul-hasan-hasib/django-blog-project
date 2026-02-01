from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            obj = form.save()
            messages.success(request, "✅ Message sent successfully!")
            print("✅ SAVED:", obj)   # terminal এ দেখাবে
            return redirect('contact')
        else:
            print("❌ ERRORS:")
            print(form.errors)       # terminal এ error দেখাবে

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
