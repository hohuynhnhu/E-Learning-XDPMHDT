from abc import ABC, abstractmethod
class AKhoaHoc(ABC):
    # hàm khởi tạo
    def __init__(self,id_Khoahoc: str, hinh_thuc:str, ten_KH:str, mo_ta:str, thoi_luong:str, do_tuoi:int):
        self.id_Khoahoc = id_Khoahoc
        self.hinh_thuc = hinh_thuc
        self.ten_KH = ten_KH
        self.mo_ta = mo_ta
        self.thoi_luong = thoi_luong
        self.do_tuoi = do_tuoi
    @abstractmethod
    def dangKyKH(self,Uid: str):
        pass
    @abstractmethod
    def hienNoiDung(self):
        pass