import csv

filename = "dataset/Amrutvahini_College_students_list.csv"

# Create an empty dictionary to store the data
data_dict = {}

# Open the CSV file and read the data
with open(filename, "r") as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header row if present
    next(reader, None)
    # Loop through each row of the CSV file
    for row in reader:
        name, email = row
        # Add the name and email to the dictionary
        data_dict[name.lower()] = email

print(data_dict)
# Check if the student is in the dictionary
username = 'chaitanya11avcoe@gmail.com'
fname = 'Chaitanya'
lname = 'Joshi'

if username in data_dict:
    name = data_dict.get(username)
    if fname in name and lname in name:
        print("Hello")