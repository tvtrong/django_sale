from django.urls import path
from . import views


urlpatterns = [
    path('', views.kho, name='kho'),
    # ---------NHAN
    path('nhan/', views.IndexNhan.as_view(), name='nhan'),
    path('create_n/', views.NhanCreateView.as_view(), name='create_nhan'),
    path('update_n/<str:pk>', views.NhanUpdateView.as_view(), name='update_nhan'),
    path('read_n/<str:pk>', views.NhanReadView.as_view(), name='read_nhan'),
    path('delete_n/<str:pk>', views.NhanDeleteView.as_view(), name='delete_nhan'),
    # ---------DON VI
    path('donvi/', views.IndexDonvi.as_view(), name='donvi'),
    path('create_dv/', views.DonViCreateView.as_view(), name='create_donvi'),
    path('update_dv/<str:pk>', views.DonViUpdateView.as_view(), name='update_donvi'),
    path('read_dv/<str:pk>', views.DonViReadView.as_view(), name='read_donvi'),
    path('delete_dv/<str:pk>', views.DonViDeleteView.as_view(), name='delete_donvi'),
    # ---------NGUOI BAN
    path('nguoiban/', views.IndexNguoiBan.as_view(), name='nguoiban'),
    path('create_nb/', views.NguoiBanCreateView.as_view(), name='create_nguoiban'),
    path('update_nb/<str:pk>', views.NguoiBanUpdateView.as_view(),
         name='update_nguoiban'),
    path('read_nb/<str:pk>', views.NguoiBanReadView.as_view(), name='read_nguoiban'),
    path('delete_nb/<str:pk>', views.NguoiBanDeleteView.as_view(),
         name='delete_nguoiban'),
    # ---------SAN PHAM
    path('sanpham/', views.IndexSanPham.as_view(), name='sanpham'),
    path('create_sp/', views.SanPhamCreateView.as_view(), name='create_sanpham'),
    path('update_sp/<str:pk>', views.SanPhamUpdateView.as_view(),
         name='update_sanpham'),
    path('read_sp/<str:pk>', views.SanPhamReadView.as_view(), name='read_sanpham'),
    path('delete_sp/<str:pk>', views.SanPhamDeleteView.as_view(),
         name='delete_sanpham'),
    # ---------NHAP KHO
    path('nhapkho/', views.IndexNhapKho.as_view(), name='nhapkho'),
    path('create_nk/', views.NhapKhoCreateView.as_view(), name='create_nhapkho'),
    path('update_nk/<str:pk>', views.NhapKhoUpdateView.as_view(),
         name='update_nhapkho'),
    path('read_nk/<str:pk>', views.NhapKhoReadView.as_view(), name='read_nhapkho'),
    path('delete_nk/<str:pk>', views.NhapKhoDeleteView.as_view(),
         name='delete_nhapkho'),
]
