"""
COMP.CS.100 Programming 1.
1.3.IndexRaisesToStudyBenefits.py
Creator: Thinh Kieu
Student id number: 152167613
"""

studentBenefits =input("Enter the amount of the study benefits: ")
sb = float(studentBenefits)
raise1 = sb * 1.0117
raise2 = raise1 * 1.0117

print("If the index raise is 1.17 percent, the study benefit,\nafter a raise, would be", raise1, "euros")
print("and if there was another index raise, the study\nbenefits would be as much as", raise2, "euros")