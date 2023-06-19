from django import forms

from catalog.models import Product, Versions


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        """Проверяет, ввёл ли пользователь запрещённые слова в title или description"""
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'] #Список слов которые нельзя вводить в title и description

        for word in forbidden_words:
            if word in title.lower() or word in description.lower():
                raise forms.ValidationError(f'Слово "{word}" запрещено в названии и описании') #Если нашлись слова из списка, то генерируем ошибку

        return cleaned_data

class VersionsForm(forms.ModelForm):

    def clean_is_active(self):
        """"Устанавливает изменяемую/создаваемую версию продукта как текующую версию"""
        is_active = self.cleaned_data.get('is_active')
        product = self.cleaned_data.get('product')
        Versions.objects.filter(product=product).exclude(id=self.instance.id).update(is_active=False) #Отфильтровать по продукту, исключить текущую версию и установаить остальным версиям этого продукта is_active = False
        return is_active

    class Meta:
        model = Versions
        fields = '__all__'