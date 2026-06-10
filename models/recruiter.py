from models.user import User

class Recruiter(User):

    def __init__(self, name, email, company_name):
        super().__init__(name, email)
        self.company_name = company_name

    def post_job(self, job_title):
        print(self.company_name, "posted as", job_title)

    # overriding parent method from the parent class
    def display_details(self):
        super().display_details()
        print("Company:", self.company_name)