from django import forms


class CheckINNForm(forms.Form):

	price_min = forms.IntegerField(label = 'Минимальная стоимость контракта, руб.')
	price_max = forms.IntegerField(label = 'Максимальная стоимость контракта, руб.')
	okved = forms.CharField(label = 'ОКПД организации')
	deadline = forms.IntegerField(label = 'Срок выполнения (в днях)')
	expertise = forms.IntegerField(label = 'Опыт поставщика на рынке (в годах)')
	debt = forms.IntegerField(label = 'Длительность без исполнительных производст (в годах)')
	staff = forms.IntegerField(label = 'Минимальное количество специалистов для оказания услуг')