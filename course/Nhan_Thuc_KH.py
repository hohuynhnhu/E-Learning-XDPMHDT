from course.Khoa_Hoc_Base import AKhoaHoc


class NhanThucKH(AKhoaHoc):
    def __init__(self, id_Khoahoc: str, hinh_thuc: str, ten_KH: str, mo_ta: str, thoi_luong: str, do_tuoi: int):
        super().__init__(id_Khoahoc, hinh_thuc, ten_KH, mo_ta, thoi_luong, do_tuoi)
    def dangKyKH(self, Uid: str):
        kq= f"Học viên {Uid}\n Đăng ký khóa học nhận thức thành công"
        print (kq)
    def hienNoiDung(self):
        nd= f"Khóa học: {self.ten_KH}\n Hình thức Mô tả: {self.mo_ta}\n Thời lượng: {self.thoi_luong}\n Độ tuổi: {self.do_tuoi}+"
        print (nd)
