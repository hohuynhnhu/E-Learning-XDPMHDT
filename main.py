from survey.user import User
from report.admin import Admin
from course.Khoa_Hoc_Factory import NhanThucFactory, PhongTranhFactory, TuChoiFactory
from program.Chuong_Trinh_Factory import HocDuongFactory, TrucTuyenFactory
if __name__ == "__main__":
    # Test Survey Factory
    user = User(1, "Nguyen Van A")
    user.start_survey("ASSIST")
    user.start_survey("CRAFFT")

    # Test Report Factory
    admin = Admin("Admin", "admin@example.com")
    admin.view_report("survey")
    admin.export_report("appointment", "pdf")

    # Test Course Factory
    kh= NhanThucFactory()
    khoaHoc1= kh.taoKhoaHoc()
    khoaHoc1.hienNoiDung()
    khoaHoc1.dangKyKH("HV001")

    kh2= PhongTranhFactory()
    khoaHoc2= kh2.taoKhoaHoc()  
    khoaHoc2.hienNoiDung()
    khoaHoc2.dangKyKH("HV002")

    kh3= TuChoiFactory()
    khoaHoc3= kh3.taoKhoaHoc()
    khoaHoc3.hienNoiDung()
    khoaHoc3.dangKyKH("HV003")
    
    # Test Program Factory
    ct= HocDuongFactory()
    chuongTrinh1= ct.taoChuongTrinh()   
    chuongTrinh1.hienThongTin()
    chuongTrinh1.thamGiaCT("HV004")
    
    ct2= TrucTuyenFactory()
    chuongTrinh2= ct2.taoChuongTrinh()
    chuongTrinh2.hienThongTin()
    chuongTrinh2.thamGiaCT("HV005")
