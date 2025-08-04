#pre-conditioned loop

study_hard = True

while study_hard:
    print("Pass test!")
    response = input("Study more?")
    if response == "no":
        study_hard = False
