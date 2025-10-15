from abc import ABC, abstractmethod

from program.Chuong_Trinh_Base import AChuongTrinh
from program.Truc_Tuyen_CT import TrucTuyenCT
from program.Hoc_Duong_CT import HocDuongCT
class KhoaHocFactory(ABC):
    @abstractmethod
    def taoChuongTrinh(self)->AChuongTrinh:
        pass

class HocDuongFactory(KhoaHocFactory):
    def taoChuongTrinh(self):
        return HocDuongCT("HD01", "Chương trình học đường", "Chương trình giúp học sinh nhận thức về tác hại của ma túy", "5 tháng", "Trường học", "Học sinh Trung học")

class TrucTuyenFactory(KhoaHocFactory):
    def taoChuongTrinh(self):
        return TrucTuyenCT("TT01", "Chương trình trực tuyến", "Chương trình giúp học sinh nhận thức về tác hại của ma túy", "3 tháng", "Trực tuyến", "Học sinh tiểu học")
