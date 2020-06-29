from django.db import models
from PythonWeb.utils import get_unique_slug

thang_c = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
)

nam_c = (
    ('1950', '1950'),

    ('1951', '1951'),

    ('1952', '1952'),

    ('1953', '1953'),

    ('1954', '1954'),

    ('1955', '1955'),

    ('1956', '1956'),

    ('1957', '1957'),

    ('1958', '1958'),

    ('1959', '1959'),

    ('1960', '1960'),

    ('1961', '1961'),

    ('1962', '1962'),

    ('1963', '1963'),

    ('1964', '1964'),

    ('1965', '1965'),

    ('1966', '1966'),

    ('1967', '1967'),

    ('1968', '1968'),

    ('1969', '1969'),

    ('1970', '1970'),

    ('1971', '1971'),

    ('1972', '1972'),

    ('1973', '1973'),

    ('1974', '1974'),

    ('1975', '1975'),

    ('1976', '1976'),

    ('1977', '1977'),

    ('1978', '1978'),

    ('1979', '1979'),

    ('1980', '1980'),

    ('1981', '1981'),

    ('1982', '1982'),

    ('1983', '1983'),

    ('1984', '1984'),

    ('1985', '1985'),

    ('1986', '1986'),

    ('1987', '1987'),

    ('1988', '1988'),

    ('1989', '1989'),

    ('1990', '1990'),

    ('1991', '1991'),

    ('1992', '1992'),

    ('1993', '1993'),

    ('1994', '1994'),

    ('1995', '1995'),

    ('1996', '1996'),

    ('1997', '1997'),

    ('1998', '1998'),

    ('1999', '1999'),

    ('2000', '2000'),

    ('2001', '2001'),

    ('2002', '2002'),

    ('2003', '2003'),

    ('2004', '2004'),

    ('2005', '2005'),

    ('2006', '2006'),

    ('2007', '2007'),

    ('2008', '2008'),

    ('2009', '2009'),

    ('2010', '2010'),

    ('2011', '2011'),

    ('2012', '2012'),

    ('2013', '2013'),

    ('2014', '2014'),

    ('2015', '2015'),

    ('2016', '2016'),

    ('2017', '2017'),

    ('2018', '2018'),

    ('2019', '2019'),

)
ngay_c =(
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
)
menh_c = [
    ('1950', 'Hoả   '),
    ('1951', 'Mộc   '),
    ('1952', 'Mộc   '),
    ('1953', 'Thuỷ  '),
    ('1954', 'Thuỷ  '),
    ('1955', 'Kim   '),
    ('1956', 'Kim   '),
    ('1957', 'Hoả   '),
    ('1958', 'Hoả   '),
    ('1959', 'Mộc   '),
    ('1960', 'Mộc   '),
    ('1961', 'Thổ   '),
    ('1962', 'Thổ   '),
    ('1963', 'Kim   '),
    ('1964', 'Kim   '),
    ('1965', 'Thuỷ  '),
    ('1966', 'Thuỷ  '),
    ('1967', 'Mộc   '),
    ('1968', 'Mộc   '),
    ('1969', 'Hoả   '),
    ('1970', 'Hoả   '),
    ('1971', 'Thổ   '),
    ('1972', 'Thổ   '),
    ('1973', 'Kim   '),
    ('1974', 'Kim   '),
    ('1975', 'Thuỷ  '),
    ('1976', 'Thuỷ  '),
    ('1977', 'Mộc   '),
    ('1978', 'Mộc   '),
    ('1979', 'Hoả   '),
    ('1980', 'Hoả   '),
    ('1981', 'Mộc   '),
    ('1982', 'Thuỷ  '),
    ('1983', 'Thuỷ  '),
    ('1984', 'Kim   '),
    ('1985', 'Kim   '),
    ('1986', 'Hoả   '),
    ('1987', 'Hoả   '),
    ('1988', 'Mộc   '),
    ('1989', 'Mộc   '),
    ('1990', 'Thổ   '),
    ('1991', 'Thổ   '),
    ('1992', 'Thuỷ  '),
    ('1993', 'Thuỷ  '),
    ('1994', 'Hoả   '),
    ('1995', 'Hoả   '),
    ('1996', 'Thuỷ  '),
    ('1997', 'Kim   '),
    ('1998', 'Thổ   '),
    ('1999', 'Thổ   '),
    ('2000', 'Kim   '),
    ('2001', 'Hoả   '),
    ('2002', 'Hoả   '),
    ('2003', 'Mộc   '),
    ('2004', 'Mộc   '),
    ('2005', 'Kim   '),
    ('2006', 'Kim   '),
    ('2007', 'Thổ   '),
    ('2008', 'Thổ   '),
    ('2009', 'Hoả   '),
    ('2010', 'Hoả   '),
    ('2011', 'Mộc   '),
    ('2012', 'Mộc   '),
    ('2013', 'Thuỷ  '),
    ('2014', 'Thuỷ  '),
    ('2015', 'Kim   '),
    ('2016', 'Kim   '),
    ('2017', 'Hoả   '),
    ('2018', 'Hoả   '),
    ('2019', 'Mộc   '),
    ('2020', 'Mộc   '),

]
nguhanh_c =(
    ('Kim', 'Kim'),('Mộc', 'Mộc'),('Thuỷ', 'Thuỷ'),('Hoả', 'Hoả'),('Thổ', 'Thổ'),
)
tuongsinh_c=(
    ('Kim', 'Thuỷ'),('Mộc', 'Hoả'),('Hoả', 'Thổ'),('Thổ', 'Kim'),('Thuỷ', 'Mộc'),
)
tuongkhac_c=(
    ('Kim', 'Hoả'),('Mộc', 'Thổ'),('Hoả', 'Kim'),('Thổ', 'Thuỷ'),('Thuỷ', 'Hoả'),
)


class Datapt(models.Model):
    hoten = models.CharField(max_length=100,verbose_name='Họ tên')
    ngay = models.CharField(max_length=100, choices=ngay_c, default='0', verbose_name='Ngày sinh')
    thang = models.CharField(max_length=100, choices=thang_c,default='0',verbose_name='Tháng sinh')
    nam = models.CharField(max_length=100, choices=nam_c,default='0',verbose_name='Năm sinh')
    menh = models.CharField(max_length=100,choices=menh_c,default='',verbose_name='Mệnh')
    nguhanh = models.CharField(max_length=100,choices=nguhanh_c,verbose_name='Ngũ hành')
    tuongsinh = models.CharField(max_length=100,choices=tuongsinh_c,verbose_name="Tương sinh")
    tuongkhac = models.CharField(max_length=100,choices=tuongkhac_c,verbose_name="Tương khắc")

    class Meta:
        verbose_name_plural = 'Data phong thuỷ'


class nguhanh(models.Model):
    name = models.CharField(max_length=100,verbose_name='Tên ngũ hành',unique=True)
    tuongsinh = models.CharField(max_length=100,verbose_name='Tương sinh')
    tuongkhac = models.CharField(max_length=100,verbose_name='Tương khắc')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Ngũ hành'

class namsinh(models.Model):
    namsinh = models.CharField( max_length=5,verbose_name='Năm sinh',unique=True)
    nguhanh_ns = models.ForeignKey(nguhanh,null=False,on_delete=models.CASCADE,verbose_name='Thuộc mệnh')
 
    def __str__(self):
        return self.namsinh
    class Meta:
        verbose_name_plural = 'Năm sinh'