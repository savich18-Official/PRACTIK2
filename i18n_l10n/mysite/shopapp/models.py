from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


def product_preview_directory_path(instance: "Product", filename: str) -> str:
    return "products/product_{pk}/preview/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Product(models.Model):
    class Meta:
        ordering = ["name", "price"]
        verbose_name = _("Product")  # ✅ перевод модели
        verbose_name_plural = _("Products")

    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField(_("Description"), null=False, blank=True)
    price = models.DecimalField(_("Price"), default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(_("Discount"), default=0)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    archived = models.BooleanField(_("Archived"), default=False)
    preview = models.ImageField(
        _("Preview"),
        null=True,
        blank=True,
        upload_to=product_preview_directory_path
    )

    def __str__(self):
        return f"Product(pk={self.pk}, name={self.name!r})"


def product_images_directory_path(instance: "ProductImage", filename: str) -> str:
    return "products/product_{pk}/images/{filename}".format(
        pk=instance.product.pk,
        filename=filename,
    )


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name=_("Product"))
    image = models.ImageField(_("Image"), upload_to=product_images_directory_path)
    description = models.CharField(_("Description"), max_length=200, null=False, blank=True)

    class Meta:
        verbose_name = _("Product image")
        verbose_name_plural = _("Product images")


class Order(models.Model):
    class Meta:
        verbose_name = _("Order")  # ✅ перевод модели
        verbose_name_plural = _("Orders")

    delivery_address = models.TextField(_("Delivery address"), null=True, blank=True)
    promocode = models.CharField(_("Promo code"), max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_("User"))
    products = models.ManyToManyField(Product, related_name="orders", verbose_name=_("Products"))
    receipt = models.FileField(_("Receipt"), null=True, upload_to='orders/receipts/')
