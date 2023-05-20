# from django.contrib import admin
# from fourth_app import *
#
# admin.site.register(Gym)
# class YearFilter(admin.SimpleListFilter):
#       title='Year'
#       parameter_name = 'year'
#
#       def lookups(self, request, model_admin):
#           years = [(year,year.year)
#                   for year in model_admin.model.objects.dates(field_name='year', kind='year')]
#           return sorted(years)
#
#       def queryset(self, request, queryset):
#           if self.value():
#               return queryset.filter(year=self.value())
#           else:
#               return queryset
# class GameAdmin(admin.ModelAdmin):
#     list_display = ('name','publisher','platform','year','id')
#     list_filter = (YearFilter,'platform')
#     search_fields = ('name','publisher')
#     ordering = ('id',)
#
#
# class YearFilterSon(admin.SimpleListFilter):
#     title = 'DateUtc'
#     parameter_name = 'DateUtc'
#
#     def lookups(self, request, model_admin):
#         years = [(DateUtc, DateUtc.DateUtc)
#                  for DateUtc in model_admin.model.objects.dates(field_name='DateUtc', kind='DateUtc')]
#         return sorted(years)
#
#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(DateUtc=self.value())
#         else:
#             return queryset
#
# class JSonAdmin(admin.ModelAdmin):
#     list_display = ('MatchNumber', 'RoundNumber', 'DateUtc', 'Location', 'HomeTeam','AwayTeam','Group','HomeTeamScore','AwayTeamScore')
#     list_filter = (YearFilter, 'Location')
#     search_fields = ('Location', 'DateUtc')
#     ordering = ('id',)








# Register your models here.
