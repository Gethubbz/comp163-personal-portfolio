
from collections import namedtuple
import math
student_name="Jordan Smith"
student_email="jsmith@ncat.edu"
student_home="Charlotte, NC"
student_graduate= "Spring 2028"
student_major= "Computer Science"
course_list=["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses=["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hrs=[3, 3, 3, 3]
GPA_hist=[ 3.2, 3.6, 3.4, 3.7]
GPA_avg=(GPA_hist[0] + GPA_hist[1] + GPA_hist[2] + GPA_hist[3])/4
credit_avg=(3 * len(credit_hrs))

class_list={"COMP 163": 3,
"MATH 150": 3,
"ENG 101": 3,
"HIS 105": 3}


Current_Skills={'Time management', 'Photography', 'Problem solving', 'HTML', 'Python basics'}
Learning_Goals={'Data structures', 'Web design', 'JavaScript', 'Git', 'Public speaking'}
Career_Interests= {'Software development', 'Game development', 'Web development', 'Data science'}
Hobbies_had={"Gaming", "Photography", "Reading", "Soccer", "Music"}
Entertain_backlog={"One Piece", "Barry", "Life", "Incantation", "Memento"}


professors_dictionary={
   "COMP 163": "Prof. Rhodes",
   "MATH 150": "Dr. Lee",
   "ENG 101": "Dr. Martinez",
   "HIS 105": "Dr. Brown"
}


Course_dictionary={
"COMP 163": "M-Eric 300",
"MATH 150": "Marteena 201",
 "ENG 101": "Crosby 121",
"HIS 105": "Crosby 210"
}


Monthly_budget={
"Food":450,
"Entertainment": 200,
"Books": 125,
"Transportation": 100
}


Study_hrs={
"Programming": 10,
"Math": 8,
 "English": 4,
"History": 3
}

Contact_dictionary= {"Mom": "704-555-0199",
"Roommate": "336-555- 7821",
"Academic Advisor": "336-334-5000"}


study_avg= Study_hrs["Programming"] + Study_hrs["Math"] + Study_hrs["English"] + Study_hrs["History"]


budgit_added= Monthly_budget["Food"] + Monthly_budget["Entertainment"] + Monthly_budget["Books"] + Monthly_budget["Transportation"]
#wanted to use a namedtuple to be creative, but using tuple=("","","","")
Emergency= namedtuple("Mom",["Name","Number"])
Emergency_tuple= Emergency("Hannah Smith (Mom)","704-555-0199")
Home= namedtuple("Street",["address","state","AreaCode"])
Home_address= Home("456 Oak Street", "Charlotte", "NC 28202")
SocialMedia= namedtuple("Media",["Followers","PlatNums"])
Social_Tuple= SocialMedia("439","2")
KeyContact=namedtuple("Contact",["people"])
Key_Tuple=KeyContact("3")
print("================================================================")
print("                              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print(f"Student: {student_name} | Email: {student_email}")
print(f"From: {student_home} | Graduating: {student_graduate}")
print(f"Major: {student_major}")
print("")
print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {credit_avg} credits across {len(credit_hrs)} courses")
print(f"Cumulative GPA: {GPA_avg:.2f}")
print(f"Weekly Study Time: {study_avg} hours")
# it says per hour so I had to reduce it as it was seen as credit hours + study hours per week
print(f"Academic Investment: ${float(math.floor((study_avg + credit_avg)/7))} per study hour")
print("")
print("Current Courses:")
print("")
print(f"{course_list[0]} - {class_list['COMP 163']} credits - {professors_dictionary['COMP 163']} - {Course_dictionary['COMP 163']}")
print(f"{course_list[1]} - {class_list['MATH 150']} credits - {professors_dictionary['MATH 150']} - {Course_dictionary['MATH 150']}")
print(f"{course_list[2]} - {class_list['ENG 101']} credits - {professors_dictionary['ENG 101']} - {Course_dictionary['ENG 101']}")
print(f"{course_list[3]} - {class_list['HIS 105']} credits - {professors_dictionary['HIS 105']} - {Course_dictionary['HIS 105']}")
print("")
print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {Current_Skills}")
print(f"Learning Goals: {Learning_Goals}")
print(f"Career Interests: {Career_Interests}")
print(f"Skills Currently Have: {len(Hobbies_had)}")
print(f"Skills Want to Learn: {len(Entertain_backlog)}")
print("")
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${ budgit_added}")
print(f"Food: ${Monthly_budget['Food']} (${Monthly_budget['Food']/30}/day)")
print(f"Entertainment: ${Monthly_budget['Entertainment']}")
print(f"Books: ${Monthly_budget['Books']}")
print(f"Transportation: ${Monthly_budget['Transportation']}")
print(f"Annual Projection: ${budgit_added * 12}")
print("")
print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {Emergency_tuple[0]} - {Emergency_tuple[1]}")
print(f"Home Address: {Home_address[0]}, {Home_address[1]}, {Home_address[2]}")
print(f"Social Media Presence: {Social_Tuple[0]} followers across {Social_Tuple[1]} platforms ")
print(f"Key Contacts: {Key_Tuple[0]} people in directory")
print("")
print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {len(completed_courses)}")
print(f"Current Academic Load: {study_avg + credit_avg} weekly commitments")
print(f"Entertainment Backlog: {len(Entertain_backlog)} items")
print(f"Current Hobbies: {len(Hobbies_had)} activities")
print("================================================================")

#AI CITATION: ON THURSDAY SEPTERMBER 18th, I aksed Ai what was the issue with my code, stating:"Im getting an error in my code saying theres an "Unmatched: [" can you find it?" where it found my error!
