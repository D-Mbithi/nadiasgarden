from django.shortcuts import render
from django.forms import formset_factory

from .forms import PizzaForm, PizzaMultiForm

# Create your views here.
def home(request):
    return render(request, 'index.html')


def order(request):
    multiform = PizzaMultiForm()
    if request.method == "POST":
        form = PizzaForm(request.POST)

        if form.is_valid():
            form.save()
            
            size = form.cleaned_data['size']
            topping1 = form.cleaned_data['topping1']
            topping2 = form.cleaned_data['topping2']
    
    form = PizzaForm()
    
    return render(request, 'order.html', {'form': form, 'multiform': multiform})


def pizzas(request):
    number_of_pizza = 2
    filled_multiform = PizzaMultiForm(request.GET)

    if filled_multiform.is_valid():
        number_of_pizza = filled_multiform.cleaned_data['number']
    
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizza)
    formset = PizzaFormSet()

    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            print('Order created successfuly, your pizzas are on the way.')
        else:
            print('Order not created, please try again')

    return render(request, 'pizzas.html', {'formset': formset})