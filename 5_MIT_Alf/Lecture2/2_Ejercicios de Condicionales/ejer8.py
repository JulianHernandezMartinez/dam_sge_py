evaluation = input("Evaluation ? :")
if (evaluation == "0.0") | (evaluation == "0.2") | (evaluation =="0.4") | (float(evaluation)>=0.6):
    print(f'your reward is {float(evaluation)*2400} €')
else:
    print("wrong evaluation input")
