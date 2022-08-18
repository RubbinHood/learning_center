from django.urls import path
from . import views

urlpatterns = [
    path('sign-in', views.SignInView.as_view(), name='UserSignInURL'),
    path('sign-up', views.SignUpView.as_view(), name='UserSignUpURL'),
    path('sign-out', views.sign_out, name='UserSignOutURL'),
    path('recovery', views.RecoveryView.as_view(), name='UserRecoveryURL'),
    path('<int:id>', views.UserProfileView.as_view(), name='profile'),
    path('', views.DashboardView.as_view(), name='UserDashboardURL'),
    path('profile', views.DashboardProfileView.as_view(), name='UserDashboardProfileURL'),
    path('courses', views.DashboardCoursesView.as_view(), name='dashboard_courses'),
    path('onlineclasses', views.DashboardOnlineClassesView.as_view(), name='dashboard_onlineclasses'),
    path('calender', views.DashboardCalenderView.as_view(), name='dashboard_calender'),
    path('support', views.DashboardSupportView.as_view(), name='dashboard_support'),
    path('password-reset-request', views.UserPasswordResetRequestView.as_view(), name='UserPasswordResetRequest'),
    path('password-reset/<int:activation_code>', views.UserPasswordResetRequestView.as_view(), name='UserPasswordReset'),
]