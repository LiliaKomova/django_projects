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


def dish_view(request, dish):

    template_name = 'calculator/index.html'

    servings = int(request.GET.get("servings", 1))
    for i in DATA.values():
        for k, v in i.items():
            i[k] = v * servings

    context = {
        'recipe': DATA[dish]
    }

    if dish in DATA.keys():
        return render(request, template_name, context)
    else:
        return render(request, template_name)
