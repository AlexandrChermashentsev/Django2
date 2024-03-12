from django import forms

class ProductForm(forms.Form):
    name_product = forms.CharField(max_length=50, label='Название продукта')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    price = forms.DecimalField(label='Цена')
    quantity = forms.IntegerField(min_value=1, label='Количество')
    date_add = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 
                                                             'type': 'date'}),
                               label='Дата добавления')
    image = forms.ImageField(label='Изображение')

class ClientForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=100, label="Имя")
    email = forms.EmailField(label="Электронная почта")
    phone_number = forms.CharField(max_length=15, label="Номер телефона")
    address = forms.CharField(widget=forms.Textarea, label="Домашний адрес")
    date_registration = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 
                                                                      'type': 'date'}),
                                                               label="Дата регистрации")