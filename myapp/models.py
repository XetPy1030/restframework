from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AnimalType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Animal(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StatusOrder(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
    status = models.ForeignKey(StatusOrder, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.animal.name


if not Category.objects.exists():
    Category.objects.create(name='Опасные')
    Category.objects.create(name='Безопасные')
    Category.objects.create(name='Другое')

if not AnimalType.objects.exists():
    AnimalType.objects.create(name='Кошка')
    AnimalType.objects.create(name='Собака')
    AnimalType.objects.create(name='Грызун')
    AnimalType.objects.create(name='Птица')
    AnimalType.objects.create(name='Рептилия')
    AnimalType.objects.create(name='Рыба')
    AnimalType.objects.create(name='Грызун')
    AnimalType.objects.create(name='Другое')

if not Status.objects.exists():
    Status.objects.create(name='В приюте')
    Status.objects.create(name='На улице')
    Status.objects.create(name='Утерян')
    Status.objects.create(name='Пропал')
    Status.objects.create(name='Усыновлен')
    Status.objects.create(name='Умер')
    Status.objects.create(name='Другое')

if not StatusOrder.objects.exists():
    StatusOrder.objects.create(name='Размещен')
    StatusOrder.objects.create(name='Обработан')
    StatusOrder.objects.create(name='Выполнен')

if not Animal.objects.exists():
    Animal.objects.create(
        category=Category.objects.get(name='Опасные'),
        animal_type=AnimalType.objects.get(name='Кошка'), name='Барсик',
        photo='https://w-dog.ru/wallpapers/4/2/514786505767463/polosataya-koshka-lezhit-otdyxaet-na-stole.jpg',
        status=Status.objects.get(name='В приюте')
    )
    Animal.objects.create(
        category=Category.objects.get(name='Безопасные'),
        animal_type=AnimalType.objects.get(name='Собака'), name='Шарик',
        photo='https://mobimg.b-cdn.net/v3/fetch/1a/1ad32de01c3b5950abdab32cf250a1cd.jpeg',
        status=Status.objects.get(name='Усыновлен')
    )

if not Order.objects.exists():
    Order.objects.create(animal=Animal.objects.get(name='Барсик'), quantity=1, date='2021-05-01',
                         status=StatusOrder.objects.get(name='Размещен'), is_done=False)
    Order.objects.create(animal=Animal.objects.get(name='Шарик'), quantity=1, date='2021-05-01',
                         status=StatusOrder.objects.get(name='Размещен'), is_done=False)