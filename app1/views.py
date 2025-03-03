from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, DatabaseError
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Device
import random
import string
import json


@login_required
def device_list(request):
    devices = Device.objects.filter(user=request.user)  # Only show devices for the logged-in user
    return render(request, 'device_list.html', {'devices': devices})

@login_required
def led_control(request):
    try:
        devices = Device.objects.filter(user=request.user)  # Get the user's devices

        selected_device = None
        if 'device' in request.GET:
            selected_device_id = request.GET.get('device')
            if selected_device_id:
                selected_device = get_object_or_404(Device, id=selected_device_id, user=request.user)

        if request.method == 'POST':
            if not selected_device:
                return HttpResponseBadRequest("Invalid device selection.")

            if 'led1' in request.POST:
                selected_device.led1_status = not selected_device.led1_status
            elif 'led2' in request.POST:
                selected_device.led2_status = not selected_device.led2_status
            elif 'led3' in request.POST:
                selected_device.led3_status = not selected_device.led3_status
            else:
                return HttpResponseBadRequest("Invalid LED control request.")

            # Save the updated LED state
            selected_device.save()

            return redirect(f'{request.path}?device={selected_device.id}')

        return render(request, 'led_control.html', {
            'devices': devices,
            'selected_device': selected_device
        })
    
    except DatabaseError:
        return HttpResponse("Database error occurred. Please try again later.", status=500)
    except Exception as e:
        return HttpResponse(f"An unexpected error occurred: {str(e)}", status=500)


# Function to generate a unique API key
def generate_api_key(length=20):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@login_required  # Ensure only logged-in users can add a device
def add_device(request):
    if request.method == 'POST':
        device_name = request.POST.get('device_name')  # Get the device name from the form

        # Check if the device name is provided
        if not device_name:
            return HttpResponse("Device name is required.", status=400)

        try:
            # Generate a unique API key
            api_key = generate_api_key()

            # Create the new device associated with the logged-in user
            Device.objects.create(
                device_name=device_name,
                api_key=api_key,
                user=request.user
            )

            # Redirect to a page showing the list of devices
            return redirect('device_list')

        except IntegrityError:
            # Handle integrity errors (e.g., duplicate entries)
            return HttpResponse("Error: Device name must be unique.", status=400)
        except DatabaseError:
            # Handle database-related errors
            return HttpResponse("Database error occurred. Please try again later.", status=500)
        except Exception as e:
            # Catch all other exceptions
            return HttpResponse(f"An unexpected error occurred: {str(e)}", status=500)

    return render(request, 'add_device.html')

@login_required
def toggle_device_activation(request, device_id):
    device = get_object_or_404(Device, id=device_id, user=request.user)
    device.is_active = not device.is_active  # Toggle the activation status
    device.save()
    return redirect('device_list')  # Redirect back to the device list

# View to delete a device
@login_required
def delete_device(request, device_id):
    device = get_object_or_404(Device, id=device_id, user=request.user)  # Ensure the device belongs to the logged-in user
    device.delete()  # Delete the device from the database
    return redirect('device_list')  # Redirect to the device list page


def get_led_status(request):
    """Fetch the status of all LEDs only if the device is active"""
    api_key = request.GET.get('api_key')

    if not api_key:
        return JsonResponse({"error": "API key is required"}, status=400)  # Bad request

    try:
        # Fetch the device for the given API key
        device = Device.objects.get(api_key=api_key)

        # Check if the device is active
        if not device.is_active:
            return JsonResponse({"error": "Device is inactive"}, status=403)  # Forbidden

        # Return LED statuses if the device is active
        return JsonResponse({
            "device_name": device.device_name,
            "user": device.user.username,  # Include user for reference
            "led1_status": int(device.led1_status),
            "led2_status": int(device.led2_status),
            "led3_status": int(device.led3_status),
            "led4_status": int(device.led4_status)
        })

    except Device.DoesNotExist:
        return JsonResponse({"error": "Invalid API key or device not found"}, status=404)
    

@login_required
def dashboard(request):
    # Get the logged-in user
    user = request.user

    # Filter devices based on the logged-in user
    total_devices = Device.objects.filter(user=user).count()
    total_active_devices = Device.objects.filter(user=user, is_active=True).count()
    total_inactive_devices = Device.objects.filter(user=user, is_active=False).count()

    # Context data to be passed to the template
    context = {
        'user': user,  # Pass user details
        'total_devices': total_devices,
        'total_active_devices': total_active_devices,
        'total_inactive_devices': total_inactive_devices,
    }
    
    return render(request, 'dashboard.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('dashboard')
        else:
            messages.error(request, "Registration failed. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
