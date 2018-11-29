from django.urls import path
from .views import professor_list, professor_new, professor_listPlan, update_professor, new_plan

app_name='professor'
urlpatterns = [
    path('', professor_list, name='list_prof'),
    path('new/', professor_new, name='create_prof'),
    path('update/<str:name>/', update_professor, name='update_prof'),
    path('plan/<int:discId>/', professor_listPlan, name='plano_aula'),
    path('plan/new/<int:profdisc>/', new_plan, name='novo_plano'),
    #path('new-disc/<int:id>/', prof_disc_new, name='update_prof'),
    # path('delete/<int:id>/', delete_product, name='delete_product'),
]