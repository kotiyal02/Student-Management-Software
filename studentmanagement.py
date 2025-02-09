from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class student:
    def readData(self,root):
        # creating a label for heading
        self.L=Label(root,text='STUDENT MANAGEMENT SYSTEM',font=('arial',30,'bold','underline'),border=10,bg='lightgreen',relief=GROOVE)
        self.L.pack(side=TOP,fill=X)
        
        # creating frame for  students details
        self.details=LabelFrame(root,text='Enter Details',font=('arial',20),relief=GROOVE,bg='grey',border=8)
        self.details.place(x=10,y=75,height=580,width=400)

         # creating frame for  details
        self.adddetails=LabelFrame(root,relief=GROOVE,bg='grey',border=8)
        self.adddetails.place(x=440,y=75,height=580,width=820)

        # crreating label for entry box name
        self.name=Label(self.details,text='NAME',bg='grey',fg='black',font=('arial',18))
        self.name.place(x=17,y=10)
        self.rollno=Label(self.details,text='Roll no.',bg='grey',fg='black',font=('arial',18))
        self.rollno.place(x=17,y=50)
        self.course=Label(self.details,text='COURSE',bg='grey',fg='black',font=('arial',18))
        self.course.place(x=10,y=90)
        self.semester=Label(self.details,text='SEMSTER',bg='grey',fg='black',font=('arial',18))
        self.semester.place(x=10,y=130)
        self.gender=Label(self.details,text='GENDER',bg='grey',fg='black',font=('arial',18))
        self.gender.place(x=10,y=170)
        self.contact=Label(self.details,text='MOB NO.',bg='grey',fg='black',font=('arial',18))
        self.contact.place(x=10,y=210)
        self.dob=Label(self.details,text='D.O.B.',bg='grey',fg='black',font=('arial',15))
        self.dob.place(x=17,y=250)
        self.fathername=Label(self.details,text="FATHER NAME",bg='grey',fg='black',font=('arial',15))
        self.fathername.place(x=10,y=290)
       
        self.address=Label(self.details,text='ADDRESS',bg='grey',fg='black',font=('arial',15))
        self.address.place(x=10,y=330)

        # creating variable 
        self.namevar=StringVar()
        self.rollnovar=StringVar()
        self.coursevar=StringVar()
        self.semestervar=StringVar()
        self.gendervar=StringVar()
        self.contactvar=StringVar()
        self.dobvar=StringVar()
        self.fathervar=StringVar()
        self.addressvar=StringVar()
        self.searchdatavar=StringVar()

        # creating  entry box for entering details..
        self.name=Entry(self.details,border=7,font=('arial',12),textvariable=self.namevar)
        self.name.place(x=165,y=5)
        self.rollno=Entry(self.details,border=7,font=('arial',12),textvariable=self.rollnovar)
        self.rollno.place(x=165,y=45)
        self.course=Entry(self.details,border=7,font=('arial',12),textvariable=self.coursevar)
        self.course.place(x=165,y=85)
        self.semester=Entry(self.details,border=7,font=('arial',12),textvariable=self.semestervar)
        self.semester.place(x=165,y=125)
        self.gender=ttk.Combobox(self.details,values=("Gender","Male","Female","Other"),font=('arial',17),textvariable=self.gendervar,width=13,state="readonly")
        self.gender.current(0)
        self.gender.place(x=165,y=165)
        self.contact=Entry(self.details,border=7,font=('arial',12),textvariable=self.contactvar)
        self.contact.place(x=165,y=205)
        self.dob=Entry(self.details,border=7,font=('arial',12),textvariable=self.dobvar)
        self.dob.place(x=165,y=245)
        self.father=Entry(self.details,border=7,font=('arial',12),textvariable=self.fathervar)
        self.father.place(x=165,y=285)
        self.address=Entry(self.details,width=20,border=7,font=('arial'),textvariable=self.addressvar)
        self.address.place(x=165,y=325)

        # creating function for connecting database
        def fetch_data():
            conn= mysql.connector.connect(host='localhost',user='root',password='H@rshukotiyal123',database='studentmanagement')
            curr=conn.cursor()
            curr.execute(' select * from details')
            rows=curr.fetchall()
            if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('',END,values=row)
                conn.commit()
                conn.close()

        def add_fun():
            if self.namevar.get()=='' or self.rollnovar.get()=='' or self.contactvar.get()=='':
                messagebox.showerror("ERROR!","Please fill all the fields")
            else:
                conn= mysql.connector.connect(host='localhost',user='root',password='H@rshukotiyal123',
                database='studentmanagement')
                curr=conn.cursor()

                curr.execute('SELECT * FROM details WHERE rollno = %s', (self.rollnovar.get(),))
                existing_record = curr.fetchone()

                if existing_record:
                  messagebox.showerror("ERROR!", "Roll number already exists. Please enter a unique roll number.")
                  conn.close()
                elif not self.contactvar.get().isdigit() or len(self.contactvar.get()) != 10:
                     messagebox.showerror("ERROR!", "Contact number must be exactly 10 digits and contain only numbers.")
                else:
                    curr.execute('INSERT INTO details(studentname, rollno, course, semester, gender, contact, dob, fathername, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (self.namevar.get(), self.rollnovar.get(), self.coursevar.get(), self.semestervar.get(), self.gendervar.get(),
                    self.contactvar.get(), self.dobvar.get(), self.fathervar.get(), self.addressvar.get()))

                conn.commit()
                conn.close()

                fetch_data() # this will show data after add 
        
        def get_cursor(EVENT):
            """thie function will fetch data of selected rows"""
            cursor_row= self.student_table.focus()
            content=self.student_table.item(cursor_row)
            row=content['values']
            self.namevar.set(row[0])
            self.rollnovar.set(row[1])
            self.coursevar.set(row[2])
            self.semestervar.set(row[3])
            self.gendervar.set(row[4])
            self.contactvar.set(row[5])
            self.dobvar.set(row[6])
            self.fathervar.set(row[7])
            self.addressvar.set(row[8])

        def clear_fun():
            """this function will clear the entryboxx"""
            self.namevar.set('')
            self.rollnovar.set('')
            self.coursevar.set('')
            self.semestervar.set('')
            self.gendervar.set('')
            self.contactvar.set('')
            self.dobvar.set('')
            self.fathervar.set('')
            self.addressvar.set('')

        def update_fun():
            """this function will update the data acoording to user"""
            conn= mysql.connector.connect(host='localhost',user='root',password='H@rshukotiyal123',database='studentmanagement')
            curr=conn.cursor()
            curr.execute('''UPDATE details 
                    SET studentname=%s, course=%s, semester=%s, gender=%s, contact=%s, dob=%s, fathername=%s, address=%s
                    WHERE rollno=%s''', 
                    (self.namevar.get(), self.coursevar.get(), self.semestervar.get(), self.gendervar.get(),
                    self.contactvar.get(), self.dobvar.get(), self.fathervar.get(), self.addressvar.get(), self.rollnovar.get()))

            conn.commit()
            fetch_data()
            conn.close()
            
        def delete_fun():
            """this will delete data according to user"""
            if self.rollnovar.get()=='':
                messagebox.showerror("ERROR!","Please select a student to delete")
            else:
                conn= mysql.connector.connect(host='localhost',user='root',password='H@rshukotiyal123',database='studentmanagement')
                curr=conn.cursor()
                curr.execute('DELETE from details where rollno=%s', (self.rollnovar.get(),))

                conn.commit()
                conn.close()

                fetch_data()

        def search_fun():
            """Searches the student details based on user input"""
            search_by = self.searchdatavar.get()
            search_value = self.searchdataentry.get().strip()  
            if search_by == "Search By" or not search_value:
                messagebox.showerror("Error", "Please select a valid search category and enter a search term.")
                return

            query = ""
            params = ()

            if search_by == "Name":
                query = "SELECT * FROM details WHERE studentname LIKE %s"
                params = (f"%{search_value}%",)
            elif search_by == "Roll no.":
                query = "SELECT * FROM details WHERE rollno = %s"
                params = (search_value,)
            elif search_by == "Contact":
                query = "SELECT * FROM details WHERE contact = %s"
                params = (search_value,)

            try:
                conn = mysql.connector.connect(host='localhost',user='root',password='H@rshukotiyal123',database='studentmanagement')

                curr = conn.cursor()
                curr.execute(query, params)
                rows = curr.fetchall()

                self.student_table.delete(*self.student_table.get_children())  # Clear existing data
                for row in rows:
                    self.student_table.insert('', END, values=row)

                if not rows:
                    messagebox.showinfo("No Results", "No matching records found.")

            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
            
            finally:
                conn.close()

        def showall_fun():
            fetch_data()
        
        # creating frame for buttons
        self.btnframe=Frame(self.details,bg='grey',border=10,relief=GROOVE)
        self.btnframe.place(x=40,y=420,height=110,width=300)

        # creating button
        self.add=Button(self.btnframe,text='ADD',bg='lightgrey',border=7,font=('arial',10,'bold'),width=14,command=add_fun)
        self.add.grid(row=0,column=0,padx=3,pady=3)
        self.update=Button(self.btnframe,text='UPDATE',bg='lightgrey',border=7,font=('arial',10,'bold'),width=14,command=update_fun)
        self.update.grid(row=0,column=1,padx=3,pady=3)
        self.delete=Button(self.btnframe,text='DELETE',bg='lightgrey',border=7,font=('arial',10,'bold'),width=14,command=delete_fun)
        self.delete.grid(row=1,column=0,padx=4,pady=3)
        self.clear=Button(self.btnframe,text='CLEAR',bg='lightgrey',border=7,font=('arial',10,'bold'),width=14,command=clear_fun)
        self.clear.grid(row=1,column=1,padx=4,pady=3)

        # creating frame for search labels
        self.searchframe=Frame(self.adddetails,bg='grey',border=10,relief=GROOVE)
        self.searchframe.pack(side=TOP,fill=X)

        # creating search label 
        self.searchlabel=Label(self.searchframe,text='Search',bg='grey',fg='black',font=('arial',14))
        self.searchlabel.grid(row=0,column=0,padx=2,pady=2)

        # creating search box
        self.searchdata=ttk.Combobox(self.searchframe,values=("Search By","Name","Roll no.","Contact"),font=('arial',13),textvariable=self.searchdatavar,width=16,state="readonly")
        self.searchdata.current(0)
        self.searchdata.grid(row=0,column=1,padx=4,pady=2)

        self.searchdataentry = Entry(self.searchframe, font=('arial', 15), width=18, border=5)
        self.searchdataentry.grid(row=0, column=2, padx=4, pady=2)

        self.searchbtn=Button( self.searchframe,text='Search',width=12,bg='lightgrey',border=8,font=('arial',12),command=search_fun)
        self.searchbtn.grid(row=0,column=3,padx=3,pady=2)
        self.showall=Button( self.searchframe,text='Show All',width=12,bg='lightgrey',border=8,font=('arial',12),command=showall_fun)
        self.showall.grid(row=0,column=4,padx=6,pady=2)

        # creating frame for showing student detail
        self.showDetails=Frame(self.adddetails,bg='grey',border=10,relief=GROOVE,height=500,width=800)
        self.showDetails.pack(fill=BOTH,expand=True)

        # creating scroll bar
        self.scroll_x= Scrollbar(self.showDetails,orient=HORIZONTAL)
        self.scroll_y= Scrollbar(self.showDetails,orient=VERTICAL)

        self.student_table= ttk.Treeview(self.showDetails,columns=("Name","Roll no.","Course",
        "Semester","Gender","Contact","D.O.B","Father's name","Address"))

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT,fill=Y)

        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Roll no.",text="Roll no.")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Contact",text="Contact")
        self.student_table.heading("D.O.B",text="D.O.B")
        self.student_table.heading("Father's name",text="Father's name")
        self.student_table.heading("Address",text="Address")

        self.student_table.column("Name",width=100)
        self.student_table.column("Roll no.",width=90)
        self.student_table.column("Course",width=90)
        self.student_table.column("Semester",width=70)
        self.student_table.column("Gender",width=60)
        self.student_table.column("Contact",width=90)
        self.student_table.column("D.O.B",width=80)
        self.student_table.column("Father's name",width=100)
        self.student_table.column("Address",width=140)

        self.student_table['show']='headings'
        self.student_table.pack(fill=BOTH,expand=True)

        fetch_data()

        self.student_table.bind("<ButtonRelease-1>",get_cursor)
        pass
        


#__MAIN__
root=Tk()
root.geometry("1350x750")
root.title("Student Management System")
ob=student()
ob.readData(root)

root.mainloop()
