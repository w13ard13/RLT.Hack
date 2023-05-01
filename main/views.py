from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import CheckINNForm
from .data.scripts.filter_1 import FilterBase
from .data.scripts.filter_2_and_rating import FilterAndRating


class IndexView(View):
	template_name = 'main/base.html'
	
	def get(self, *args, **kwargs):
		form = CheckINNForm()
		context = {'form': form}
		return render(self.request, self.template_name, context)
		
	def post(self, *args, **kwargs):
		form = CheckINNForm(self.request.POST)
		if form.is_valid():
			
			price_min = form.cleaned_data['price_min']
			price_max = form.cleaned_data['price_max']
			okved = form.cleaned_data['okved']
			deadline = form.cleaned_data['deadline']
			
			expertise = form.cleaned_data['expertise']
			debt = form.cleaned_data['debt']
			staff = form.cleaned_data['staff']
			try:
				filterBase = FilterBase(price_min, price_max, okved, deadline)
				filt1 = filterBase.make()
				
				objFilter = FilterAndRating(expertise, debt, staff)
				df = objFilter.make()
				
				context = {
					'price_min': price_min,
					'price_max': price_max,
					'okved': okved,
					'deadline': deadline,
					'expertise': expertise,
					'debt': debt,
					'staff': staff,
					'form': form,
					'df': df
				}
			except:
				return HttpResponse("По запросу не найдено поставщиков. Пожалуйста, попробуйте расширить ценовой диапазон или увеличить количество дней.")
			return render(self.request, self.template_name, context)
		else:
			return HttpResponse("Form is invalid")
