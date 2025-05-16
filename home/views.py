from django.shortcuts import render,redirect
from .models import Recipe
# Create your views here.

def recepies(request):
    if request.method == 'POST':
        # Handle the form submission
        # For example, you can save the data to the database or process it
        # Here, we just print the data to the console
        data = request.POST
        image = request.FILES.get('image')
        print(data.get('name'))
        print(data.get('description')) 
        print(image)
        print("Form submitted")

        Recipe.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            image=image
        )

        return redirect('/')

    recipes = Recipe.objects.all()
    return render(request, 'recepies.html', {'recipes': recipes})