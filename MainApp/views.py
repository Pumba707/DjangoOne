from django.shortcuts import render
from django.http import HttpResponse
from MainApp.models import Item

full_name = "Романов П.В."
first_name = "Павел"
middle_name = "Витальевич"
last_name = "Романов"
phone = "+7 9272189162"
email = "pavel.v.romanov@megafon.ru"

#items = [
#    {"id": 1, "name": "Диван", "quantity":3},
#    {"id": 2, "name": "Чемодан", "quantity":1},
#    {"id": 3, "name": "Саквояж", "quantity":4},
#    {"id": 4, "name": "Картина", "quantity":1},
#    {"id": 5, "name": "Корзина", "quantity":5},
#    {"id": 6, "name": "Картонка", "quantity":9},
#    {"id": 7, "name": "маленькая собачонка", "quantity":0},
#]



def home(request):

    context = {
        'name':'Романов Павел',
        'email':'pavel.v.romanov@megafon.ru'
    }

    return render(request,"index.html",context)



def about(request):

    text = ""
    text += f"Имя: {first_name}<br>"
    text += f"Отчество: {middle_name}<br>"
    text += f"Фамилия: {last_name}<br>"
    text += f"телефон: {phone}<br>"
    text += f"email: {email}<br>"

    return HttpResponse(text)



def get_item(request,item_id):

    #for item in items:
    #    if item['id']==item_id:
    #        context = {
    #            'item': item
    #        }

    print(item_id)

    item = Item.objects.get(id=item_id)

    print(item)

    context = {
        'item': item
    }

    if not context:
        return HttpResponse(f"Товар с индексом {item_id} не найден")

    return render(request,"item.html",context)



def get_all_items(request):

    items = Item.objects.all()

    context = {
        'items' : items
    }

    return render(request,"items-list.html",context)
