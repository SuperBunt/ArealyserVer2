from django.db import models

# Create your models here.
# PPR
class PPR(models.Model):
    COUNTIES = (  
        ('Carlow','Carlow'),
        ('Cavan','Cavan'),
        ('Clare','Clare'),
        ('Cork','Cork'),
        ('Donegal','Donegal'),
        ('Dublin','Dublin'),
        ('Galway','Galway'),
        ('Kerry','Kerry'),
        ('Kildare','Kildare'),
        ('Kilkenny','Kilkenny'),
        ('Laois','Laois'),
        ('Leitrim','Leitrim'),
        ('Limerick','Limerick'),
        ('Longford','Longford'),
        ('Louth','Louth'),
        ('Mayo','Mayo'),
        ('Meath','Meath'),
        ('Monaghan','Monaghan'),
        ('Offaly','Offaly'),
        ('Roscommon','Roscommon'),
        ('Tipperary','Tipperary'),
        ('Waterford','Waterford'),
        ('Westmeath','Westmeath'),
        ('Wexford','Wexford'),
        ('Wicklow','Wicklow')  
    )
    
    BOOL_CONVERT = (
        (0, 'No'),
        (1, 'Yes')
    )
    address = models.TextField('Address')
    county = models.CharField('County', max_length=10, choices=COUNTIES)
    price = models.DecimalField('Price', max_digits=12, decimal_places=2)
    # description = models.CharField('Description', max_length=40, choices=TYPE)
    date_of_sale = models.DateField()
    not_full_market = models.BooleanField('Not Full Market Price', choices=BOOL_CONVERT, default=1)
    # vat_exclusive = models.BooleanField('VAT Exclusive', default=0)
    # postal_code = models.CharField('Postal Code', max_length=18, default="")
    # prop_size_desc = models.CharField('Size description', max_length=80, default="")
    # longitude = models.DecimalField(max_digits=3, decimal_places=6)
    # latitude = models.DecimalField(max_digits=3, decimal_places=6)

    def __str__(self):
        return u'Address: {0}, Price: &euro; {1}'.format(self.address, self.price) 

    class Meta:
        app_label = 'arealyser'
        ordering = ['date_of_sale']
#endregion