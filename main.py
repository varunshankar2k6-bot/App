# Qn2: Create a JobSeeker object and apply for a job
from models.job_seeker import JobSeeker
from models.user import User
js = JobSeeker(
    "Varun",
    "varun@gmail.com",
    ["Python","Java"]
)
# Display details inherited from User class
js.display_details()
# Apply for a job
js.apply_job("Software Engineer")
# Display total number of users created
print("Total users:", User.get_total_users())

# Qn3: Create a Recruiter object and post a job
from models.recruiter import Recruiter
r = Recruiter(
    "A",
    "a@gmail.com",
    "Xminds"
)
# Display recruiter details
r.display_details()
# Post a new job
r.post_job("Data Analyst")

# Qn4: Create a Premium Job Seeker object
from models.premium_job_seeker import PremiumJobSeeker
pjs = PremiumJobSeeker(
    "Arun",
    "arun@gmail.com",
    ["Python", "C++"],
    "Gold"
)
# Use premium feature
pjs.priority_apply()
# Apply for a job
pjs.apply_job("Software Engineer")

# Qn5: Demonstrate multiple inheritance
from models.premium_member import PremiumMember
#Object
pm = PremiumMember()
# Upload resume feature from ResumeManager class
pm.upload_resume()
# Premium support feature from PremiumFeatures class
pm.premium_support()

#Qn 6 Demonstrating run time polymorphism
from notification.notification import (
    EmailNotification,
    SMSNotification,
    WhatsAppNotification
)
notifications = [
    EmailNotification(),
    SMSNotification(),
    WhatsAppNotification()]
for i in notifications:
    i.send()

#Qn 7 Overloading
from models.job_application import JobApplication
#Defining objects
ja1 = JobApplication("John", 5)
ja2 = JobApplication("Sara", 3)
if ja1 > ja2:
    print(ja1.applicant_name, "has more experience")
else:
    print(ja2.applicant_name, "has more experience")

#Qn 8:Exception handling
from models.job_seeker import JobSeeker
from utils.exceptions import JobPortalException
#Exception using try except and finally
try:
    js = JobSeeker(
        "Var",
        "vargmail.com",
        ["Python", "Java"]
    )
except JobPortalException as e:
    print("Error:", e)
finally:
    print("Program runs successfully")

#Question 10 Singleton pattern
from patterns.database import Database
db1 = Database()
db2 = Database()
#Checking if both objects are same
print(db1 == db2)

#Question 11 Factory Pattern
from patterns.user_factory import UserFactory
u1 = UserFactory.create_user(
    "jobseeker",
    "Varun",
    "varun@gmail.com",
    ["Python", "Java"]
)
u1.display_details()


#Question 12 Strategic Pattern
from patterns.search_strategy import SkillSearch, LocationSearch, SalarySearch, JobSearch
s1 = JobSearch(SkillSearch())
s1.execute_search()
s2 = JobSearch(LocationSearch())
s2.execute_search()
s3 = JobSearch(SalarySearch())
s3.execute_search()