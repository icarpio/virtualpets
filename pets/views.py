from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import PetBase, Pet
from django.http import HttpResponseForbidden
from django.http import JsonResponse
import requests
from django.http import HttpResponse


@login_required
def create_pet(request):
    if request.method == "POST":
        # Obtener el tipo de mascota elegido y el nombre ingresado
        pet_base_id = request.POST.get('pet_base')
        pet_name = request.POST.get('pet_name')

        # Obtener el objeto PetBase correspondiente al tipo de mascota seleccionado
        pet_base = PetBase.objects.get(id=pet_base_id)

        # Crear una nueva mascota asociada al usuario y al tipo de mascota elegido
        pet = Pet.objects.create(
            user=request.user,
            pet_base=pet_base,
            name=pet_name,
            current_image=pet_base.base_image  # Asignar la imagen base
        )

        # Redirigir a la página del dashboard de la mascota
        return redirect('pet_dashboard')

    # Obtener las opciones de mascotas predefinidas
    pet_bases = PetBase.objects.all()
    return render(request, 'pets/create_pet.html', {'pet_bases': pet_bases})


def pet_dashboard(request):
    pets = Pet.objects.filter(user=request.user)  # Obtener todas las mascotas asociadas al usuario
    return render(request, 'pets/pet_dashboard.html', {'pets': pets})

def delete_pet(request, pet_id):
    print(f"Intentando eliminar la mascota con ID: {pet_id}")  # 👈 Debug
    pet = Pet.objects.get(id=pet_id)
    pet.delete()
    return redirect('pet_dashboard')


def pet_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'pets/pet_detail.html', {'pet': pet})


def increase_hunger(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
        pet.hunger = min(pet.hunger + 9, 100)  # Asegura que no supere 100
        evolution_message = pet.evolve()  # Verificar evolución
        pet.save()
        return JsonResponse({'hunger': pet.hunger, 'message': evolution_message})
    except Pet.DoesNotExist:
        return JsonResponse({'error': 'Pet not found'}, status=404)
    
# Vista para aumentar la energía
def increase_energy(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
        pet.energy = min(pet.energy + 9, 100)  # Asegura que no supere 100
        evolution_message = pet.evolve()  # Verificar evolución
        pet.save()
        return JsonResponse({'energy': pet.energy, 'message': evolution_message})
    except Pet.DoesNotExist:
        return JsonResponse({'error': 'Pet not found'}, status=404)
    
    
# Vista para aumentar la felicidad
def increase_happiness(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
        pet.happiness = min(pet.happiness + 9, 100)  # Asegura que no supere 100
        evolution_message = pet.evolve()  # Verificar evolución
        pet.save()
        return JsonResponse({'happiness': pet.happiness, 'message': evolution_message})
    except Pet.DoesNotExist:
        return JsonResponse({'error': 'Pet not found'}, status=404)

def image_proxy(request, image_url):
    # Obtén la imagen desde la URL externa
    response = requests.get(image_url)
    # Devuelve la imagen en la respuesta HTTP
    return HttpResponse(response.content, content_type="image/png")


  
