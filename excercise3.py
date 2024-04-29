#KBC GAME EXCERISE 
print("WELCOME TO KBC : \n")
questions = ["How many planets are in the solar system? ", "Who is the Prime Minister of India? ", "What is the currency of India? "]
prices = [90000, 100000, 200000] # Corrected prices to integers
options = [[9, 8, 3, 1], ["Narendra Modi", "Manmohan Singh", "Elvish Yadav", "Orry"], ["Rupees", "Dollars", "Pounds", "Euros"]]
correct_answers = [1, 0, 0]
final_amount = 0 # for price calculations
#nested loop to check each option of every single question.
for i in range(len(questions)):
    print("Question:", questions[i])  #looping through every questions
    print("Options:")
    for j in range(len(options[i])):    
        print(f"{j+1}.{options[i][j]}") # looping through every single option by converting each option into string
    
    user_answer = int(input("Enter your answer (1, 2, 3, 4): ")) - 1
    #converting user input into integer 

    if user_answer != correct_answers[i]:
        print("Wrong Answer!")
        break       #if the answer is wrong then print wrong answer and break out of loop
    else:
        print("Correct Answer!")
        final_amount += prices[i] #if answer is correct print correct answer and add the price to final amount

print("Final Amount:", final_amount , "$") #print final amount 
