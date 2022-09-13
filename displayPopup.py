# Life systems through the quiz.o
life_Total = 3
life_Total_L1 = 2
life_Total_FinalLife = 1
Life_Total_ExitGame = 0

# Question 1.
Q1 = input("What is a nanoparticle? \n 3: An incredibly small particle, that is part of the micrometre spectrum. \n 8: An incredibly small particle, that is part of the quark-size spectrum. \n @: An incredibly small particle, that is part of the nanometre spectrum. \n (): An incredibly small particle, that is part of the millimetre spectrum. \n Answer: ")

if Q1 != "@":
    print("You have failed this question; you lose a life!")
    print(life_Total_L1)
    print("You have two more lives for the remainder of the quiz; good luck!")
elif Q1 == "@":
    print("You have got the question right; congrats!")



# Question 2.
Q2 = input("What is nanobiotechnology? \n KAI: The process of using artifical intelligence on playing games by itself. \n one: The process of using technology designed for the small stuff (nano), and for altering organisms. \n PHI: Using technology for biological purposes. \n *: Biotechnology is a game. L, this is the RIGHT answer (This is Iron Man; it MUST be the right answer). \n Answer: ")
Q2_Right = "one"

if Q1 == "@":
    if Q2 != "one":
            print(life_Total - 1)
            print("You lost a life.")
if Q1 !=  "@":
    if Q2 != "one":
        print(life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        print(life_Total_L1, ": Your lives left.")
        print("You got this question right...")
elif Q2 == "one":
    print("You got this question right; you progress for now...")



# Question 3.
Q3 = input("What molecules does nanobiotechnology combine with to make the medicine's ability better? \n @: The types of nanoparticles/molecules that are used in nanobiotechnology are: organic, inorganic, and composite nanoparticles. \n &: The types of nanoparticles that are used in nanobiotech are: incomposite, fermions, and higgs. \n ^: The three types of nanoparticles/molecules are: bosons, quarks, and gluons. \n +: The three types of nanoparticles are: arc-reactor, qubit, and the gluon. \n Answer: ")

if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            print(life_Total_L1)
            print("You lost a life.")
if Q1 == "@":
    if Q2 != "one":
        if Q3 != "@":
            print(life_Total_FinalLife)
            print("You lost a life.")
if Q1 != "@":
    if Q2 == "one":
        if Q3 != "@":
            print(life_Total_FinalLife)
            print("You lost a life.")

if Q1 != "@":
    if Q2 != "one":
        if Q3 == "@":
            print("You got this question right, but you still have ", life_Total_L1, " lives left.")
if Q1 != "@":
    if Q2 != "one":
        if Q3 != "@":
            print(Life_Total_ExitGame)
            print("You lose the quiz; try again!")
            exit()
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            print("You got this question right with two lives remaining still!")
elif Q3 == "@":
    print("You have got the question right; you progress now!")




# Question 4.
Q4 = input("How can nanobiotechnology be used in medicine? \n DELTA: Implement medicine to destroy one's health for the worse. \n SIGMA: Create atoms with scattering-models. \n ALPHA: Create the really small stuff. \n BETA: Make medicine to improve personal-health, and to be used personally without diagnostics.")

