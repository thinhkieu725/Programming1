"""
COMP.CS.100 Programming 1.
3.8.ParacetamolDosage.py
Creator: Thinh Kieu
Student id number: 152167613
"""

def calculate_dose(weight, time, total_doze_24):
    """
    calculate_dose(weight, time, total_doze_24) function:
    objective: calculate a correct dose of paracetamol for a patient
    :param weight: string _ the weight of the patient
    :param time: time _ the time (in full-hours) from the previous dose
    :param total_doze_24: the accumulative amount of paracetamol the patient has used for the last 24 hours
    :return: int _ the correct dose for the patient
    """
    weight = int(weight)
    time = int(time)
    total_doze_24 = int(total_doze_24)

    if time < 6:
        return 0
    tempRes = weight * 15
    maxDose = 4000 - total_doze_24
    return min(tempRes, maxDose)

def main():
    weight = input("Patient's weight (kg): ")
    time = input("How much time has passed from the previous dose (full hours): ")
    total_doze_24 = input("The total dose for the last 24 hours (mg): ")
    print("The amount of Parasetamol to give to the patient:", calculate_dose(weight, time, total_doze_24))

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)

if __name__ == "__main__":
  main()
