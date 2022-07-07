from django.http import HttpResponse
from django.shortcuts import render
from data_ import DATA_

def home(request):
    recipe_list = list(DATA_.keys())
    return render(request, 'index.html', context={'name': recipe_list})

def make_recipes(request, dishes):
    if dishes in DATA_:
        recipe = {}
        serving = int(request.GET.get('servings', 1))
        
        for k, v in DATA_[dishes].items():
            recipe[k] = round(serving * v, 2)
            context = {
                'recipe': recipe, 
                'name': dishes, 
                'serving': serving}
    else:
        return render (request, 'notrecipe.html')
        
    return render(request, 'recipes.html', context)