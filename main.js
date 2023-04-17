// Function to read data from file
function readDataFromFile(fileData) {
    var data = [];
    var lines = fileData.split('\n');
    var i = 0;
    while (i < lines.length) {
        if (lines[i].startsWith('Disease:')) {
            var disease = lines[i].trim().split(': ')[1];
            i++;
            var symptoms = lines[i].trim().split(': ')[1];
            i++;
            var remedies = lines[i].trim().split(': ')[1];
            data.push({'disease': disease, 'symptoms': symptoms, 'remedies': remedies});
        }
        i++;
    }
    return data;
}

// Function to find remedies for a given disease
function findRemedies(disease, data) {
    for (var i = 0; i < data.length; i++) {
        if (data[i]['disease'].toLowerCase().trim() === disease.toLowerCase().trim()) {
            return data[i]['remedies'];
        }
    }
    return null;
}

// Read data from file
var fileData = `Disease: Disease1
Symptoms: Symptom1, Symptom2, Symptom3
Remedies: Remedy1, Remedy2

Disease: Disease2
Symptoms: Symptom2, Symptom3, Symptom4
Remedies: Remedy3, Remedy4`;

var data = readDataFromFile(fileData);

// User input for symptoms
var userInput = prompt("Enter the symptoms separated by commas: ");
var symptoms = userInput.split(',').map(function(symptom) {
    return symptom.trim().toLowerCase();
});

// Find matching diseases
var matchingDiseases = [];
for (var i = 0; i < data.length; i++) {
    var itemSymptoms = data[i]['symptoms'].split(',').map(function(s) {
        return s.trim().toLowerCase();
    });
    if (itemSymptoms.some(function(symptom) {
        return symptoms.includes(symptom);
    })) {
        matchingDiseases.push(data[i]['disease']);
    }
}

if (matchingDiseases.length > 0) {
    console.log("Matching diseases:");
    for (var i = 0; i < matchingDiseases.length; i++) {
        console.log("- " + matchingDiseases[i]);
    }
    var userInput = prompt("Enter the name of the disease for which you want to find remedies: ");
    var remedies = findRemedies(userInput, data);
    if (remedies) {
        console.log("Remedies for " + userInput + ":");
        console.log("- " + remedies.split(',').join('\n- '));
    } else {
        console.log("Disease not found.");
    }
} else {
    console.log("No matching diseases found.");
}
