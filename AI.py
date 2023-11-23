import os
import spacy

nlp = spacy.load("en_core_web_lg")
from pathlib import Path

current_directory = os.path.dirname(os.path.abspath(__file__))
print("\n*Welcome to Your ChatApp*\n")
user = input("Account Username: ")
check = True
programCheck = True
file_name = "{}.txt".format(user)
file_path = os.path.join(current_directory, file_name)

if os.path.exists(file_path):
    with open(file_name, "a") as file:
        with open(file_path, 'r') as file:
            first_lineCheck = file.readline()
            while check:
                passWord = input("Account Password: ")
                first_line = next(open("{}.txt".format(user)))
                if first_lineCheck.strip() == passWord.strip():
                    print(">>>Welcome to your Data<<<")
                    check = False
                else:
                    print("Wrong Password")
else:
    with open(file_path, "w") as file:
        print("Account Doesn't exist\nCreating...")
        passWord = input("Create account Password: ")
        file.write("{}\n".format(passWord))

def load_questions_and_answers(file_path):
    qa_dict = {}
    try:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file):
                if i == 0:
                    continue
                else:
                    question, answer = line.strip().split('|')
                    qa_dict[question] = answer
        return qa_dict
    except FileNotFoundError:
        return {}

def save_question_and_answer(file_path, question, answer):
    with open(file_path, 'a') as file:
        file.write(f"{question}|{answer}\n")

def get_most_similar_question(user_question, qa_dict):
    max_similarity = 0
    most_similar_question = None
    for question in qa_dict:
        similarity = nlp(user_question).similarity(nlp(question))
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_question = question
    return most_similar_question, max_similarity

def chatbot(file_path):
    qa_dict = load_questions_and_answers(file_path)

    while True:
        user_question = input("You: ")
        if user_question.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        if user_question in qa_dict:
            print(f"Chatbot: {qa_dict[user_question]}")
        else:
            most_similar_question, similarity = get_most_similar_question(user_question, qa_dict)
            if similarity > 0.3:  # Increase the threshold for specificity of answer retreival 
                print(f"Chatbot: Did you mean '{most_similar_question}'? {qa_dict[most_similar_question]}")
                questionCheck = input("Y/N: ")
                if questionCheck == "N":
                    print("Chatbot: I don't know the answer to that. Please tell me.")
                    new_answer = input("You (provide the answer): ")
                    qa_dict[user_question] = new_answer
                    save_question_and_answer(file_path, user_question, new_answer)
                    print("Chatbot: Thanks, I've learned something new!")
                if questionCheck == "Y":
                    print(f"Chatbot: {qa_dict[most_similar_question]}")
                    continue
            else:
                print("Chatbot: I don't know the answer to that. Please tell me.")
                new_answer = input("You (provide the answer): ")
                qa_dict[user_question] = new_answer
                save_question_and_answer(file_path, user_question, new_answer)
                print("Chatbot: Thanks, I've learned something new!")

if __name__ == "__main__":
    print("Chatbot: Hello! You can ask me anything. Type 'exit' to end the conversation.")
    chatbot(file_name)
