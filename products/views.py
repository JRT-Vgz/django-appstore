from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Product, Comment
from .forms import CommentsForm


def calculate_product_price_with_discount(product):
    if product.brand.discount > 0:
        final_price = product.price - (product.price * product.brand.discount / 100)
    return final_price

def index(request):
    products = Product.objects.all()
    return render(request, "products/list_of_products.html", {"products": products})

def get_product(request, id):
    try:   
        product = Product.objects.get(id=id)
        comments = Comment.objects.filter(product=id)
        form = CommentsForm()
        final_price = calculate_product_price_with_discount(product)
        return render(request, "products/show_product.html", 
                {"product": product, 
                "comments": comments,
                "form": form,
                "final_price": final_price})
    except:
        return redirect("index")
    

@login_required(login_url="login")
@permission_required("products.add_comment", raise_exception=True)
def add_new_comment(request, id):
    if request.method == "POST":
        form = CommentsForm(data=request.POST)
        if form.is_valid:
            user = request.user
            product = Product.objects.get(id=id)
            new_comment = form.save(commit=False)
            new_comment.author = user
            new_comment.product = product
            
            new_comment.save()
            
    return redirect("get_product", id)
    