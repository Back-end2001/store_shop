from django.db import models



class Category(models.Model):
      name = models.CharField(verbose_name="Category name", max_length=100)


      def  __str__(self):
          return self.name

      class Meta:
          verbose_name = "Category"
          verbose_name_plural = "Categories"

class Product(models.Model):
      name = models.CharField(verbose_name="Product name", max_length=250)
      price= models.FloatField(verbose_name="Product price")
      create_date = models.DateTimeField(verbose_name="Product create date", auto_now_add=True)
      update_date = models.DateTimeField(verbose_name="Product update date", auto_now=True)
      description = models.TextField(verbose_name="Product description")
      image = models.ImageField(upload_to="products/", verbose_name="Product image")


      def get_image(self):
          if self.image.url:
              return self.image.url
          else:
              return None



      def __str__(self):
          return self.name

      class Meta:
          verbose_name = "Product"
          verbose_name_plural = "Products"


class Order(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)