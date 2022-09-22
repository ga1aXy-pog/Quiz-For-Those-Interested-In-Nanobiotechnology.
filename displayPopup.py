# Life systems through the quiz.
life_Total = 3
life_Total_L1 = 2
life_Total_FinalLife = 1
Life_Total_ExitGame = 0

# Imports.
from PIL import Image

# Top rules.
print("---------Hello Trapped People!----------")
print("The rules: \n 1: You have three lives through the whole escape box. \n 2: If you lose all three lives, the display pop-up will exit. \n 3: There are some questions you might need to research (some of the question answers might not be on the fact sheet). \n 4: If you lose all three lives, you need to restart the whole quiz (type displayPopup after clicking the Windows sign on the computer). \n 5: At the end of the quiz, you will be asked to type in a code. This code can be found by taking in all the symbols (correct answers) and typing the resultant code to escape! \n 6: The answer to the question is the symbol given at the start of the options. \n 7: For some questions, you might be asked to watch a clip to answer the question. Copy the link address and enter it in the Chrome Tab open.")

# Question 1.
print("\n")
print("----------------------------------------------------------------------------------------")
Q1 = input("What is a nanoparticle? \n 3: An incredibly small particle, that is part of the micrometre spectrum. \n 8: An incredibly small particle, that is part of the quark-size spectrum. \n @: An incredibly small particle, that is part of the nanometre spectrum. \n (): An incredibly small particle, that is part of the millimetre spectrum. \n Answer: ")

if Q1 != "@":
    print("You have failed this question; you lose a life!")
    print(life_Total_L1)
    print("You have two more lives for the remainder of the quiz; good luck!")
elif Q1 == "@":
    print("You have got the question right; congrats!")

print("\n")

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

print("\n")

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
if Q3 == "@":
    print("You have got the question right; you progress now!")


print("\n")

# Question 4.
Q4 = input("How can nanobiotechnology be used in medicine? \n DELTA: Implement medicine to destroy one's health for the worse. \n SIGMA: Create atoms with scattering-models. \n ALPHA: Create the really small stuff. \n BETA: Make medicine to improve personal-health, and to be used personally without diagnostics. \n Answer: ")


if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                print(life_Total_L1)
                print("You lost your first life from the questions.")
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 != "BETA":
                print(life_Total_FinalLife)
                print("You lost another life.")
if Q1 == "@":
    if Q2 != "one":
        if Q3 != "@":
            if Q4 != "BETA":
                print(Life_Total_ExitGame, ": no life.")
                exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                print("You still have not lost a life. Good job!")

# Repition.
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                print(life_Total_L1)
                print("You lost your first life from the questions.")
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                print(life_Total_L1)
                print("You lost your first life from the questions.")
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                print(life_Total_L1)
                print("You lost your first life from the questions.")


if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                print(life_Total_FinalLife)
                print("You lost another life.")
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                print(life_Total_FinalLife)
                print("You lost another life.")
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 != "BETA":
                print(life_Total_FinalLife)
                print("You lost another life.")


if Q1 != "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 != "BETA":
                print(Life_Total_ExitGame, ": no life.")
                exit()
if Q1 != "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 != "BETA":
                print(Life_Total_ExitGame, ": no life.")
                exit()


print("\n")


# Question 5.
Q5 = input("What 'things' make up nanoparticles? \n nine: Nanoparticles are made up of picoatoms, which allow it to have three types (organic, inorganic, and composite). \n KAI: Nanoparticles are made up of macroatoms, which allows it to create three different nanoparticles: organic, inorganic, and composite. \n Triton: Nanoparticles are made up of microatoms, which allows it to create three possible of nanoparticles (organic, inorganic, and composite). \n Answer: ")

if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    print("You have gotten this question right, and all the other questions as well. Good job.", life_Total)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    print("You got this question wrong. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 != "nine":
                    print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 != "BETA":
                if Q5 != "nine":
                    exit()

# Repitions.
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    print("You got this question right. ", life_Total_L1)


if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    print("You got this question wrong. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    print("You got this question wrong. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    print("You got this question right. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    print("You got this question right. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    print("You got this question right. ", life_Total_FinalLife)
                    
if Q1 == "@":
    if Q2 != "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    print("You got this question right. ", life_Total_FinalLife)

if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    print("You got this question right. ", life_Total_FinalLife)


if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 != "nine":
                    exit()
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 != "nine":
                    exit()
if Q1 != "@":
    if Q2 != "one":
        if Q3 != "@":
            exit()


print("\n")

# Question 6.
Q6 = input("Identify the processes used to alter organisms in medicine and agriculture. \n δ: Harming all the cells of the organs. \n Sigma: Finding the cells of the body that harm the body; spreading these infections further through the organism; adding in nice genes that treat this issue; continue the process until completed. \n β: Finding the genes in DNA pieces; finding the cells that are harming health, and alter them; change the cell by adding in particles that damage harmful cells; add in the new gene; continue this process until completed. \n Answer: ")

if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        print("You have gotten this question right, and all the other questions as well. Good job.", life_Total)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        print("You got this question wrong. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 != "β":
                        print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 != "nine":
                    if Q6 != "β":
                        exit()


# Repition sequence.
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        print("You got this question right. ", life_Total_L1)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        print("You got this question right: ", life_Total_L1)

if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        print("You got this question wrong. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        print("You got this question wrong. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        print("You got this question right. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        print("You got this question right. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        print("You got this question right. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 != "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 != "nine":
                    if Q6 != "β":
                        exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 != "β":
                        exit()
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 != "β":
                        exit()
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 != "β":
                        exit()

print("\n")

# Question 7.
print("https://www.youtube.com/watch?v=tYeu2fG87T4&t=297s. Use this clip to answer the question.")
Q7 = input("Explain how changing enzymes of a body can affect selective breeding in agricultural processes? \n Integral: The alteration of enzymes for organisms in agriculture produces livestock and crops that are not morally right, and organisms that are not healthy. \n Σ: The alteration of a certain gene for an organism, and then allowing that organism to mate. Only the best of the best are selected to be alive. \n DX: Agriculture is morally right, but adding in biotechnology makes it SO GOOD. It only allows the best of the best to be continued through the life-time. \n Answer: ")

if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You have gotten this question right, and all the other questions as well. Good job.", life_Total)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            print("You got this question wrong. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 != "Σ":
                            print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 != "β":
                        if Q7 != "Σ":
                            exit()

# Repition sequences.
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_L1)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_L1)

if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            print("You got this question wrong. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            print("You got this question wrong. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 != "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 == "Σ":
                            print("You got this question right. ", life_Total_FinalLife)

if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 != "Σ":
                            exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 != "Σ":
                            exit()
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 != "Σ":
                            exit()
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 != "Σ":
                            exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            exit()
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            exit()
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            exit()

print("\n")

# Question 8.
Q8 = input("How has nanobiotechnology been used for personal reasons? \n Reggae: For the use of micromedicine to worsen one's health. \n B: For the commercial use of nanomedicine to worsen one's health. \n Φ: For the commercial use of nanomedicine to improve one's health. \n Answer: ")

if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                print("You have gotten this question right, and all the other questions as well. Good job.", life_Total)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                print("You got this question wrong. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 != "Φ":
                                print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 != "Σ":
                            if Q8 != "Φ":
                                exit()

# Repitions for Q8.
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 == "Φ":
                                print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                print("You got this question right. ", life_Total_L1)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                print("You got this question right. ", life_Total_L1)

if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                print("You got this question wrong. ", life_Total_FinalLife)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                print("You got this question wrong. ", life_Total_FinalLife)

if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 != "Φ":
                                exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 != "Φ":
                                exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 != "Φ":
                                exit()
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 != "Φ":
                                exit()
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 != "Φ":
                                exit()


print("\n")

# Question 9
Q9 = input("Identify the nanoparticles implemented in nanomedicine. \n Δ: Micelles, Dendrimers, Liposomes, Polymers, Carbon nanotubes, Gold, Mesoporous silica, Iron oxide, Core-shell, composite. \n PI: Micelles, Denrimers, organic, inorganic, composite, gold. \n TRITON: Micelles, Dendrimers, Liposomes, Polymers, Biomolecules, Carbon microtubes, gold, Mesoprous silica, iron oxide, Nano-shell, Inposite. \n Answer: ")

if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    print("You have gotten this question right, and all the other questions as well. Good job.", life_Total)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    print("You got this question wrong. ", life_Total_L1)
if Q1 == "@":   
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                if Q9 != "Δ":
                                    print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 != "Φ":
                                if Q9 != "Δ":
                                    exit()

# Repitions for Q9.
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                if Q9 == "Δ":
                                    print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    print("You got this question right. ", life_Total_L1)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    print("You got this question right. ", life_Total_L1)

if Q1 == "@":   
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":   
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":   
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":   
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":   
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":   
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    print("You got this question wrong. ", life_Total_FinalLife)
if Q1 != "@":   
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    print("You got this question wrong. ", life_Total_FinalLife)

if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                if Q9 != "Δ":
                                    exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                if Q9 != "Δ":
                                    exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                if Q9 != "Δ":
                                    exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                if Q9 != "Δ":
                                    exit()
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                if Q9 != "Δ":
                                    exit()
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                if Q9 != "Δ":
                                    exit()

print("\n")

# Question 10
Q10 = input("What is the science of transgenic Salmon compared to non-transgenic Salmon? \n Sleep: Taking the enzymes that alter growth according to seasonal and water changes, and editing them to die. \n δ: Taking the enzymes that alter growth according to seasonal and water conditions, and changing these strands to grow and continue growing. \n ~: Taking the enzymes that alter growth according to seasonal and water conditions, and changing these strands for them to mate only. \n Answer: ")
Q10_clip = print("Watch this clip to answer the question: https://www.youtube.com/watch?v=UFkHcs7WmuA")

if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 == "δ":
                                        print("You have gotten this question right, and all the other questions as well. Good job.", life_Total)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 != "δ":
                                        print("You got this question wrong. ", life_Total_L1)
if Q1 == "@":   
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    if Q10 != "δ":
                                        print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                if Q9 != "Δ":
                                    if Q10 != "δ":
                                        exit()
                                    
# Repitions for Q10.
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    if Q10 == "δ":
                                        print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                if Q9 == "Δ":
                                    if Q10 == "δ":
                                        print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 == "δ":
                                        print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 == "δ":
                                        print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 == "δ":
                                        print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 == "δ":
                                        print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 == "δ":
                                        print("You got this question right. ", life_Total_L1)
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 == "δ":
                                        print("You got this question right. ", life_Total_L1)
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 == "δ":
                                        print("You got this question right. ", life_Total_L1)

if Q1 == "@":   
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 != "Φ":
                                if Q9 == "Δ":
                                    if Q10 != "δ":
                                        print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":   
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 != "δ":
                                        print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":   
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 != "δ":
                                        print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":   
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 != "δ":
                                        print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":   
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 != "δ":
                                        print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":   
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 != "δ":
                                        print("You got this question wrong. ", life_Total_FinalLife)
if Q1 == "@":   
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 != "δ":
                                        print("You got this question wrong. ", life_Total_FinalLife)
if Q1 != "@":   
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 == "Δ":
                                    if Q10 != "δ":
                                        print("You got this question wrong. ", life_Total_FinalLife)

if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    if Q10 != "δ":
                                        exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 != "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    if Q10 != "δ":
                                        exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 != "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    if Q10 != "δ":
                                        exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 != "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    if Q10 != "δ":
                                        exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 != "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    if Q10 != "δ":
                                        exit()
if Q1 == "@":
    if Q2 == "one":
        if Q3 != "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    if Q10 != "δ":
                                        exit()
if Q1 == "@":
    if Q2 != "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    if Q10 != "δ":
                                        exit()
if Q1 != "@":
    if Q2 == "one":
        if Q3 == "@":
            if Q4 == "BETA":
                if Q5 == "nine":
                    if Q6 == "β":
                        if Q7 == "Σ":
                            if Q8 == "Φ":
                                if Q9 != "Δ":
                                    if Q10 != "δ":
                                        exit()



# Ciper Escape Code.
print("\n")
cipher = input("Enter the code from the questions you answered now, to escape from here (with no spaces)! \n Code: ")

print("\n")

if cipher == "@one@BETAnineβΣΦΔδ":
    img = Image.open('Q&A Nanobiotech/you_win.jpg')
    img.show()
    Finish = input("You now have the chance to get an award. Your prize --> https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    print("You have won the game! You can now leave.")
elif cipher != "@one@BETAnineβΣΦΔδ":
    print("Sadly, you cannot leave. You have got this question wrong. Time for you to redo the quiz I guess...")

