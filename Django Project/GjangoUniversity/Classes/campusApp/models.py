from django.db import models


#Creates the model of university campus
class UniversityCampus(models.Model):
    Campus_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    Campus_ID = models.IntegerField(default="", blank=True, null=False)

    #creates model manager
    object = models.Manager()

    # Displays object output values in the form of a string
    def __str__(self):
    # Returns the input value of the campus name
    # field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.Campus_Name}'
        return display_campus.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"
