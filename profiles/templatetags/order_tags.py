 
from django import template


register = template.Library()

@register.filter(name="get_status")
def get_order_status(status):
    if status == 'N':
        return 'Шинэ'
    elif status =='F':
        return 'Цуцалсан'
    elif status =='D': 
        return 'Дууссан'
    elif status =='B': 
        return 'Буцаагдсан'
    elif status =='O': 
        return 'Захиалсан'
    elif status =='C': 
        return 'Үнэ бодогдсон'
    elif status =='P': 
        return 'Төлбөр төлөгдсөн'
    else: 
        return 'Мэдээлэл буруу'

@register.filter(name="get_text")
def get_texts(text):
    if text == None:
        return '-'
    else: 
        return text
    
