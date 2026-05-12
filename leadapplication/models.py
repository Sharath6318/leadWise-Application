from django.db import models

from django.db import models

class Lead(models.Model):

    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('proposal', 'Proposal Sent'),
        ('won', 'Won'),
        ('lost', 'Lost'),
    ]

    SOURCE_CHOICES = [
        ('website', 'Website'),
        ('referral', 'Referral'),
        ('linkedin', 'LinkedIn'),
        ('ads', 'Ads'),
        ('cold_call', 'Cold Call'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=100, blank=True, null=True)

    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    requirement = models.TextField()


    next_follow_up_date = models.DateField(blank=True, null=True)
    last_contacted_date = models.DateField(blank=True, null=True,auto_now=True)


    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name