from django.db import models

SUBJECT_CHOICES = [
    ('maths', 'Mathematics'),
    ('science', 'Science'),
    ('social_science', 'Social Science'),
    ('english', 'English'),
    ('hindi', 'Hindi'),
]


class Query(models.Model):
    """A student's question submitted from a subject page."""
    subject = models.CharField(max_length=30, choices=SUBJECT_CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_subject_display()} - {self.name} ({self.created_at:%Y-%m-%d})"
