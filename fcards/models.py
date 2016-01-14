from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    # Relations
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="profile",
                                verbose_name="user")

    # Attributes
    sets = models.PositiveIntegerField(default=0,
                                       verbose_name="list of sets")
    # Custom Properties
    @property
    def username(self):
        return self.user.username
    
    # Methods
    
    # Meta and Unicode
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ("user",)
        
    def __unicode_(self):
        return self.user.username
    
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    # checks if a new instance of the User has been created
    # if true, creates a Profile instance using the new user instance
    if created:
        profile = Profile(user=instance)
        profile.save()
        
        
class Subject(models.Model):
    # Relations
    # each subject instance must be related to one User Profile
    # each User Profile can be related to 0, 1 or more subjects
    user = models.ForeignKey(Profile,
                             related_name="subjects",
                             verbose_name="user")
        
    # Attributes
    name = models.CharField(max_length=50,
                            verbose_name="name",
                            help_text="Enter the subject name")
    
    # Meta and Unicode
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        ordering = ("user", "name")
        unique_together = ("user", "name")
        
    def __unicode__(self): 
        return "%s - %s" % (self.user.username, self.name)        
    
    
class Card(models.Model):
    # Relations
    card = models.ForeignKey(Subject,
                             related_name="flashcards",
                             verbose_name="flashcard",
                             null=True,
                             blank=True)
    
    # Attributes
    term = models.CharField(max_length=100,
                            verbose_name="term",
                            help_text="Enter the term")
    
    defin = models.TextField(verbose_name="definition",
                             help_text="Enter the definition")
    
    created = models.DateTimeField(default=timezone.now)
    
    # Meta and Unicode
    class Meta:
        verbose_name = "Flashcard"
        verbose_name_plural = "Flashcards"
        
    def __unicode__(self):
        return "%s - %s" % (self.term, self.defin)
