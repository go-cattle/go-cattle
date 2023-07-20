# Read diseases and symptoms from data.txt
with open('data.txt', 'r') as file:
    data = file.read().splitlines()

diseases = []
current_disease = None

# Parse data and extract diseases and symptoms
for line in data:
    if line.startswith('Disease:'):
        # Start of a new disease
        disease_name = line[9:]
        
        # Check if the disease already exists
        if not any(disease['name'] == disease_name for disease in diseases):
            current_disease = {'name': disease_name, 'symptoms': []}
            diseases.append(current_disease)
    elif line.startswith('Symptoms:'):
        # Symptoms of the current disease
        symptoms = line[10:].split(', ')
        current_disease['symptoms'] = symptoms

# Count the number of diseases and symptoms
num_diseases = len(diseases)
num_symptoms = sum(len(disease['symptoms']) for disease in diseases)

# Print the results
print(f"Number of Diseases: {num_diseases}")
print(f"Number of Symptoms: {num_symptoms}")
