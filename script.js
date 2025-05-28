document.addEventListener('DOMContentLoaded', () => {
    // Get references to key HTML elements
    const resumeForm = document.getElementById('resumeForm');
    const clearButton = document.getElementById('clearButton');
    const errorMessagesDiv = document.getElementById('errorMessages');

    // Input fields
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const phoneInput = document.getElementById('phone');
    const linkedinInput = document.getElementById('linkedin');
    const placeInput = document.getElementById('place');
    
    const genderRadioButtons = document.getElementsByName('gender'); // Get all radio buttons by name

    const objectiveTextarea = document.getElementById('objective');
    const skillsInput = document.getElementById('skills');

    const degreeInput = document.getElementById('degree');
    const yearOfPassingInput = document.getElementById('yearOfPassing');
    const projectsTextarea = document.getElementById('projects');
    const internshipTextarea = document.getElementById('internship');
    const achievementsTextarea = document.getElementById('achievements');

    // --- "Clear" Button Functionality ---
    clearButton.addEventListener('click', () => {
        // Reset text input and textarea fields
        nameInput.value = '';
        emailInput.value = '';
        phoneInput.value = '';
        linkedinInput.value = '';
        placeInput.value = '';
        
        objectiveTextarea.value = '';
        skillsInput.value = '';
        
        degreeInput.value = '';
        yearOfPassingInput.value = '';
        projectsTextarea.value = '';
        internshipTextarea.value = '';
        achievementsTextarea.value = '';

        // Deselect gender radio buttons
        for (const radioButton of genderRadioButtons) {
            radioButton.checked = false;
        }

        // Clear error messages
        errorMessagesDiv.innerHTML = '';
        errorMessagesDiv.style.display = 'none'; // Hide if it was made visible

        // Set focus to the first input field
        nameInput.focus();
    });

    // --- Form Submission Handling ---
    resumeForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent default form submission

        // Clear previous error messages
        errorMessagesDiv.innerHTML = '';
        errorMessagesDiv.style.display = 'none';

        const resumeData = getFormData();
        // console.log('Resume Data:', resumeData); // Keep for debugging if needed, but validation is next

        const validationErrors = validateData(resumeData);

        if (validationErrors.length > 0) {
            errorMessagesDiv.innerHTML = validationErrors.map(error => `<p>${error}</p>`).join('');
            errorMessagesDiv.style.display = 'block'; // Make sure it's visible
        } else {
            errorMessagesDiv.innerHTML = ''; // Clear any previous errors
            errorMessagesDiv.style.display = 'none';
            console.log("Validation successful! Generating resume...");

            const resumeText = generateResumeText(resumeData);
            const filename = (resumeData.name.replace(/\s+/g, '_') || 'resume') + "_resume.txt";
            downloadResume(resumeText, filename);
            
            // Optionally, display a success message or clear form after download
            // For now, let's log success
            console.log("Resume generated and download initiated.");
            // alert("Resume generated! Check your downloads."); // Simple alert
        }
    });

    // --- Resume Text Generation Function ---
    function generateResumeText(data) {
        let output = `
  RESUME
  ===============================================================================

  OBJECTIVE
  -------------------------------------------------------------------------------
  ${data.objective || 'N/A'}

  PERSONAL DETAILS
  -------------------------------------------------------------------------------
  NAME            : ${data.name || 'N/A'}
  EMAIL           : ${data.email || 'N/A'}
  PHONE           : ${data.phone || 'N/A'}
  GENDER          : ${data.gender || 'N/A'}
  LINKEDIN URL    : ${data.linkedin || 'N/A'}
  PLACE           : ${data.place || 'N/A'}

  EDUCATION & SKILLS
  -------------------------------------------------------------------------------
  DEGREE          : ${data.degree || 'N/A'}
  YEAR OF PASSING : ${data.yearOfPassing || 'N/A'}
  SKILLS          : ${data.skills || 'N/A'}

  EXPERIENCE & ACHIEVEMENTS
  -------------------------------------------------------------------------------
  PROJECTS        :
  ${data.projects ? data.projects.split('\n').map(line => `  - ${line}`).join('\n') : '  N/A'}

  INTERNSHIP      :
  ${data.internship ? data.internship.split('\n').map(line => `  - ${line}`).join('\n') : '  N/A'}

  ACHIEVEMENTS    :
  ${data.achievements ? data.achievements.split('\n').map(line => `  - ${line}`).join('\n') : '  N/A'}

  ===============================================================================
        `;
        // Remove leading/trailing whitespace and ensure consistent newlines
        return output.trim().replace(/\r\n/g, '\n');
    }

    // --- Resume Download Function ---
    function downloadResume(resumeText, filename) {
        const blob = new Blob([resumeText], { type: 'text/plain;charset=utf-8;' });
        const link = document.createElement("a");

        if (link.download !== undefined) { // Check if HTML5 download attribute is supported
            const url = URL.createObjectURL(blob);
            link.setAttribute("href", url);
            link.setAttribute("download", filename);
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            URL.revokeObjectURL(url); // Clean up
        } else {
            // Fallback for older browsers (less common now)
            alert("Your browser does not support direct file download. Please copy the resume content manually.");
            // Optionally, display the resume text in a new window or textarea for manual copying
            const resumeWindow = window.open("", "_blank");
            if (resumeWindow) {
                resumeWindow.document.write("<pre>" + resumeText + "</pre>");
            } else {
                console.error("Could not open new window for resume preview.");
            }
        }
    }

    // --- Data Validation Function ---
    function validateData(data) {
        const errors = [];
        const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

        // Required fields
        if (!data.name) {
            errors.push("Name is required.");
        }
        if (!data.email) {
            errors.push("Email is required.");
        } else if (!emailRegex.test(data.email)) {
            errors.push("Email format is invalid (e.g., user@example.com).");
        }
        if (!data.phone) {
            errors.push("Phone number is required.");
        }
        if (!data.gender) { // Check if gender is selected
            errors.push("Gender must be selected.");
        }
        if (!data.objective) {
            errors.push("Career Objective is required.");
        }
        if (!data.skills) {
            errors.push("Skills are required (comma-separated).");
        }
        if (!data.degree) {
            errors.push("Degree is required.");
        }
        if (!data.yearOfPassing) {
            errors.push("Year of Passing is required.");
        }
        
        // Optional fields (LinkedIn, Place, Projects, Internship, Achievements)
        // are not checked for emptiness here unless specific format validation is needed.

        return errors;
    }

    // --- Data Collection Function ---
    function getFormData() {
        const resumeData = {};

        resumeData.name = nameInput.value.trim();
        resumeData.email = emailInput.value.trim();
        resumeData.phone = phoneInput.value.trim();
        resumeData.linkedin = linkedinInput.value.trim();
        resumeData.place = placeInput.value.trim();

        // Get selected gender
        let selectedGender = '';
        for (const radioButton of genderRadioButtons) {
            if (radioButton.checked) {
                selectedGender = radioButton.value;
                break;
            }
        }
        resumeData.gender = selectedGender;

        resumeData.objective = objectiveTextarea.value.trim();
        resumeData.skills = skillsInput.value.trim();

        resumeData.degree = degreeInput.value.trim();
        resumeData.yearOfPassing = yearOfPassingInput.value.trim();
        resumeData.projects = projectsTextarea.value.trim();
        resumeData.internship = internshipTextarea.value.trim();
        resumeData.achievements = achievementsTextarea.value.trim();
        
        return resumeData;
    }
});
