from apps.warehouse.models import NhapKho, Nguoiban, Sanpham, Donvi, Nhan
from bootstrap_modal_forms.forms import BSModalModelForm


class NhapKhoModelForm(BSModalModelForm):
    class Meta:
        model = NhapKho
        fields = ('san_pham', 'so_luong', 'gia_nhap',
                  'don_vi_tinh', 'mua_tu', 'ghi_chu')


class SanPhamModelForm(BSModalModelForm):
    class Meta:
        model = Sanpham
        fields = '__all__'


class NguoiBanModelForm(BSModalModelForm):
    class Meta:
        model = Nguoiban
        fields = '__all__'


class DonViModelForm(BSModalModelForm):
    class Meta:
        model = Donvi
        fields = '__all__'


class NhanModelForm(BSModalModelForm):
    class Meta:
        model = Nhan
        fields = '__all__'
