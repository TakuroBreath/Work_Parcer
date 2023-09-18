from src.user_exp.actions import *
from src.processing import HeadHunter, SuperJob
from src.user_exp.actions import save_vacancies, get_top_vac
import tkinter as tk

from tkinter import messagebox


class FirstWindow:
    # name = ""
    # salary = 0
    # count = 0

    def __init__(self, master):
        self.name = ""
        self.salary = 0
        self.count = 0

        self.master = master
        self.master.title("Enter criteria")
        self.master.geometry("300x150")

        self.name_label = tk.Label(master, text="Job Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.salary_label = tk.Label(master, text="Salary:")
        self.salary_label.pack()
        self.salary_entry = tk.Entry(master)
        self.salary_entry.pack()

        self.count_label = tk.Label(master, text="Count of vacancies:")
        self.count_label.pack()
        self.count_entry = tk.Entry(master)
        self.count_entry.pack()

        self.enter_button = tk.Button(master, text="Confirm", command=self.enter)
        self.enter_button.pack()

    def enter(self):
        global job_name, job_salary, job_count
        job_name = str(self.name_entry.get())
        job_salary = int(self.salary_entry.get())
        job_count = int(self.count_entry.get())


        self.master.destroy()
        root = tk.Tk()
        SecondWindow(root)
        root.mainloop()
        return self.name, self.salary, self.count


class SecondWindow:

    hh_vacancies = []
    sj_vacancies = []

    hh_site = HeadHunter()
    sj_site = SuperJob()

    def __init__(self, master):
        self.master = master
        self.master.title("Choose platform")
        self.master.geometry("300x150")

        self.HH_button = tk.Button(master, text="HeadHunter", command=self.head_hunter)
        self.HH_button.pack()

        self.SJ_button = tk.Button(master, text="SuperJob", command=self.super_job)
        self.SJ_button.pack()

        self.both_button = tk.Button(master, text="HeadHunter\nand\nSuperJob", command=self.both)
        self.both_button.pack()

    def head_hunter(self):
        print(job_name, job_salary, job_count)
        vacancies = self.hh_site.get_vacancies(job_name, job_salary, job_count)
        hh_vacancies = self.hh_site.parse(vacancies)

        if len(hh_vacancies) > 0:
            messagebox.showinfo("Nice!", {get_top_vac(hh_vacancies)})
            save_vacancies(hh_vacancies)
        else:
            messagebox.showerror("Fail(", "Job search failed")

    def super_job(self):
        vacancies = self.sj_site.get_vacancies(job_name, job_salary, job_count)
        sj_vacancies = self.sj_site.parse(vacancies)

        if len(sj_vacancies) > 0:
            messagebox.showinfo("Nice!", {get_top_vac(sj_vacancies)})
            save_vacancies(sj_vacancies)
        else:
            messagebox.showerror("Fail(", "Job search failed")

    def both(self):
        vacancies = self.hh_site.get_vacancies(job_name, job_salary, job_count)
        hh_vacancies = self.hh_site.parse(vacancies)

        vacancies = self.sj_site.get_vacancies(job_name, job_salary, job_count)
        sj_vacancies = self.sj_site.parse(vacancies)

        all_vacancies = hh_vacancies + sj_vacancies
        if len(all_vacancies) > 0:
            messagebox.showinfo("Nice!", "Job search completed successfully")
            return all_vacancies
        else:
            messagebox.showerror("Fail(", "Job search failed")




if __name__ == '__main__':
    root = tk.Tk()
    FirstWindow(root)
    root.mainloop()
