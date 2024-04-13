################################
# Chime Youden
# ICE
# 02230210
################################
# REFERENCES
# https://chat.openai.com/c/241e5316-0d0f-4f10-b28c-20fd1540c2cb
# http://link.to.an.article/video.com
################################
# SOLUTION
# Your Solution Score:
# 43249
################################

# Read the input.txt file
def read_input(file_input):
    data = []
    with open(file_input, "r") as file:
        for line in file:
            opp_move, desired_outcome = line.split()
            data.append((opp_move, desired_outcome))
    return data

def calculate_score(round_data):
    total_score = 0
    for opp_move, desired_outcome in round_data:

        # Determine your move based on the desired outcome
        if desired_outcome == 'x':
            if opp_move == 'A': 
                total_score += 3  
            elif opp_move == 'B':
                total_score += 1  
            elif opp_move == 'C':
                total_score += 2  
        elif desired_outcome == 'Y': 
            if opp_move == 'A':
                total_score += 4  
            elif opp_move == 'B':
                total_score += 5 
            elif opp_move == 'C':
                total_score += 6  
        elif desired_outcome == 'Z':
            if opp_move == 'A':
                total_score += 8  
            elif opp_move == 'B':
                total_score += 9  
            elif opp_move == 'C':
                 total_score += 7  
    print(f"The total score is : {total_score}")
    # 1 (x:0 , y:3, z:6)
    # 2 (A:1(rock), B:2(paper), C:3(scissor))
    # total score = 1() + 2()

# Other parts of code here to run your functions and printing of the input.
file_input= "CSF101CAP/input_0_cap1.txt"
calculate_score(read_input(file_input))
