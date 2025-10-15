from abc import ABC, abstractmethod

from course.Khoa_Hoc_Base import AKhoaHoc
from course.Nhan_Thuc_KH import NhanThucKH
from course.Phong_Tranh_KH import Phong_Tranh_KH
from course.Tu_Choi_KH import TuChoiKH
# class dùng để tạo các đối tượng khóa
class KhoaHocFactory(ABC):
    @abstractmethod
    def taoKhoaHoc(self)->AKhoaHoc:
        pass
# các lớp con cụ thể cho từng loại khóa học tạo đối tượng khóa học tương ứng
class NhanThucFactory(KhoaHocFactory):
    def taoKhoaHoc(self):
        return NhanThucKH ("NT01","online","Khóa học nhận thức","Khóa học giúp nhận thức về tác hại của ma túy","3 tháng",15)

class PhongTranhFactory(KhoaHocFactory):
    def taoKhoaHoc(self):
        return Phong_Tranh_KH("PT01", "offline", "Khóa học phòng tranh", "Khóa học giúp phòng tránh những nguy cơ về ma túy", "6 tháng", 18)

class TuChoiFactory(KhoaHocFactory):
    def taoKhoaHoc(self):
        return TuChoiKH("TC01", "online", "Khóa học từ chối", "Khóa học giúp học cách từ chối dử dụng chất ma túy", "4 tháng", 14)