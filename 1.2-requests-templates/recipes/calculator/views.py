from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home_view(request):
    template_name = 'calculator/index.html'
    return render(request, template_name)


def omlet_view(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get("servings", 1))
    context = {
        'recipe':
            {
                'яйца, шт': 2 * servings,
                'молоко, л': 0.1 * servings,
                'соль, ч.л.': 0.5 * servings,
            }
    }

    return render(request, template_name, context)


def pasta_view(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get("servings", 1))
    context = {
        'recipe': {
            'макароны, г': 0.3 * servings,
            'сыр, г': 0.05 * servings,
        },
    }
    return render(request, template_name, context)


def buter_view(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get("servings", 1))
    context = {
        'recipe': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
    }
    return render(request, template_name, context)
