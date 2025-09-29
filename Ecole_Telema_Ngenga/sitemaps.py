from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import BlogPost

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'pages:accueil', 
            'pages:a-propos', 
            'pages:histoire',
            'pages:mission',
            'equipe:equipe', 
            'actions:actions', 
            'blog:post_list', 
            'contact:contact'
        ]

    def location(self, item):
        return reverse(item)

class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        # On ajoute un ordre pour éviter le warning
        return BlogPost.objects.order_by('pk')

    def lastmod(self, obj):
        return obj.date_publication
