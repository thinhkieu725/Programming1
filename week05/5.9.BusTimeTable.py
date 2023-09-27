"""
COMP.CS.100 Programming 1
5.9.BusTimeTable.py
Creator: Thinh Kieu
Student number: 152167613
"""

def main():
    listBusTime = [630, 1015, 1415, 1620, 1720, 2000]
    time = input("Enter the time (as an integer): ")
    time = int(time)
    check = False
    print("The next buses leave:")
    for i in range(len(listBusTime)):
        if listBusTime[i] >= time:
            print(listBusTime[i % len(listBusTime)])
            print(listBusTime[(i+1) % len(listBusTime)])
            print(listBusTime[(i+2) % len(listBusTime)])
            check = True
            break
    if check == False:
        print(listBusTime[0])
        print(listBusTime[1])
        print(listBusTime[2])

if __name__ == "__main__":
    main()
