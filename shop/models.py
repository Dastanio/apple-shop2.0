from django.db import models
import datetime 


class Product(models.Model):
	type = models.CharField("Название категории", max_length=100, default='')
	title = models.CharField('Название товара',max_length = 150)
	image = models.ImageField('Изображения', upload_to = 'shop/', blank = True)
	description = models.TextField('Описание')
	character = models.CharField('Характеристика', max_length = 300)
	pub_date = models.DateTimeField('Дата публикации', default = '')
	price = models.CharField('Цена', max_length = 100)


	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'


class Comment(models.Model):
	products = models.ForeignKey(Product, on_delete = models.CASCADE)
	date = models.DateTimeField('Дата публикации', default= '')
	author_name = models.CharField('Имя автора', max_length = 60)
	comment_text = models.TextField('Текст комментария')

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Комментария'
		verbose_name_plural = 'Комментарий'

