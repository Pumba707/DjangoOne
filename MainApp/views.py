from django.shortcuts import render
from django.http import HttpResponse

full_name = "Романов П.В."
first_name = "Павел"
middle_name = "Витальевич"
last_name = "Романов"
phone = "+7 9272189162"
email = "pavel.v.romanov@megafon.ru"

items = [
    {"id": 1, "name": "Диван"},
    {"id": 2, "name": "Чемодан"},
    {"id": 3, "name": "Саквояж"},
    {"id": 4, "name": "Картина"},
    {"id": 5, "name": "Корзина"},
    {"id": 6, "name": "Картонка"},
    {"id": 7, "name": "маленькая собачонка"},
]
 
def home(request):

    text = f"""<h1>"Изучаем django"</h1>
<strong>Автор</strong>: <i>{full_name}</i>"""

    return HttpResponse(text)

def about(request):

    text = ""
    text += f"Имя: {first_name}<br>"
    text += f"Отчество: {middle_name}<br>"
    text += f"Фамилия: {last_name}<br>"
    text += f"телефон: {phone}<br>"
    text += f"email: {email}<br>"

    return HttpResponse(text)

def get_item(request,item_id):

    text = ""
    for item in items:
        if item['id']==item_id:
            text+=item['name']+"<br>"

    if text == "":
        text=f"Товар с индексом {item_id} не найден"

    return HttpResponse(text)

def get_all_items(request):

    text = ""
    for item in items:
        text+=f"""<a href=/item/{item['id']}>{str(item['id'])} {item['name']}</a><br>"""

    return HttpResponse(text)