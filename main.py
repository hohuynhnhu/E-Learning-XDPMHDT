from survey.user import User
from report.admin import Admin

if __name__ == "__main__":
    # Test Survey Factory
    user = User(1, "Nguyen Van A")
    user.start_survey("ASSIST")
    user.start_survey("CRAFFT")

    # Test Report Factory
    admin = Admin("Admin", "admin@example.com")
    admin.view_report("survey")
    admin.export_report("appointment", "pdf")
