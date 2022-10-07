from django.db import models
from django.template.defaultfilters import slugify

# todo add related_names to all relations


class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand_logos/', blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class SizeClothes(models.Model):
    class Sizes(models.TextChoices):
        S = "S", "Small"
        M = "M", "Medium"
        L = "L", "Large"
        XL = "XL", "Large Large"
        XXL = "XXL", "XLarge XLarge"
        OutOfStock = "OutOfStock", "OutOfStock"

    size = models.CharField(max_length=100, choices=Sizes.choices, default=Sizes.OutOfStock)

    class Meta:
        verbose_name_plural = "SizeClothes"

    def __str__(self):
        return self.size 

# toto add size choices 
class SizeFoot(models.Model):
    size = models.DecimalField(max_digits=3, decimal_places=1, default=0)



    def __str__(self):
        return str(self.size)


class Product(models.Model):

    name = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # sizes 
    size_clothes = models.ManyToManyField(SizeClothes, through="SizeClothesM2M",  through_fields=('product', 'size_clothes'), blank=True)

    size_foot = models.ManyToManyField(SizeFoot, blank=True)


    def __str__(self) -> str:
        return self.name


class SizeClothesM2M(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_clothes = models.ForeignKey(SizeClothes, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Size_Clothe"


class ProdPickture(models.Model):
    picture = models.ImageField(upload_to='prod_picktures/', blank=True)
    product = models.ForeignKey(Product, related_name="prod_picktures", on_delete=models.CASCADE)

    def __str__(self):
        return self.picture.url
