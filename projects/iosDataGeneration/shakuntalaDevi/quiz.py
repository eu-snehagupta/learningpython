import os
import csv
from csv import reader

def read_data(file_directory_name):
    data = []
    with open (os.path.join(file_directory_name, "swedish_sign_board.csv"), "r") as f:
        csv_reader = reader(f)
        header = next(csv_reader)
        if header != None:
            for rows in csv_reader:
                data.append("level.append(QuizData(category: \"{}\", image: \"{}\", question: \"{}\", choiceA: \"{}\", choiceB: \"{}\", choiceC: \"{}\", choiceD: \"{}\", answer: {}, solutionimage: \"{}\"))".format(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8]))
    with open (os.path.join(file_directory_name, "swedish_sign_board.txt"), "w") as f:
        for eachitem in data:
            f.write(eachitem + "\n")

file_directory_name = "C://Users//Neha//Desktop//swedish_sign_board//"

read_data(file_directory_name) 
