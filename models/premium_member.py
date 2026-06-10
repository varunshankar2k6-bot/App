#Defing class
class ResumeManager:
    #Creating upload resume function
    def upload_resume(self):
        print("Resume has been successfully uploaded")
#Creating class PremiumFeatures
class PremiumFeatures:
    def premium_support(self):
        print("Premium support has been activated")
#Creating PremiumMember class which injerits from both classes
class PremiumMember(ResumeManager, PremiumFeatures):
    pass