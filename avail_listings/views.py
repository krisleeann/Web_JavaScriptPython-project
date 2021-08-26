from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms

from .models import User, Listing, Apply, Category, Event
from .forms import NewInterestForm, NewListingForm, NewEventForm


# Following index, all functions are arranged alphabetically
def index(request):
    
    if request.user.is_authenticated:
        return render(request, "avail_listings/index.html", {
            'listing': Listing.objects.all()
        })
    else:
        return render(request, "avail_listings/register.html", {
            'message': "Please register or login to view available listings."
        })


def categories(request):
    categories = Category.objects.all()
    listings = Listing.objects.filter(category=categories)
        
    if request.method == "POST":
        return render(request, "avail_listings/categories.html", {
                'categories': categories,
                'category': Category.objects.get(id=category).category if category is not None else "",
                'listings': listings
            }) 
    else:
        return render(request, "avail_listings/categories.html", {
            'message': "Bug: Does not link/display each categories respective listings."
        })


def category(request, category_id):
    category = Category.objects.get(id=category_id)

    return render(request, "avail_listings/category.html", {
        'Category': category,
    })

@login_required
def create_event(request):
    
    form = NewEventForm(request.POST)
    
    if request.method == "POST":
        if form.is_valid():
            title = form.cleaned_data["title"] 
            location =  form.cleaned_data["location"]
            date = form.cleaned_data["date"]
            description = form.cleaned_data["description"]
            
            new_event = Listing.objects.create(title=title,
                                            location=location,
                                            date=date,
                                            description=description)
            new_event.save()
        
        return HttpResponseRedirect(reverse("events"))
    
    else:
        return render(request, "avail_listings/create_event.html", {
            'form': NewEventForm()
        })
    

@login_required
def create_listing(request):
    user = request.user
    form = NewListingForm(request.POST)

    if request.method == "POST":

        if form.is_valid():
            user = request.user
            title = form.cleaned_data["title"]
            category = form.cleaned_data["category"]
            location = form.cleaned_data["location"]
            dates = form.cleaned_data["dates"]
            description = form.cleaned_data["description"]

            new_listing = Listing.objects.create(user=user, title=title, dates=dates,
                                                 category=category, location=location, description=description)

            new_listing.save()

            return HttpResponseRedirect(reverse("index"))

        else:
            messages.error(request, "Error")

            return render(request, "avail_listings/create_listing.html", {
                'form': NewListingForm()
            })

    else:
        return render(request, "avail_listings/create_listing.html", {
            'form': form
        })


def events(request):
    event = Event.objects.all()
    user = request.user

    return render(request, "avail_listings/events.html", {
        'Event': event,
        'user': user,
    })


@login_required
def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    user = request.user

    if listing.user == user:
        owner = True
    else:
        owner = False

    return render(request, "avail_listings/listing.html", {
        'Listing': listing,
        'user': user,
        'owner': owner,
    })


# The OP may mark their listing as inactive if they've found help
# Unfinished 
@login_required
def listing_inactive(request, listing_id):
    user = request.user
    listing = Listing.objects.get(pk=listing_id)
    listing.active = False
    listing.save()

    if listing.user == user:
        return render(request, "avail_listings.html", {
            'listing': listing,
            'message': "Thank you. This listing is now inactive and will no longer accept interest submissions."
        })
    else:
        return render(request, "avail_listings/listing_inactive.html", {
            'message': "This listing is inactive."
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "avail_listings/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "avail_listings/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "avail_listings/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "avail_listings/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "avail_listings/register.html")
