from django.db import models


class Base(models.Model):
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)
    actived = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Document(Base):
    id_doc = models.IntegerField(default=0)
    path = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=100)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Dossie'

    def __str__(self):
        return self.titulo


class History(Base):
    document = models.ForeignKey(Document, related_name='histories', on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    start_hour = models.DateTimeField(auto_now=True)
    end_hour = models.DateTimeField()

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Histories'
        # unique_together = ['document']

        def __str__(self):
            return f'{self.action} iniciou em {self.start_hour} e finalizou as {self.end_hour}'