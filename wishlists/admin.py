from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",  # name 과 동일.
        "user",
        "created_at",
        "updated_at",
    )
