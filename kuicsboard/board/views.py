from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from .forms import BoardForm
from .models import BoardItem


NUM_ITEMS = 8


def list(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(BoardItem.objects.all(), NUM_ITEMS)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {
        'items': items,
        'item_page_offset': items.paginator.num_pages - items.number,
    })


def view(request, board_id):
    item = get_object_or_404(BoardItem, pk=board_id)
    if item.private and item.written_by != request.user:
        messages.error(request, '비밀글은 글 작성자만 볼 수 있습니다.')
        return redirect('board:list')
    else:
        return render(request, 'item.html', {
            'item': item,
        })


def add(request):
    return render(request, 'item_edit.html', {
        'form': BoardForm(),
        'title': '새로운 글 쓰기',
        'target_url': reverse('board:add_submit')
    })


def update(request, board_id):
    item = get_object_or_404(BoardItem, pk=board_id)
    return render(request, 'item_edit.html', {
        'form': BoardForm(item),
        'title': '글 수정하기',
        'target_url': reverse(
            'board:update_submit', kwargs={'board_id': board_id}
        )
    })


def _auth(request, id, pw):
    user = authenticate(username=id, password=pw)
    if user:
        if user.is_staff:
            return '관리자 계정으로 로그인할 수 없습니다.'
        elif user.is_active:
            login(request, user)
            return None
    else:
        return '올바르지 않은 계정입니다.'


def auth(request):
    return render(request, 'auth.html')


def auth_logout(request):
    logout(request)
    messages.info(request, '로그아웃 되었습니다. 다음에 또 봐요!')
    return redirect('board:list')


@require_http_methods(['POST'])
def auth_submit(request):
    auth_result = _auth(
        request,
        request.POST.get('username'),
        request.POST.get('password')
    )

    if auth_result is not None:
        messages.error(request, auth_result)

    return redirect('board:list')


@require_http_methods(['POST'])
def add_submit(request):
    form = BoardForm(request.POST)
    user = None
    if not form.is_valid():
        error = next(iter(form.errors.values()))
    else:
        error = None
        name, password = (
            form.data.get('written_by_name'),
            form.data.get('written_by_password'),
        )

        if not request.user.is_authenticated():
            if not all([name, password]):
                error = '글쓴이 정보를 입력해주세요.'
            else:
                try:
                    user = User.objects.create_user(name, None, password)
                    _auth(request, name, password)
                except IntegrityError:
                    error = '이미 존재하는 회원 이름입니다.'
        else:
            user = request.user

    if error:
        messages.error(request, error)
        target = 'board:add'
    else:
        BoardItem.create(request, form.cleaned_data, user)
        messages.info(request, '새 글이 등록되었습니다.')
        target = 'board:list'

    return redirect(target)


@require_http_methods(['POST'])
def update_submit(request, board_id):
    pass
