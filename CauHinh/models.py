from django.db import models

from CauHinh import migrations

Default_title = 'Sim số đẹp - Thương hiệu sim số uy tín nhất việt nam'
Default_key = 'Mua sim ,bán sim , Sim số đẹp, sim tứ quý ,sim năm sinh'
Default_des = 'Sim số đẹp - Thương hiệu uy tín trong ngành sim số đẹp từ hơn 10 năm qua, giao sim Miễn phí,dịch vụ tốt nhất thị trường'
Default_fav= '/favico.png'

Default_robot = {
    ('index,follow' , 'Lập chỉ mục trang web (index,follow)'),
    ('noindex,nofollow' , 'Chặn google lập chỉ mục trang web :(noindex,nofollow)')
}

# Create your models herec
class CauHinhSeo(models.Model):
    title = models.CharField(max_length=200,default=Default_title,verbose_name='Tiêu đề website')
    keyword = models.CharField(max_length=300,default=Default_key,verbose_name='Từ khóa website',help_text='Từ khóa được phân cách bằng dầu phẩy')
    des = models.TextField(max_length=300,default=Default_des,verbose_name='Mô tả website')
    favico = models.ImageField(null=True,default=Default_fav,verbose_name='Favico')
    google = models.CharField(max_length=100,blank='',default='Mã google site',verbose_name='Google-Webmaster')
    fb_app = models.CharField(max_length=100,blank='',default='123456767890',verbose_name='Facebook app id')
    robots = models.CharField(max_length=100,choices=Default_robot,verbose_name='Robots' ,help_text='Tùy chỉnh lập chỉ mục trang web với google',default='index,follow')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Cấu Hình SEO'



Default_titles = 'Sim số đẹp - Thương hiệu sim số uy tín nhất việt nam'
zalo_d = '0969641652'
Default_sdt1 = '0969641652'
Default_sdt2 = '0345003654'
Default_banner= '/logo_banner.png'
Default_footer= '<p><strong>&copy;Sim HUTECH - Hệ thống phân phối <a href="/">Sim số đẹp</a> lớn nhất Việt Nam! <div></strong></br><a href="http://online.gov.vn/HomePage/CustomWebsiteDisplay.aspx?DocId=3849"><img alt="Sim thăng long đã đăng ký với bộ công thương" src="https://static.simthanglong.vn/images/bct.jpg" style="width: 215px;"></a>'
mess ='1317836384978667'



# Create your models herec
class CauHinhTrang(models.Model):
    title = models.CharField(max_length=200,default=Default_titles,verbose_name='Tiêu đề website')
    sdt1 = models.CharField(max_length=300,default=Default_sdt1,verbose_name='Số điện thoại 1')
    sdt2 = models.CharField(max_length=300, default=Default_sdt2, verbose_name='Số điện thoại 2')
    banner = models.ImageField(null=True,default=Default_banner,verbose_name='Banner đầu trang')
    zalo = models.CharField(max_length=300, default=zalo_d, verbose_name='Nhập số zalo')
    chatfb = models.CharField(max_length=300,default=mess, verbose_name='Nhập id page facebook')
    footer = models.TextField(max_length=1000, default=Default_footer, verbose_name='Thêm nội dung chân trang')


    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Cấu Hình Trang'

