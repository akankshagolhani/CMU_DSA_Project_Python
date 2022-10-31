import os

def take_input():

    people = []
    for i in range(N):
        S1 = file.readline()
        person = []
        for word in S1.split(" "):
            S2 = word
            S2 = int(S2)
            person.append(S2)
        people.append(person)
    people = sorted(people, key=lambda x: x[0])


    min_contribution = float('inf')
    for i in range(len(people)):
        left = 0
        right = 0
        if i > 0:
            left = max(0, people[i - 1][1] - people[i][0])
        if i < len(people) - 1:
            right = max(people[i][1] - people[i + 1][0], 0)
        contribute = max(0, people[i][1] - people[i][0] - left-right)
        min_contribution = min(min_contribution, contribute)
        if min_contribution == 0:
            break


    total = 0
    maximum = 0
    for j in range(len(people)):
        start = people[j][0]
        end = people[j][1]

        if end <= maximum:
            continue
        elif start < maximum:
            total += end - maximum
        elif start >= maximum:
            total += end - start
        maximum = end

    result=total - min_contribution
    return(result)


def file_name():
    output = []
    for i in range(1, 11):
        first_part = r"C:\Users\Akanksha Golhani\PycharmProjects\CMU_DSA_Project"
        file_number = str(i)
        second_part = r".in"
        Path = (first_part + os.sep + file_number + second_part)
        global file
        file = open(Path)
        N1 = file.readline()
        global N
        N = int(N1)
        output.append(take_input())
    return (output)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    output1=[]
    output1 = file_name()
    x = 1
    for i in output1:
        new_file = str(x) + ".out"
        with open(new_file, 'w') as f:
            S3 = str(i)
            f.write(S3)
            x = x + 1