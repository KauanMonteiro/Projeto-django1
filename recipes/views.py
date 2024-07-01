from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

def home(request):
    recipes = Recipe.objects.filter( is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(
         is_published=True,
         category__id=category_id
    ).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
         'title': f'{recipes[0].category.name}-Category'
    })

def recipe(request, id):
    recipe = Recipe.objects.filter(
        is_published=True,
        pk = id
    ).order_by('-id').first()
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
