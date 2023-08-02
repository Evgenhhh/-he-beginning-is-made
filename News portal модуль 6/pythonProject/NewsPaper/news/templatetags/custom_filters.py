from django import template
register = template.Library()

@register.filter(name='currency')
def currency(value):
    currency_list = ['запрет', 'запрет2', 'запрет3']
    list_z = value.split()

    for i in currency_list:
        for j in list_z:
            if j == i:
                a = list_z.index(j)
                list_z.remove(j)
                list_z.insert(a, '*' * len(j))
    return ' '.join(list_z)