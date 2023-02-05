from django.shortcuts import render
from django.views import generic
from . import models
from django.db.models import Q, F, Sum, Avg, Count, Max, Prefetch
from itertools import islice, chain
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import WishListSerializer
from users.models import User

# Create your views here.
class Home(generic.TemplateView):
    template_name = "index.html"
    queryset = (
        models.Product.objects.filter(available=True)
        .filter(options__quantity__gt=0)
        .prefetch_related(
            Prefetch(
                "options",
                queryset=models.Option.objects.prefetch_related("order_items").all(),
            )
        )
        .prefetch_related("images")
        .distinct()
    )
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = models.Category.objects.all()
        ctx["new_arrivals"] = self.queryset.order_by("-created")

        popular_products_ids = models.Popular_Products.objects.all()[:8].values_list(
            "id", flat=True
        )
        popular_products = self.queryset.annotate(
            is_popular=Q(id__in=popular_products_ids)
        ).filter(is_popular=True)

        most_paid_products = (
            self.queryset.annotate(count=Count("options__order_items"))
            .order_by("-count")
            .exclude(Q(id__in=popular_products_ids))[: 8 - len(popular_products)]
        )

        ctx["popular_products"] = chain(popular_products, most_paid_products)
        
        return ctx



class WishList_ListCreateApiView(APIView):
    serializer_class = WishListSerializer

    def post(self, request, *args, **kwargs):
        id = int(request.data['id'])
        user = request.user
        if user.is_authenticated:
            user.wishlist.add(id)
            user.save()
            return Response({"success":True})
        

        value = request.session.get('wishlist')
        
        if not value:
            request.session['wishlist'] = [id]
            request.session.modified = True
        else:
            if id not in request.session['wishlist']:
                request.session['wishlist'].append(id)
                request.session.modified = True
            else:
                request.session['wishlist'].remove(id)
                request.session.modified = True
                return Response({"deleted":True})

        return Response({"success":True})
