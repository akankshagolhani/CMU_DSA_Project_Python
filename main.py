import os

def Take_Input():
    Hours = []
    Guards = []
    for i in range(N):
        S1 = file.readline()
        for word in S1.split(" "):
            S2 = word
            S2 = int(S2)
            Hours.append(S2)

    for i in range(0, (len(Hours)-2), 2):
        if Hours[i] == Hours[i + 2]:
            if Hours[i + 1] > Hours[i + 3]:
                Time = Hours[i + 1] - Hours[i]
                Guards.append(Time)
            else:
                Time = Hours[i + 3] - Hours[i]
                Guards.append(Time)
        else:
            Time = Hours[i + 1] - Hours[i]
            Guards.append(Time)

    total = 0
    for val in Guards:
        total = total + val

    return (total)

def file_name():
    output= []
    for i in range(1, 11):
        first_part = r"C:\Users\HP\PycharmProjects\pythonProject1"
        file_number = str(i)
        second_part = r".in"
        Path = (first_part + os.sep + file_number + second_part)
        global file
        file = open(Path)
        N1 = file.readline()
        global N
        N = int(N1)
        output.append(Take_Input())
    return (output)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    output1=[]
    output1 = file_name()
    print(output1)
