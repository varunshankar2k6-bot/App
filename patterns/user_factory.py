#QUestion 11 Factory Pattern
#Inheriting from other classes
from models.job_seeker import JobSeeker
from models.recruiter import Recruiter
from utils.exceptions import JobPortalException
class UserFactory:
    #Static method for factory
    @staticmethod
    def create_user(user_type, name, email, extra):
        if user_type == "jobseeker":
            return JobSeeker(name, email, extra)
        elif user_type == "recruiter":
            return Recruiter(name, email, extra)
        else:
            raise JobPortalException("Invalid user type")