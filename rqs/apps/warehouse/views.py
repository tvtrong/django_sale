from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from .models import *
from bootstrap_modal_forms.generic import (
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)


def kho(request):
    return render(request, 'warehouse/kho.html')


'''
''''''''''''''''''NHAN
'''


class IndexNhan(generic.ListView):
    model = Nhan
    context_object_name = 'nhans'
    template_name = 'warehouse/Nhan/nhan.html'

# Create


class NhanCreateView(BSModalCreateView):
    template_name = 'warehouse/Nhan/create_nhan.html'
    form_class = NhanModelForm
    success_message = 'Success: Nhan was created.'
    success_url = reverse_lazy('nhan')

# Update


class NhanUpdateView(BSModalUpdateView):
    model = Nhan
    template_name = 'warehouse/Nhan/update_nhan.html'
    form_class = NhanModelForm
    success_message = 'Success: Nhan was updated.'
    success_url = reverse_lazy('nhan')

# Read


class NhanReadView(BSModalReadView):
    model = Nhan
    template_name = 'warehouse/Nhan/read_nhan.html'

# Delete


class NhanDeleteView(BSModalDeleteView):
    model = Nhan
    template_name = 'warehouse/Nhan/delete_nhan.html'
    success_message = 'Success: Nhan was deleted.'
    success_url = reverse_lazy('nhan')


'''
''''''''''''''''''DON VI
'''


class IndexDonvi(generic.ListView):
    model = Donvi
    context_object_name = 'donvis'
    template_name = 'warehouse/Donvi/donvi.html'

# Create


class DonViCreateView(BSModalCreateView):
    template_name = 'warehouse/Donvi/create_donvi.html'
    form_class = DonViModelForm
    success_message = 'Success: Don Vi was created.'
    success_url = reverse_lazy('donvi')

# Update


class DonViUpdateView(BSModalUpdateView):
    model = Donvi
    template_name = 'warehouse/Donvi/update_donvi.html'
    form_class = DonViModelForm
    success_message = 'Success: Don Vi was updated.'
    success_url = reverse_lazy('donvi')

# Read


class DonViReadView(BSModalReadView):
    model = Donvi
    template_name = 'warehouse/Donvi/read_donvi.html'

# Delete


class DonViDeleteView(BSModalDeleteView):
    model = Donvi
    template_name = 'warehouse/Donvi/delete_donvi.html'
    success_message = 'Success: Don Vi was deleted.'
    success_url = reverse_lazy('donvi')


'''
''''''''''''''''''NGUOI BAN
'''


class IndexNguoiBan(generic.ListView):
    model = Nguoiban
    context_object_name = 'nguoibans'
    template_name = 'warehouse/Nguoiban/nguoiban.html'

# Create


class NguoiBanCreateView(BSModalCreateView):
    template_name = 'warehouse/Nguoiban/create_nguoiban.html'
    form_class = NguoiBanModelForm
    success_message = 'Success: Nguoi Ban was created.'
    success_url = reverse_lazy('nguoiban')

# Update


class NguoiBanUpdateView(BSModalUpdateView):
    model = Nguoiban
    template_name = 'warehouse/Nguoiban/update_nguoiban.html'
    form_class = NguoiBanModelForm
    success_message = 'Success: Nguoi Ban was updated.'
    success_url = reverse_lazy('nguoiban')

# Read


class NguoiBanReadView(BSModalReadView):
    model = Nguoiban
    template_name = 'warehouse/Nguoiban/read_nguoiban.html'

# Delete


class NguoiBanDeleteView(BSModalDeleteView):
    model = Nguoiban
    template_name = 'warehouse/Nguoiban/delete_nguoiban.html'
    success_message = 'Success: Nguoi Ban was deleted.'
    success_url = reverse_lazy('nguoiban')


'''
''''''''''''''''''SAN PHAM
'''


class IndexSanPham(generic.ListView):
    model = Sanpham
    context_object_name = 'sanphams'
    template_name = 'warehouse/Sanpham/sanpham.html'

# Create


class SanPhamCreateView(BSModalCreateView):
    template_name = 'warehouse/Sanpham/create_sanpham.html'
    form_class = SanPhamModelForm
    success_message = 'Success: Hang Hoa was created.'
    success_url = reverse_lazy('sanpham')

# Update


class SanPhamUpdateView(BSModalUpdateView):
    model = Sanpham
    template_name = 'warehouse/Sanpham/update_sanpham.html'
    form_class = SanPhamModelForm
    success_message = 'Success: Hang Hoa was updated.'
    success_url = reverse_lazy('sanpham')

# Read


class SanPhamReadView(BSModalReadView):
    model = Sanpham
    template_name = 'warehouse/Sanpham/read_sanpham.html'

# Delete


class SanPhamDeleteView(BSModalDeleteView):
    model = Sanpham
    template_name = 'warehouse/Sanpham/delete_sanpham.html'
    success_message = 'Success: Hang Hoa was deleted.'
    success_url = reverse_lazy('sanpham')


'''
''''''''''''''''''NHAP KHO
'''


class IndexNhapKho(generic.ListView):
    model = NhapKho
    context_object_name = 'nhapkhos'
    template_name = 'warehouse/Nhapkho/nhapkho.html'

# Create


class NhapKhoCreateView(BSModalCreateView):
    template_name = 'warehouse/Nhapkho/create_nhapkho.html'
    form_class = NhapKhoModelForm
    success_message = 'Success: San Pham trong Kho was created.'
    success_url = reverse_lazy('nhapkho')

# Update


class NhapKhoUpdateView(BSModalUpdateView):
    model = NhapKho
    template_name = 'warehouse/Nhapkho/update_nhapkho.html'
    form_class = NhapKhoModelForm
    success_message = 'Success: San Pham trong Kho was updated.'
    success_url = reverse_lazy('nhapkho')

# Read


class NhapKhoReadView(BSModalReadView):
    model = NhapKho
    template_name = 'warehouse/Nhapkho/read_nhapkho.html'

# Delete


class NhapKhoDeleteView(BSModalDeleteView):
    model = NhapKho
    template_name = 'warehouse/Nhapkho/delete_nhapkho.html'
    success_message = 'Success: San Pham trong Kho was deleted.'
    success_url = reverse_lazy('nhapkho')
