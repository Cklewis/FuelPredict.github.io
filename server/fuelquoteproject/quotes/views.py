from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import FuelQuote, FuelQuoteModifier
from .forms import FuelQuoteModelForm
from decimal import * #decimals imported

# Create your views here.

def quote_detail_page(request, fuel_quote_id):
  obj = get_object_or_404(FuelQuote, id=fuel_quote_id)
  context = {"object": obj}
  return render(request, 'pages/quote.html', context)

def quote_confirmation_page(request, quote_id):
  obj = get_object_or_404(FuelQuote, id=quote_id)

  context = {
    'obj': obj
  }

  if request.method=='POST' and 'confirm' in request.POST:
    obj.save()
    return redirect(reverse('quotes'))
  elif request.method=='POST' and 'delete' in request.POST:
    obj.delete()
    return redirect(reverse('get_quote'))
    
  
  return render(request,'pages/quote_confirmation.html', context)



def quotes(request):
  if request.user.is_authenticated:
    my_qs = FuelQuote.objects.filter(user=request.user)
    context = {'object_list': my_qs}
    return render(request, 'pages/quote_list.html', context)
  else:
    return render(request, 'pages/quote_list.html')

def get_quote(request):
  form = FuelQuoteModelForm(request.POST or None)
  user = request.user
  if form.is_valid():
    obj = form.save(commit=False) 
    obj.user = request.user
    fuel_modifier_obj = get_object_or_404(FuelQuoteModifier, id=1)
    date_month = obj.delivery_date.strftime('%B')
    price_per_gallon = fuel_modifier_obj.price_per_gallon
    price_per_gallon = float(price_per_gallon)
    profit_margin = float(fuel_modifier_obj.profit_margin)


    # Apply Seasonal Fluctuation 
    if date_month in {'March', 'April', 'May', 'June', 'July', 'August'}:
      summer_modifier = float(fuel_modifier_obj.summer_modifier)
      price_per_gallon = price_per_gallon * (1 + summer_modifier)
    
    quotes_list = FuelQuote.objects.filter(user=request.user)

    # Apply Discounts 
    if len(quotes_list) > 15:
      price_per_gallon = price_per_gallon - 0.15
      discounts = obj.gallons_requested * 0.15
    elif len(quotes_list) > 10:
      price_per_gallon = price_per_gallon - 0.10
      discounts = obj.gallons_requested * 0.10
    elif len(quotes_list) > 5:
      price_per_gallon = price_per_gallon - 0.05
      discounts = obj.gallons_requested * 0.05
    else:
      discounts = 0

    # Apply Transportation 
    if obj.delivery_state not in ['TX']:
      price_per_gallon = price_per_gallon + 0.90

    # Calculate Total Amount Due
    price_per_gallon = price_per_gallon + profit_margin
    obj.total_amount_due = obj.gallons_requested * price_per_gallon
    obj.price_per_gallon = price_per_gallon

    #Calculate Total Discounts
    obj.discounts = discounts

    context = {
      "quote_amount": obj.total_amount_due,
      "quote_id": obj.id,
      "obj": obj
    }

    obj.save()
    quote_id = obj.id
    return redirect('confirm', quote_id)
  context = {
    "form": form,
    "user": user
  }
  return render(request, 'pages/get_quote.html', context)