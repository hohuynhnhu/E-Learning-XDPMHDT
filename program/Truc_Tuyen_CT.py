from program.Chuong_Trinh_Base import AChuongTrinh
class TrucTuyenCT(AChuongTrinh):
    def __init__(self, id_ct: str, ten_ct: str,noi_dung: str, thoi_gian: str, dia_diem: str, doi_tuong: str):
        super().__init__(id_ct, ten_ct,noi_dung, thoi_gian, dia_diem, doi_tuong)
    def hienThongTin(self):
        tt= f"Chương trình: {self.ten_ct}\n Nội dung: {self.noi_dung}\n Thời gian: {self.thoi_gian}\n Địa điểm: {self.dia_diem}\n Đối tượng: {self.doi_tuong}"
        print (tt)
    def thamGiaCT(self, Uid: str):
        kq= f"Học viên {Uid}\n Tham gia chương trình học đường thành công"
        print (kq)