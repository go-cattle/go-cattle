const form = document.getElementById("symptoms-form");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  
  const symptoms = [];
  
  // Retrieve the user's input from the form
  const checkboxes = document.querySelectorAll("input[type='checkbox']:checked");
  checkboxes.forEach((checkbox) => {
    symptoms.push(checkbox.value);
  });
  
  // Format the symptoms as a string for input to the OpenAI API
  const symptomString = symptoms.join(" ");
  
  // Make an API call to the OpenAI API to get the disease diagnosis
  fetch("https://api.openai.com/v1/engines/davinci-codex/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer YOUR_API_KEY"
    },
    body: JSON.stringify({
      prompt: `Based on the symptoms provided, what disease is the cattle most likely suffering from? Symptoms: ${symptomString}`,
      max_tokens: 1,
      temperature: 0.7
    })
  })
  .then(response => response.json())
  .then(data => {
    // Display the disease diagnosis to the user
    const output = document.getElementById("diagnosis-output");
    output.innerHTML = `The most likely disease is ${data.choices[0].text}.`;
  })
  .catch(error => {
    console.error(error);
  });
});
