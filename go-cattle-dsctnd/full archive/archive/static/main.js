// Fetch data from example.txt file
fetch('example.txt')
  .then(response => response.text())
  .then(data => processData(data))
  .catch(error => console.error('Error fetching data:', error));

// Function to process data from example.txt file
function processData(data) {
  // Split the data into lines
  const lines = data.split('\n');
  
  // Initialize arrays to store diseases, symptoms, and remedies
  const diseases = [];
  const symptoms = [];
  const remedies = [];
  
  // Loop through each line of data
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    
    // Extract disease name
    if (line.startsWith('Disease:')) {
      const disease = line.slice(9).trim();
      diseases.push(disease);
    }
    
    // Extract symptoms
    if (line.startsWith('Symptoms:')) {
      const symptomList = line.slice(10).trim();
      const symptomArr = symptomList.split(',').map(symptom => symptom.trim());
      symptoms.push(...symptomArr);
    }
    
    // Extract remedies
    if (line.startsWith('Remedy:')) {
      const remedyList = line.slice(8).trim();
      const remedyArr = remedyList.split(',').map(remedy => remedy.trim());
      remedies.push(...remedyArr);
    }
  }

  // Remove duplicate symptoms
  const uniqueSymptoms = [...new Set(symptoms)];

  // Generate checkboxes for symptoms in HTML
  const checkboxesContainer = document.getElementById('checkboxes-container');
  for (let i = 0; i < uniqueSymptoms.length; i++) {
    const symptom = uniqueSymptoms[i];
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.name = 'symptom';
    checkbox.value = symptom;
    const label = document.createElement('label');
    label.textContent = symptom;
    checkboxesContainer.appendChild(checkbox);
    checkboxesContainer.appendChild(label);
    checkboxesContainer.appendChild(document.createElement('br'));
  }

  // Add submit event listener to the form
  const form = document.getElementById('form');
  form.addEventListener('submit', function(event) {
    event.preventDefault();

    // Get checked symptoms
    const checkedSymptoms = Array.from(document.querySelectorAll('input[name="symptom"]:checked'))
      .map(checkbox => checkbox.value);

    // Find matching diseases
    const matchingDiseases = [];
    for (let i = 0; i < diseases.length; i++) {
      const disease = diseases[i];
      const diseaseSymptoms = symptoms[i].split(',').map(symptom => symptom.trim());
      const hasCommonSymptom = diseaseSymptoms.some(symptom => checkedSymptoms.includes(symptom));
      if (hasCommonSymptom) {
        matchingDiseases.push(disease);
      }
    }

    // Display matching diseases and remedies
    const resultContainer = document.getElementById('result-container');
    resultContainer.innerHTML = '';
    if (matchingDiseases.length > 0) {
      const heading = document.createElement('h2');
      heading.textContent = 'Matching Diseases:';
      resultContainer.appendChild(heading);
      const ul = document.createElement('ul');
      matchingDiseases.forEach(disease => {
        const li = document.createElement('li');
        li.textContent = disease + ' - Remedy: ' + remedies[diseases.indexOf(disease)];
        ul.appendChild(li);
      });
      resultContainer.appendChild(ul);
    } else{
      const message = document.createElement('p');
      message.textContent = 'No matching disease found.';
      resultContainer.appendChild(message);
      }
      });
      }
      
      
