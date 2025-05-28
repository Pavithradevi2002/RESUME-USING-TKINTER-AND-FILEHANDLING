from tkinter import *
from tkinter import ttk # Import ttk
from tkinter.ttk import Combobox # Combobox is already ttk, but explicit import is fine
from tkinter import messagebox
from tkinter import filedialog # Import filedialog
import re # Import re for email validation


class ResumeData:
    """
    A data class to store and manage information for a single resume.
    """
    def __init__(self, username, mail, phone, linked, pl, gn, skill, obj, degree, year, proj, intern, ach):
        """
        Initializes the ResumeData object with all necessary resume fields.

        Args:
            username (str): The name of the person.
            mail (str): Email address.
            phone (str): Phone number.
            linked (str): LinkedIn profile URL.
            pl (str): Place/Location.
            gn (str): Gender.
            skill (str): Skills.
            obj (str): Career objective.
            degree (str): Educational degree.
            year (str): Year of passing.
            proj (str): Project details.
            intern (str): Internship details.
            ach (str): Achievements.
        """
        self.username = username
        self.mail = mail
        self.phone = phone
        self.linked = linked
        self.pl = pl
        self.gn = gn
        self.skill = skill
        self.obj = obj
        self.degree = degree
        self.year = year
        self.proj = proj
        self.intern = intern
        self.ach = ach


class ResumeApp:
    """
    Main application class for the Resume Builder.
    Manages the UI, data input, validation, and file generation.
    """
    def __init__(self, master):
        """
        Initializes the ResumeApp.

        Args:
            master (Tk): The root Tkinter window.
        """
        self.master = master
        master.title('Resume Builder')
        master.geometry('1000x750') # Set a reasonable default size

        # Configure resizing behavior for the main window
        # Allow the two main columns and the row containing the main frames to expand
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)

        self.gender = IntVar()
        self.gender.set(0) # Initialize gender to a non-selected state (0)

        self._create_widgets()

    def _create_widgets(self):
        """
        Creates and lays out all UI widgets using the ttk.grid() geometry manager.
        This includes labels, entry fields, comboboxes, radio buttons, and action buttons.
        """
        # --- Main Title ---
        title_label = ttk.Label(self.master, text='RESUME MAKER', font=('Times New Roman', 20, 'bold'), anchor='center')
        title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky='ew')
        
        # --- Main Frames Setup (Personal and Professional Details) ---
        # This helps in organizing the UI into two primary columns.
        personal_main_frame = ttk.Frame(self.master, padding=10)
        personal_main_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        personal_main_frame.columnconfigure(0, weight=1) 
        personal_main_frame.rowconfigure(0, weight=1) 

        professional_main_frame = ttk.Frame(self.master, padding=10)
        professional_main_frame.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)
        professional_main_frame.columnconfigure(0, weight=1) 
        # Configure rows in professional_main_frame to expand
        professional_main_frame.rowconfigure(0, weight=1) # Objective
        professional_main_frame.rowconfigure(1, weight=1) # Education
        professional_main_frame.rowconfigure(2, weight=1) # Experience


        # --- Personal Details Labelframe ---
        personal_lf = ttk.Labelframe(personal_main_frame, text="Personal Details", padding=10)
        personal_lf.grid(row=0, column=0, sticky='nsew', pady=(0,10))
        personal_lf.columnconfigure(1, weight=1) # Allow input fields to expand

        row_idx = 0 # Row index for grid placement within personal_lf
        ttk.Label(personal_lf, text="Name:").grid(row=row_idx, column=0, sticky='w', padx=5, pady=5)
        self.name_entry = ttk.Entry(personal_lf)
        self.name_entry.grid(row=row_idx, column=1, sticky='ew', padx=5, pady=5)
        row_idx += 1

        ttk.Label(personal_lf, text="Mail ID:").grid(row=row_idx, column=0, sticky='w', padx=5, pady=5)
        self.mailid_entry = ttk.Entry(personal_lf)
        self.mailid_entry.grid(row=row_idx, column=1, sticky='ew', padx=5, pady=5)
        row_idx += 1

        ttk.Label(personal_lf, text="Phone Number:").grid(row=row_idx, column=0, sticky='w', padx=5, pady=5)
        self.phno_entry = ttk.Entry(personal_lf)
        self.phno_entry.grid(row=row_idx, column=1, sticky='ew', padx=5, pady=5)
        row_idx += 1

        ttk.Label(personal_lf, text="LinkedIn Profile:").grid(row=row_idx, column=0, sticky='w', padx=5, pady=5)
        self.link_entry = ttk.Entry(personal_lf)
        self.link_entry.grid(row=row_idx, column=1, sticky='ew', padx=5, pady=5)
        row_idx += 1

        ttk.Label(personal_lf, text="Place:").grid(row=row_idx, column=0, sticky='w', padx=5, pady=5)
        self.place_entry = ttk.Entry(personal_lf)
        self.place_entry.grid(row=row_idx, column=1, sticky='ew', padx=5, pady=5)
        row_idx += 1

        # Gender Radiobuttons in a dedicated frame for horizontal layout
        ttk.Label(personal_lf, text="Gender:").grid(row=row_idx, column=0, sticky='w', padx=5, pady=5)
        gender_frame = ttk.Frame(personal_lf)
        gender_frame.grid(row=row_idx, column=1, sticky='ew', padx=5, pady=5)
        ttk.Radiobutton(gender_frame, text="Male", variable=self.gender, value=1).pack(side=LEFT, padx=(0,5))
        ttk.Radiobutton(gender_frame, text="Female", variable=self.gender, value=2).pack(side=LEFT, padx=(0,5))
        ttk.Radiobutton(gender_frame, text="Transgender", variable=self.gender, value=3).pack(side=LEFT)
        row_idx += 1
        
        ttk.Label(personal_lf, text="Skills:").grid(row=row_idx, column=0, sticky='w', padx=5, pady=5)
        self.skills_combo = ttk.Combobox(personal_lf, 
                                         values=['Python', 'Java', 'C', 'C++', 'Django', 'JavaScript', 'SQL', 'HTML', 'CSS', 'React', 'Angular', 'Vue.js', 'Node.js'])
        self.skills_combo.grid(row=row_idx, column=1, sticky='ew', padx=5, pady=5)
        row_idx +=1
        
        # Configure row weights in personal_lf to make rows expand if space is available (though less critical here)
        for i in range(row_idx): personal_lf.rowconfigure(i, weight=1)


        # --- Professional Details Sections (Objective, Education, Experience) ---
        
        # Objective Labelframe
        objective_lf = ttk.Labelframe(professional_main_frame, text="Objective", padding=10)
        objective_lf.grid(row=0, column=0, sticky='nsew', pady=(0,10))
        objective_lf.columnconfigure(0, weight=1) # Text widget column
        objective_lf.rowconfigure(0, weight=1)    # Text widget row
        self.objective_text = Text(objective_lf, height=5, width=40) # Standard tkinter Text widget
        self.objective_text.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

        # Education Labelframe
        education_lf = ttk.Labelframe(professional_main_frame, text="Education", padding=10)
        education_lf.grid(row=1, column=0, sticky='nsew', pady=(0,10))
        education_lf.columnconfigure(1, weight=1) # Allow input fields to expand

        edu_row_idx = 0 # Row index for grid placement within education_lf
        ttk.Label(education_lf, text="Degree:").grid(row=edu_row_idx, column=0, sticky='w', padx=5, pady=5)
        self.deg_entry = ttk.Entry(education_lf)
        self.deg_entry.grid(row=edu_row_idx, column=1, sticky='ew', padx=5, pady=5)
        edu_row_idx += 1

        ttk.Label(education_lf, text="Year of Passing:").grid(row=edu_row_idx, column=0, sticky='w', padx=5, pady=5)
        self.yop_entry = ttk.Entry(education_lf)
        self.yop_entry.grid(row=edu_row_idx, column=1, sticky='ew', padx=5, pady=5)
        edu_row_idx += 1
        
        ttk.Label(education_lf, text="Projects:").grid(row=edu_row_idx, column=0, sticky='w', padx=5, pady=5)
        self.project_entry = ttk.Entry(education_lf)
        self.project_entry.grid(row=edu_row_idx, column=1, sticky='ew', padx=5, pady=5)
        edu_row_idx += 1
        for i in range(edu_row_idx): education_lf.rowconfigure(i, weight=1)


        # Experience Labelframe
        experience_lf = ttk.Labelframe(professional_main_frame, text="Experience", padding=10)
        experience_lf.grid(row=2, column=0, sticky='nsew', pady=(0,10))
        experience_lf.columnconfigure(1, weight=1) # Allow input fields to expand

        exp_row_idx = 0 # Row index for grid placement within experience_lf
        ttk.Label(experience_lf, text="Internship Details:").grid(row=exp_row_idx, column=0, sticky='w', padx=5, pady=5)
        self.internship_entry = ttk.Entry(experience_lf)
        self.internship_entry.grid(row=exp_row_idx, column=1, sticky='ew', padx=5, pady=5)
        exp_row_idx += 1

        ttk.Label(experience_lf, text="Achievements:").grid(row=exp_row_idx, column=0, sticky='w', padx=5, pady=5)
        self.achieve_entry = ttk.Entry(experience_lf)
        self.achieve_entry.grid(row=exp_row_idx, column=1, sticky='ew', padx=5, pady=5)
        exp_row_idx += 1
        for i in range(exp_row_idx): experience_lf.rowconfigure(i, weight=1)
        

        # --- Buttons Frame (Submit and Clear) ---
        buttons_frame = ttk.Frame(self.master, padding=10)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky='ew', pady=10)
        # Configure columns to center buttons or push them apart
        buttons_frame.columnconfigure(0, weight=1) 
        buttons_frame.columnconfigure(1, weight=1)

        self.submit_button = ttk.Button(buttons_frame, text="SUBMIT", command=self.add_data)
        self.submit_button.grid(row=0, column=0, padx=5, sticky='e') # Align to the right of its cell

        self.clear_button = ttk.Button(buttons_frame, text="CLEAR", command=self.clear_data)
        self.clear_button.grid(row=0, column=1, padx=5, sticky='w') # Align to the left of its cell


    def add_data(self):
        """
        Gathers data from UI fields, validates it, and if valid,
        prompts the user for a filename and saves the resume data.
        """
        # --- Gather data from UI elements ---
        username = self.name_entry.get()
        linked = self.link_entry.get()
        place = self.place_entry.get()
        mail = self.mailid_entry.get()
        phone = self.phno_entry.get()
        
        gender_value = self.gender.get()
        gender_str = ""
        if gender_value == 1:
            gender_str = "Male"
        elif gender_value == 2:
            gender_str = "Female"
        elif gender_value == 3: # Assuming 3 is for Transgender and it's a valid selection
            gender_str = "Transgender"
        # If gender_value is 0 (unselected), gender_str remains "" which is handled by validation.

        skill = self.skills_combo.get()
        objective = self.objective_text.get(1.0, END) # Get all text from Text widget
        degree = self.deg_entry.get()
        year_of_passing = self.yop_entry.get()
        projects = self.project_entry.get()
        internship = self.internship_entry.get()
        achievements = self.achieve_entry.get()

        # --- Create ResumeData instance ---
        # Objective is stripped here before being passed to ResumeData
        current_resume_data = ResumeData(
            username=username,
            mail=mail,
            phone=phone,
            linked=linked,
            pl=place,
            gn=gender_str,
            skill=skill,
            obj=objective.strip(), 
            degree=degree,
            year=year_of_passing,
            proj=projects,
            intern=internship,
            ach=achievements
        )

        # --- Enhanced Validation Logic ---
        error_messages = []

        if not current_resume_data.username.strip(): # Check stripped version for validation
            error_messages.append("Name is required.")
        if not current_resume_data.mail.strip():
            error_messages.append("Email is required.")
        elif not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", current_resume_data.mail): # Email format regex
            error_messages.append("Email format is invalid (e.g., user@example.com).")
        if not current_resume_data.phone.strip():
            error_messages.append("Phone number is required.")
        if not current_resume_data.linked.strip():
            error_messages.append("LinkedIn Profile URL is required.")
        if not current_resume_data.pl.strip(): 
            error_messages.append("Place is required.")
        
        if not current_resume_data.gn: # Check if gender string is empty (means not selected)
            error_messages.append("Gender must be selected.")
        
        if not current_resume_data.skill.strip():
            error_messages.append("At least one skill must be selected/entered.")
        
        if not current_resume_data.obj: # Already stripped
            error_messages.append("Objective cannot be empty.")
            
        if not current_resume_data.degree.strip():
            error_messages.append("Degree is required.")
        if not current_resume_data.year.strip():
            error_messages.append("Year of Passing is required.")
        if not current_resume_data.proj.strip():
            error_messages.append("Project details are required.")
        if not current_resume_data.intern.strip():
            error_messages.append("Internship details are required.")
        if not current_resume_data.ach.strip():
            error_messages.append("Achievements are required.")

        # If there are any error messages, display them and stop processing
        if error_messages:
            messagebox.showerror("Validation Error", "\n".join(error_messages))
            return
        
        # --- File Dialog and Saving Logic (only if validation passes) ---
        default_filename = f"{current_resume_data.username.replace(' ', '_')}_resume.txt" # Sanitize username for filename
        
        # Prompt user for save location and filename
        fname = filedialog.asksaveasfilename(
            initialfile=default_filename,
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("Word Document", "*.doc"), ("All files", "*.*")]
        )

        if not fname: # User cancelled the save dialog
            return 

        # --- Write data to the selected file ---
        try:
            with open(fname, 'w') as fi:
                fi.write("  RESUME \n") # Added newline for better start
                fi.write("\n\nOBJECTIVE \n")
                fi.write(current_resume_data.obj + "\n") # Add newline after content
                fi.write("\n\nPERSONAL DETAILS\n")
                fi.write(f"NAME            : {current_resume_data.username}\n")
                fi.write(f"EMAIL           : {current_resume_data.mail}\n")
                fi.write(f"PHONE           : {current_resume_data.phone}\n")
                fi.write(f"GENDER          : {current_resume_data.gn}\n")
                fi.write(f"LINKED IN URL   : {current_resume_data.linked}\n")
                fi.write(f"PLACE           : {current_resume_data.pl}\n")
                fi.write("\n\nEDUCATION DETAILS\n")
                fi.write(f"DEGREE          : {current_resume_data.degree}\n")
                fi.write(f"YEAR OF PASSING : {current_resume_data.year}\n")
                fi.write(f"SKILLS          : {current_resume_data.skill}\n")
                fi.write("\n\nEXPERIENCE\n") # Added a header for Experience section
                fi.write(f"INTERNSHIP      : {current_resume_data.intern}\n")
                fi.write(f"PROJECT         : {current_resume_data.proj}\n") # Moved project under experience as it's often project experience
                fi.write(f"ACHIEVEMENTS    : {current_resume_data.ach}\n")
            messagebox.showinfo("Success", f"Resume successfully saved to:\n{fname}")
        except IOError as e:
            messagebox.showerror("File Save Error", f"Could not save the resume to the specified location.\nError: {e}")
        except Exception as e: # Catch any other unexpected errors during save
            messagebox.showerror("Error", f"An unexpected error occurred while saving the resume: {e}")


    def clear_data(self):
        """
        Clears all input fields in the form, resetting them to their default states.
        """
        self.name_entry.delete(0, END)
        self.mailid_entry.delete(0, END)
        self.phno_entry.delete(0, END)
        self.link_entry.delete(0, END)
        self.place_entry.delete(0, END)
        self.gender.set(0) # Reset gender selection
        self.skills_combo.set('') # Clear combobox selection
        
        self.objective_text.delete(1.0, END) # Clear Text widget
        
        self.deg_entry.delete(0, END)
        self.yop_entry.delete(0, END)
        self.project_entry.delete(0, END)
        self.internship_entry.delete(0, END)
        self.achieve_entry.delete(0, END)

        # Set focus to the first entry field after clearing
        self.name_entry.focus_set()


if __name__ == "__main__":
    root = Tk()
    app = ResumeApp(root)
    root.mainloop()
