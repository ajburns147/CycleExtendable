from chat_extendability import is_cycle_extendable, is_hamiltonian

import time
import datetime

desired_vertex = 11


def startLog(file):
    file.write("---------------------------------\n")
    file.write(f"Time = {datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')}\n")
    file.write("---------------------------------\n")


def endLog(w, start_time, num_graphs):
    completion_time = round(time.time() - start_time, 3)
    print("\n\nEnd Report \n" +
        "-------------------------------"
        "")

    if num_graphs < 100_000:
        end_report = f"Number of graphs = {num_graphs} \n" + \
                     f"Time to complete = {completion_time} sec\n"
    else:
        end_report = f"Number of graphs = {num_graphs} \n" + \
                     f"Time to complete = {convert_time(completion_time)}\n"
    print(end_report)
    print("---------------------------------\n\n\n")
    w.write(end_report)


def convert_time(seconds):
    seconds = round(seconds)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def printReport(start_time, file_length, curr_file_loc):
    percent_complete = round(curr_file_loc * 100 / file_length, 3)
    curr_time = time.time()
    time_so_far = curr_time - start_time
    estimated_total = (time_so_far/(curr_file_loc+1))*file_length
    time_left = round(estimated_total - time_so_far, 3)

    print(
        "\n\nRunning Report \n" +
        "-------------------------------\n" +
        f"Percent Completion = {percent_complete} %\n" +
        f"Time so far = {convert_time(time_so_far)}\n" +
        f"Time remaining = {convert_time(time_left)}"
    )


if __name__ == "__main__":
    start_time = time.time()
    mid_time = time.time()

    filename = "../rawChordal/2022-04-30 Chordal " + str(desired_vertex) + ".txt"
    f = open(filename)
    w = open(f"../Logs/{desired_vertex}vertices", "a")

    startLog(w)

    length = len(f.readlines())
    f.seek(0)
    line = 0

    printReport(start_time, length, line)

    for graph6 in f.readlines():
        # print(graph6)
        line += 1

        rolling_time = time.time() - mid_time

        if rolling_time > 3:
            mid_time = time.time()
            printReport(start_time, length, line)
        t0 = time.time()
        if not is_hamiltonian(graph6.strip("\n")):
            # print(f"{graph6} is not hamiltonian")
            continue

        t1 = time.time()
        if not is_cycle_extendable(graph6.strip("\n")):
            w.write(graph6 +
                    "Not Extendable\n\n"
                    )



    endLog(w, start_time, line)
    f.close()
    w.close()
