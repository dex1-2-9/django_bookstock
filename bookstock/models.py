from django.db import models

# Create your models here.

#category_choice = (
#    ('Sci-Fi', 'Sci-Fi'),
#    ('Fantasy', 'Fantasy'),
#    ('History', 'History'),
#    ('Comics','Comics'),
#    ('Poetry', 'Poetry'),
#    ('Science','Science'),
#    ('Action', 'Action'),
#    ('Adventure', 'Adventure'),
#    ('Nature', 'Nature')
#)


class Kategorie(models.Model):
    item_name = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.item_name

class Stock(models.Model):
    category = models.ForeignKey(Kategorie, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(default='1', blank=False, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
	    return self.item_name