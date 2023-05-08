from store.models import CartItem


def nav_bar_ctx(request):
    if request.user.is_authenticated:
        wishlist = request.user.wishlist.count()
        cart = CartItem.objects.filter(user=request.user).count()
    else:
        wishlist = len(request.session.get("wishlist", set()))
        cart = len(request.session.get("cart", set()))
    return {"wishlist": wishlist, "cart": cart}