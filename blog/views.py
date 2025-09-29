from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.core.paginator import Paginator
from django.db.models import F

def post_list(request):
    all_posts = BlogPost.objects.all().order_by('-date_publication')
    paginator = Paginator(all_posts, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    # Logique pour le compteur de vues unique par session
    viewed_posts = request.session.get('viewed_posts', [])
    if post.pk not in viewed_posts:
        post.views = F('views') + 1
        post.save()
        viewed_posts.append(post.pk)
        request.session['viewed_posts'] = viewed_posts

    # Logique pour le "like" unique par session
    liked_posts = request.session.get('liked_posts', [])
    if request.method == 'POST':
        if post.pk not in liked_posts:
            post.likes = F('likes') + 1
            post.save()
            liked_posts.append(post.pk)
            request.session['liked_posts'] = liked_posts
        return redirect('blog:post_detail', pk=post.pk)

    # Recharger l'objet pour avoir les dernières valeurs
    post.refresh_from_db()

    context = {
        'post': post,
        'has_liked': post.pk in liked_posts
    }
    return render(request, 'blog/post_detail.html', context)
