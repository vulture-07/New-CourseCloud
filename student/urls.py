from django.urls import path
from student import views



urlpatterns=[
    path("register/",views.StudentRegistarationView.as_view(),name="student-register"),
    path("signin/",views.SignInView.as_view(),name="signin"),
    path("index/",views.IndexView.as_view(),name="index"),

    path ("course/<int:pk>/",views.CourseDetailView.as_view(),name="course-detail"),

    path("course/<int:pk>/add-to-cart/",views.AddToCartView.as_view(),name="cart-add"),

    path("cart/summary/",views.CartsummaryView.as_view(),name="cart-summary"),

    path("cart/<int:pk>/remove/",views.CartDeleteView.as_view(),name="cart-item-delete"),

    path("checkout/",views.CheckOutView.as_view(),name="check-out"),
    
    path("mycourse/",views.MyCourseView.as_view(),name="my-course"),

    path("course/<int:pk>/watch/",views.LessonDetailView.as_view(),name=("lesson-detail")),

    path("payament/verify/",views.PaymentVerificationView.as_view(),name="payment-verify"),

    path("signout/",views.SignOutView.as_view(),name="signout")

    
]