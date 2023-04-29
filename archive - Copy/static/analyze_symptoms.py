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

# User input for symptoms
user_input = input("Enter the symptoms separated by commas: ")
symptoms = [symptom.strip().lower() for symptom in user_input.split(',')]

# Find matching diseases
matching_diseases = []
for item in data:
    item_symptoms = [s.strip().lower() for s in item['symptoms'].split(',')]
    if any(symptom in item_symptoms for symptom in symptoms):
        matching_diseases.append(item['disease'])

if matching_diseases:
    print("Matching diseases:")
    for disease in matching_diseases:
        print("- " + disease)
    user_input = input("Enter the name of the disease for which you want to find remedies: ")
    remedies = find_remedies(user_input, data)
    if remedies:
        print("Remedies for", user_input + ":")
        for remedy in remedies.split(','):
            print("- " + remedy)
    else:
        print("Disease not found.")
else:
    print("No matching diseases found.")
