 
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
    

@register.filter(name="get_title")
def get_titles(text):
    if text == None:
        return ''
    else: 
        return text
@register.filter(name="get_calculate")
def get_calc(order):
    cost  = 0 if order.cost ==None else order.cost
    scost  = 0 if order.shipping_cost ==None else order.shipping_cost
    dcost  = 0 if order.delivery_cost ==None else order.delivery_cost
    fee  = 0 if order.service_fee ==None else order.service_fee
    if order.hansh ==None:
        return '0'
    else:
        price = (cost + scost + dcost + fee)*order.hansh
        currency = "{:,.2f}".format(price)
        return str(currency)+"₮"
    
    
