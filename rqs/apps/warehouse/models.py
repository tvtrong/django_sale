from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Donvi(models.Model):
    ten_dv = models.CharField(
        primary_key=True, verbose_name='Tên đơn vị', max_length=100, null=False)

    def __str__(self):
        return self.ten_dv


class Nhan(models.Model):
    ten_nhan = models.CharField(primary_key=True,
                                verbose_name='Tên nhãn', max_length=200, null=False)

    def __str__(self):
        return self.ten_nhan


class Nguoiban(models.Model):
    ten_nb = models.CharField(
        verbose_name='Tên người bán', max_length=100, null=False)
    sdt_nb = PhoneNumberField(primary_key=True, verbose_name='SDT')
    email_nb = models.EmailField(verbose_name='Email', null=True, blank=True)
    dia_chi_nb = models.TextField(
        verbose_name='Địa chỉ', max_length=200, null=True, blank=True)
    ngay_hoptac = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '{}-{}'.format(self.ten_nb, self.sdt_nb)


class Sanpham(models.Model):
    ten_sp = models.CharField(
        primary_key=True, verbose_name='Tên sản phẩm', max_length=200, null=False, default='Yến Sào')
    mo_ta = models.TextField(verbose_name='Mô tả', null=True, blank=True)
    nhan = models.ManyToManyField(Nhan, verbose_name='Nhãn')

    def __str__(self):
        return self.ten_sp


class NhapKho(models.Model):
    san_pham = models.ForeignKey(
        Sanpham, null=True, on_delete=models.SET_NULL, verbose_name='Tên sản phẩm')
    so_luong = models.IntegerField(
        verbose_name='Số lượng', default=1, blank=False, null=False)
    gia_nhap = models.FloatField(
        verbose_name='Giá nhập', null=True, default=19.99)
    don_vi_tinh = models.ManyToManyField(Donvi, verbose_name='Đơn vị tính')
    mua_tu = models.ForeignKey(
        Nguoiban, null=True, on_delete=models.SET_NULL, verbose_name='Mua từ')
    ghi_chu = models.TextField(verbose_name='Ghi chú', null=True)
    ngay_nhap = models.DateTimeField(auto_now_add=True, null=True)
    #thanhtien = models.FloatField(default=0)

    @property
    def get_thanhtien(self):
        return self.so_luong*self.gia_nhap

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.san_pham.ten_sp, self.mua_tu.ten_nb, self.thanh_tien)
