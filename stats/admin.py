from django.contrib import admin

from .models import Stat
from obj_ev.models import ObjEv
from users.models import Userc

admin.site.register(Userc)



@admin.register(Stat)
class PostAdmin(admin.ModelAdmin):
    """regists article in admin panel"""



@admin.register(ObjEv)
class ObjEvAdmin(admin.ModelAdmin):
    """regists tags in admin panel"""

    pass


