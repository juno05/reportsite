from django.contrib import admin
from .models import Code, CodeGroup, EscalationMatrix, Incident
# Register your models here.


admin.site.register(Code)
admin.site.register(CodeGroup)
admin.site.register(EscalationMatrix)
admin.site.register(Incident)

