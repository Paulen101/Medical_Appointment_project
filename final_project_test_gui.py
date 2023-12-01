import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from final_project_test import Patient, Doctor, HospitalSystem

class HospitalGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital System")

        self.hospital_system = HospitalSystem()

        self.create_widgets()

    def create_widgets(self):
        # Create patient registration frame
        patient_frame = tk.Frame(self.master)
        patient_frame.pack(pady=10)

        tk.Label(patient_frame, text="Patient ID:").grid(row=0, column=0)
        tk.Label(patient_frame, text="Name:").grid(row=1, column=0)
        tk.Label(patient_frame, text="Age:").grid(row=2, column=0)
        tk.Label(patient_frame, text="Gender:").grid(row=3, column=0)

        self.patient_id_entry = tk.Entry(patient_frame)
        self.patient_id_entry.grid(row=0, column=1)
        self.name_entry = tk.Entry(patient_frame)
        self.name_entry.grid(row=1, column=1)
        self.age_entry = tk.Entry(patient_frame)
        self.age_entry.grid(row=2, column=1)
        self.gender_entry = tk.Entry(patient_frame)
        self.gender_entry.grid(row=3, column=1)

        tk.Button(patient_frame, text="Register Patient", command=self.register_patient).grid(row=4, column=0, columnspan=2)

        # Create doctor registration frame
        doctor_frame = tk.Frame(self.master)
        doctor_frame.pack(pady=10)

        tk.Label(doctor_frame, text="Doctor ID:").grid(row=0, column=0)
        tk.Label(doctor_frame, text="Name:").grid(row=1, column=0)
        tk.Label(doctor_frame, text="Specialization:").grid(row=2, column=0)

        self.doctor_id_entry = tk.Entry(doctor_frame)
        self.doctor_id_entry.grid(row=0, column=1)
        self.doctor_name_entry = tk.Entry(doctor_frame)
        self.doctor_name_entry.grid(row=1, column=1)
        self.specialization_entry = tk.Entry(doctor_frame)
        self.specialization_entry.grid(row=2, column=1)

        tk.Button(doctor_frame, text="Register Doctor", command=self.register_doctor).grid(row=3, column=0, columnspan=2)

        # Create appointment scheduling frame
        appointment_frame = tk.Frame(self.master)
        appointment_frame.pack(pady=10)

        tk.Label(appointment_frame, text="Patient ID:").grid(row=0, column=0)
        tk.Label(appointment_frame, text="Doctor ID:").grid(row=1, column=0)
        tk.Label(appointment_frame, text="Date and Time:").grid(row=2, column=0)

        self.patient_id_app_entry = tk.Entry(appointment_frame)
        self.patient_id_app_entry.grid(row=0, column=1)
        self.doctor_id_app_entry = tk.Entry(appointment_frame)
        self.doctor_id_app_entry.grid(row=1, column=1)
        self.date_time_entry = tk.Entry(appointment_frame)
        self.date_time_entry.grid(row=2, column=1)

        tk.Button(appointment_frame, text="Schedule Appointment", command=self.schedule_appointment).grid(row=3, column=0, columnspan=2)

    def register_patient(self):
        patient_id = self.patient_id_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()

        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Error", "Invalid age. Please enter a valid number.")
            return

        patient = Patient(patient_id, name, age, gender)
        self.hospital_system.add_patient(patient)
        messagebox.showinfo("Success", f"Patient {name} registered successfully!")

    def register_doctor(self):
        doctor_id = self.doctor_id_entry.get()
        name = self.doctor_name_entry.get()
        specialization = self.specialization_entry.get()

        doctor = self.hospital_system.register_doctor(doctor_id, name, specialization)
        messagebox.showinfo("Success", f"Doctor {name} registered successfully!\nID: {doctor.doctor_id}, Specialization: {doctor.specialization}")

    def schedule_appointment(self):
        patient_id = self.patient_id_app_entry.get()
        doctor_id = self.doctor_id_app_entry.get()
        date_time = self.date_time_entry.get()

        appointment = self.hospital_system.schedule_appointment(patient_id, doctor_id, date_time)
        if appointment:
            messagebox.showinfo("Success", f"Appointment scheduled successfully!\nPatient: {appointment.patient.name}, Doctor: {appointment.doctor.name}, Date and Time: {appointment.date_time}")
        else:
            messagebox.showerror("Error", "Invalid patient ID or doctor ID. Please check and try again.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalGUI(root)
    root.mainloop()
