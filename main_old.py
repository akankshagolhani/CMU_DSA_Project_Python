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
def max_cov(i):
    input_list = i.split('\n')
    count = int(input_list[0])
    last = count + 1
    info = map(lambda x: x.split(' '), input_list[1:last])

    # Create a schedule table
    guard_schedule = {}
    for guard_id, guard_info in enumerate(info):
        [start, end] = [int(guard_info[0]), int(guard_info[1])]
        if not guard_schedule.get(start):
            guard_schedule[start] = {'start': [], 'end': []}
        if not guard_schedule.get(end):
            guard_schedule[end] = {'start': [], 'end': []}
        guard_schedule[start]['start'].append(guard_id)
        guard_schedule[end]['end'].append(guard_id)

    sortedschedule = dict(sorted(guard_schedule.items()))

 # Iterate through the schedule table to find coverage time
    previous_shift = {}
    on_duty = 0
    alone= {}
    for time, schedule in sortedschedule.items():
        if len(previous_shift) >= 1:
            previous_shift = time - previous_time
            on_duty += previous_shift
            if len(previous_shift) == 1:
                guard_id = next(iter(previous_shift))
                if not alone.get(guard_id):
                    alone[guard_id] = previous_shift
                else:
                    alone[guard_id] += previous_shift

        for guard_id in schedule['start']:
            previous_shift[guard_id] = True

        for guard_id in schedule['end']:
            del previous_shift[guard_id]

        previous_time = time

# Get minimum alone time
    if (len(alone)) < count:
        min_alone_time = 0 # When there's more than 1 guard to choose to be fired
    else:
        min_alone_time = min(alone.values())

    # Return maximum coverage time when fire 1 guard that has minimum alone time
    return on_duty- min_alone_time


def run():
    CURR_DIR = os.path.dirname(os.path.abspath(_file_))
    INPUT_DIR = os.path.join(CURR_DIR, 'Input')
    OUTPUT_DIR = os.path.join(CURR_DIR, 'Output')
    for file_name in sorted(os.listdir(INPUT_DIR)):
        data = open(os.path.join(INPUT_DIR, file_name), 'r').read()
        output = str(max_cov(data))
        with open(os.path.join(OUTPUT_DIR, file_name.replace('in','out')), 'w') as o:
            o.write(output)

run()


def file_name():
    output= []
    for i in range(1, 11):
        first_part = r"C:\Users\HP\PycharmProjects\CMU_DSA_Project_Python"
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
    x = 1
    for i in output1:
        new_file = str(x) + ".out"
        with open(new_file, 'w') as f:
            S3 = str(i)
            f.write(S3)
            x = x + 1
    print(output1)