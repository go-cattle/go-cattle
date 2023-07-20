import json

# Read the .txt file
with open('cattle_diseases.txt', 'r') as file:
    lines = file.readlines()

disease_list = []

# Loop through each line and extract disease information
for line in lines:
    # Check for disease name
    if line.startswith('-'):
        disease_name = line.strip('-').strip()
    # Check for breed
    elif line.startswith('-- Breeds:'):
        breed = line.strip('-- Breeds:').strip()
    # Check for symptoms
    elif line.startswith('-- Symptoms:'):
        symptoms = line.strip('-- Symptoms:').strip().split(';')
    # Check for remedies
    elif line.startswith('-- Remedies:'):
        remedies = line.strip('-- Remedies:').strip().split(';')
        # Create a dictionary for the disease
        disease = {
            'Disease Name': disease_name,
            'Breed': breed,
            'Symptoms': symptoms,
            'Remedies': remedies
        }
        # Append the disease dictionary to the disease list
        disease_list.append(disease)

# Create a JSON file to store the disease list
with open('cattle_diseases.json', 'w') as json_file:
    json.dump(disease_list, json_file, indent=4)

# Print the disease list
print(disease_list)
