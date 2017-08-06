from django.conf.urls import url
from ourfirstapp.views import signup_view, login_view, feed_view, post_view, like_view, comment_view

urlpatterns = [
    url('post/', post_view),
    url('feed/', feed_view),
    url('like/', like_view),
    url('comment/', comment_view),
    url('login/', login_view),
    url('', signup_view),

]
