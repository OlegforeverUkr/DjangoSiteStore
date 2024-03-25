from django.shortcuts import render


def index(request):
    context = {
        "title": "Home - Главная",
        "content": "Pizza House HOME",
    }
    return render(request=request, template_name='main/index.html', context=context)


def about(request):
    context = {
        "title": "About - Про нас",
        "content": "About Page",
        "text_on_page": f"Мы — команда профессионалов, которая с любовью и страстью создает самую \
                         вкусную пиццу в городе. Наша история началась давно, когда маленькая пиццерия  \
                         открыла свои двери в сердце города. Мы гордимся тем, что используем только  \
                         самые свежие и качественные ингредиенты. Наши повара тщательно отбирают продукты, \
                         чтобы каждая пицца, которая покидает нашу кухню, была наивкуснейшей и удовлетворяла \
                         самые изысканные вкусы. Наше меню разнообразно и удовлетворит даже самых взыскательных \
                         гурманов. Мы предлагаем классические варианты пиццы, а также авторские рецепты, \
                         которые не оставят вас равнодушными. Благодаря разнообразию начинок и теста вы  \
                         всегда найдете именно то, что угодит вашему вкусу. Наша цель — не просто приготовить  \
                         пиццу, а создать для вас незабываемый опыт. Мы с нетерпением ждем вас в нашей пиццерии!"
    }
    return render(request=request, template_name='main/about.html', context=context)