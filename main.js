// Read example.txt file using Fetch API
fetch('example.txt')
  .then(response => response.text())
  .then(text => {
    // Split text by lines
    const lines = text.split('\n');
    let diseases = [];
    let symptoms = [];
    let remedies = [];

    // Loop through lines and extract disease, symptoms, and remedies
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();
      if (line.startsWith('Disease:')) {
        diseases.push(line.replace('Disease:', '').trim());
      } else if (line.startsWith('Symptoms:')) {
        const symptomList = line.replace('Symptoms:', '').trim();
        const symptomArr = symptomList.split(',');
        for (let j = 0; j < symptomArr.length; j++) {
          const symptom = symptomArr[j].trim();
          if (!symptoms.includes(symptom)) {
            symptoms.push(symptom);
          }
        }
      } else if (line.startsWith('Remedy:')) {
        remedies.push(line.replace('Remedy:', '').trim());
      }
    }

    // Create checkboxes for symptoms
    const checkboxesContainer = document.getElementById('checkboxes-container');
    for (let i = 0; i < symptoms.length; i++) {
      const symptom = symptoms[i];
      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.id = 'checkbox-' + i;
      checkbox.value = symptom;
      const label = document.createElement('label');
      label.textContent = symptom;
      label.setAttribute('for', 'checkbox-' + i);
      checkboxesContainer.appendChild(checkbox);
      checkboxesContainer.appendChild(label);
      checkboxesContainer.appendChild(document.createElement('br'));
    }

    // Handle form submission
    const form = document.getElementById('form');
    form.addEventListener('submit', function(event) {
      event.preventDefault();
      const selectedSymptoms = Array.from(form.elements)
        .filter(element => element.type === 'checkbox' && element.checked)
        .map(element => element.value);

      // Find matching disease and display remedy
      let matchingDisease = '';
      let matchingRemedy = '';
      for (let i = 0; i < diseases.length; i++) {
        const disease = diseases[i];
        const diseaseSymptoms = lines[lines.indexOf('Disease: ' + disease) + 1]
          .replace('Symptoms:', '')
          .trim()
          .split(', ')
          .map(symptom => symptom.trim());
        if (selectedSymptoms.every(symptom => diseaseSymptoms.includes(symptom))) {
          matchingDisease = disease;
          matchingRemedy = lines[lines.indexOf('Disease: ' + disease) + 2].replace('Remedy:', '').trim();
          break;
        }
      }

      // Display matching disease and remedy
      const resultContainer = document.getElementById('result-container');
      resultContainer.textContent = '';
      if (matchingDisease !== '') {
        const diseaseHeading = document.createElement('h3');
        diseaseHeading.textContent = 'Matching Disease: ' + matchingDisease;
        resultContainer.appendChild(diseaseHeading);
        const remedyParagraph = document.createElement('p');
        remedyParagraph.textContent = 'Remedy: ' + matchingRemedy;
        resultContainer.appendChild(remedyParagraph);
      } else {
        const noMatchParagraph = document.createElement('p');
        noMatchParagraph.textContent = 'No matching disease found.';
        resultContainer.appendChild(noMatchParagraph);
      }
    });
  })
  .catch(error => {
    console.error('Failed to fetch example.txt:', error);
  });
