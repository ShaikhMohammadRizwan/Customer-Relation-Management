from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()

    # check to see if logging In
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successfully!!!')
            return redirect('home')
        else:
            messages.success(request, "There was an error Logging in")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})



def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out successfully!!!')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user and get the user object
            # Authenticate and login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Use 'password1' instead of 'password'
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have registered successfully!!!')
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed. Please try again.')
                return redirect('register')  # Optionally, redirect to registration page if authentication fails
        else:
            return render(request, 'register.html', {'form': form})

    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, 'You must be logged in to view this record.')
        return redirect('home')
    

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record has been deleted successfully.')
        return redirect('home')
    else:
        messages.error(request, 'You must be logged in to delete this record.')
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()  # Save the new record
                messages.success(request, 'New record has been added successfully.')
                return redirect('home')  # Redirect to the home page after adding the record
            else:
                # If the form is not valid, render the form again with error messages
                messages.error(request, 'There was an error adding the record. Please check the form fields.')
                return render(request, 'add_record.html', {'form': form})
        else:
            # If the method is GET, render the empty form
            return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to add a new record.')
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)  # Get the record to be updated
        form = AddRecordForm(request.POST or None, instance=current_record)  # Pre-fill the form with the current record's data
        
        if request.method == 'POST':
            if form.is_valid():
                form.save()  # Save the updated record
                messages.success(request, 'Record has been updated successfully.')
                return redirect('home')  # Redirect to the home page after updating the record
            else:
                # If the form is not valid, render the form again with error messages
                messages.error(request, 'There was an error updating the record. Please check the form fields.')
                return render(request, 'update_record.html', {'form': form})
        
        # If the request is GET, render the form with the current record's data
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to update this record.')
        return redirect('home')

