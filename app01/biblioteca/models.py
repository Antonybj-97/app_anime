from django.db import models
from django.urls import reverse


class Editorial(models.Model):
    name = models.CharField(max_length=255, verbose_name='Editorial')
    adress = models.CharField(max_length=255, verbose_name='Direccion')
    phone = models.CharField(max_length=20, verbose_name= 'Telefono')
    email = models.EmailField(max_length=100, verbose_name= 'Email')
    country = models.CharField(max_length=100, verbose_name= 'Pais')

    def __str__(self):
        return self.name
       
    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'

class Author(models.Model):
    firstname = models.CharField(max_length=80, verbose_name='Nombre')
    lastname = models.CharField(max_length=80, verbose_name='Apellido(s)')
    birthday = models.DateField(verbose_name='Fecha de nacimiento')
    nationality = models.CharField(max_length=50, verbose_name='Nacionalidad')

    def _str_(self): 
        return "{0} {1} :: {2}".format(self.firstname, self.lastname, self.nationality)           

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Book(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Autor')
    editorial_id = models.ForeignKey(Editorial, on_delete=models.CASCADE, verbose_name='Edirorial')
    title = models.CharField(max_length=255, verbose_name='Titulo')
    isd = models.CharField(max_length=50, verbose_name='ISBN')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Pricio')
    edition = models.CharField(max_length=50, verbose_name='Edicion')
    numPages = models.PositiveIntegerField(verbose_name='Numero de páginas')
    pubYear = models.CharField(max_length=4, verbose_name='Año de publicación')

    def __str__(self):
        return "{0}".format(self.title)
       
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'


