# Function to read data from file
def read_data_from_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if lines[i].startswith('Disease:'):
                disease = lines[i].strip().split(': ')[1]
                i += 1
                symptoms = lines[i].strip().split(': ')[1]
                i += 1
                remedies = lines[i].strip().split(': ')[1]
                data.append({'disease': disease, 'symptoms': symptoms, 'remedies': remedies})
            i += 1
    return data

# Function to find remedies for a given disease
def find_remedies(disease, data):
    for item in data:
        if item['disease'].lower().strip() == disease.lower().strip():
            return item['remedies']
    return None

# Read data from file
file_path = 'example.txt' # Replace with the path of your .txt file
data = read_data_from_file(file_path)

# User input for disease
user_input = input("Enter the name of the disease: ")
remedies = find_remedies(user_input, data)
if remedies:
    print("Remedies for", user_input + ":")
    for remedy in remedies.split(','):
        print("- " + remedy)
else:
    print("Disease not found.")
