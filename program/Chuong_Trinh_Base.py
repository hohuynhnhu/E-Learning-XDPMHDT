from abc import ABC, abstractmethod
# self có nghĩa là thuộc tính của lớp hiện tại
class AChuongTrinh(ABC):
    def __init__(self, id_ct: str, ten_ct: str,noi_dung: str, thoi_gian: str, dia_diem: str, doi_tuong: str):
        self.id_ct = id_ct
        self.ten_ct = ten_ct
        self.noi_dung = noi_dung
        self.thoi_gian = thoi_gian
        self.dia_diem = dia_diem
        self.doi_tuong = doi_tuong
    @abstractmethod
    def hienThongTin(self):
        pass
    @abstractmethod
    def thamGiaCT(self,Uid: str):
        pass
