from django.http import JsonResponse
from django.views import View

# Create your views here.


class AddToAndRemoveFromWishlistView(View):
    http_method_names = ["post", "delete"]

    def post(self, request, prod_id):
        user = request.user
        if user.is_authenticated:
            user.wishlist.add(id)
        else:
            wishlist = request.session.get("wishlist", set())
            wishlist.add(id)
            request.session["wishlist"] = wishlist
            request.session.modified = True
        return JsonResponse({"success": True})

    def delete(self, request, prod_id):
        user = request.user
        if user.is_authenticated:
            user.wishlist.remove(id)
        else:
            wishlist = request.session.get("wishlist", set())
            wishlist.remove(id)
            request.session["wishlist"] = wishlist
            request.session.modified = True
        return JsonResponse({"success": True})
