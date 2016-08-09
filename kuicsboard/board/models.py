from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from . import helper


class BoardItem(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '게시글'

    def __str__(self):
        return '{} ({} 작성)'.format(self.title, self.created_at)

    title = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    written_by = models.ForeignKey(User, verbose_name='작성자')
    written_from = models.CharField('REMOTE_ADDR', max_length=100)
    created_at = models.DateTimeField('생성일', default=timezone.now)
    updated_at = models.DateTimeField('수정일', default=timezone.now)

    locked = models.BooleanField('글 수정 불가 여부', default=False)
    private = models.BooleanField('비밀글 여부', default=False)

    @classmethod
    def create(cls, request, form, user):
        model = cls(
            title=form['title'],
            content=form['content'],
            private=form['private'],
            written_by=user,
            written_from=request.META.get('REMOTE_ADDR'),
            created_at=timezone.now()
        )

        model.save()
