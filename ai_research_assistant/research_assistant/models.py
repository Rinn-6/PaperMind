from django.db import models


class ResearchPaper(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to="uploads/")
    extracted_text = models.TextField()
    summary = models.TextField(blank=True, null=True)
