import re
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import csv
import pickle

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')
stop_words = stopwords.words('english')
stemmer = PorterStemmer()
############################################################################################################
#                                       User Authentication Function                                       #
############################################################################################################
def name_valid(name):
    if name.isalpha() and len(name) > 2:
        return True
    else:
        return False

def password_valid(pass1):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
	
	# compiling regex
    pat = re.compile(reg)
	
	# searching regex				
    mat = re.search(pat, pass1)
	
	# validating conditions
    if mat:
        return True
    else:
        return False

def password_check(password1, password2):
    if password1 == password2:
        return True
    else : 
        return False

def contact_valid(number):
    Pattern = re.fullmatch("[6-9][0-9]{9}",number)
    if Pattern != None:
        return True
    else:
        return False

def authentication(first_name, last_name, pass1, pass2):
    if name_valid(first_name) == False:
        return "Invalid First Name"           
    elif name_valid(last_name) == False:
            return "Invalid Last Name"
    elif password_valid(pass1) == False:
        return "Password Should be in Proper Format. (eg. Password@1234)"
    elif password_check(pass1, pass2) == False:
        return "Password Not Matched"
    else:
        return "success"
############################################################################################################
#                                         Prediction                                          #
############################################################################################################



def predict(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15):
    sentiment = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15]
    happiness_dataset = pd.read_csv('dataset/happiness_index_dataset (1).csv')
    happiness_dataset.dropna()
    happiness_dataset['Result'].value_counts()
    happiness_dataset.groupby('Result').mean()
    X = happiness_dataset.drop(columns = 'Result', axis=1)
    Y = happiness_dataset['Result']
    scaler = StandardScaler()
    scaler.fit(X)
    standardized_data = scaler.transform(X)
    X = standardized_data
    Y = happiness_dataset['Result']
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=24)
    classifier = svm.SVC(kernel='linear')
    #training the support vector Machine Classifier
    classifier.fit(X_train, Y_train)
    input_data = (sentiment)
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    # standardize the input data
    std_data = scaler.transform(input_data_reshaped)
    prediction = classifier.predict(std_data)
    return prediction[0]

def preprocess(text):
    # Remove unnecessary characters
    text = text.replace("<br />", " ")
    # Convert to lowercase
    text = text.lower()
    # Remove stop words and stem words
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    return " ".join(words)

def review_prediction(review):
    # Load the model from a file
    with open("dataset/feedback_predict.pkl", "rb") as f:
        model = pickle.load(f)
    with open("dataset/feedback_vectorizer.pkl", "rb") as f:
        vector = pickle.load(f)
    
    external_review_vect = vector.transform([preprocess(review)])
    external_feedback = model.predict(external_review_vect)[0]
    external_feedback = int(external_feedback)
    if external_feedback >= 8 and external_feedback <=10:
        return "Happy",external_feedback
    elif external_feedback >=3 and external_feedback <= 7:
        return "Moderate Happy",external_feedback
    else:
        return "Not Happy",external_feedback

def predict_final_feedback(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,feedback_count):
    list1 = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15]
    total = sum([eval(x) for x in list1])
    average = total/15
    final_pred = (average + feedback_count)/2
    final_pred = int(final_pred)
    if final_pred >= 8 and final_pred <=10:
        return "Happy"
    elif final_pred >=3 and final_pred <= 7:
        return "Moderate Happy"
    else:
        return "Not Happy"
#################################################################################
#                          Student Valid                                        #
#################################################################################
def valid(fname, lname, username, designation):
    if designation == "Student":
        filename = "dataset/met_students.csv"
    elif designation == "Staff":
        filename = "dataset/met_staff.csv"
    else:
        filename = "dataset/met_other_than_teacher_staff.csv"

    # Create an empty dictionary to store the data
    data_dict = {}
    print(f"Filename: {filename}")
    print(f"Initial data_dict: {data_dict}")

    # Open the CSV file and read the data
    try:
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            print("CSV Reader Initialized")
            # Skip the header row if present
            next(reader, None)
            # Loop through each row of the CSV file
            for row in reader:
                if len(row) >= 2:  # Ensure there are at least two columns
                    email, name = row  # Assuming first column is email and second is name
                    # Add the email and name to the dictionary, using email as the key
                    data_dict[email.strip().lower()] = name.strip().lower()

        print(f"Loaded data_dict: {data_dict}")

        if username.strip().lower() in data_dict:
            stored_name = data_dict[username.strip().lower()]
            print(f"Stored name: {stored_name}")
            # Check if either the first name or last name matches the stored name
            if fname.strip().lower() in stored_name or lname.strip().lower() in stored_name:
                return True
            else:
                return False
        else:
            return False
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
