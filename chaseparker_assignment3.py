from collections import namedtuple
import math
#changed the old date about Jordan Smith, and made it about me reguarding my email,name,graduation date,major,etc
student_name="Chase Parker"
student_email="ceparker@aggies.ncat.edu"
student_home="Fort Mill, SC"
student_graduate= "Spring 2029"
student_major= "Computer Science"
# Updated my classes by either changing the type of subject (Math 150 --> 110) or compleatly adding a new class like Freshman studies 101
course_list=["COMP 163", "MATH 110", "ENG 100", "HIS 106","Eng 111","Freshman Studies 101"]
#Since im a freshman, i added the only two classes I have  "College Credit for"
completed_courses=["Ap Calc", "Ap Bio"]
#Adding hours of all classes
credit_hrs=[3,4, 3, 3, 1,1]
#Using predicted GPA standings for each 6 classes
GPA_hist=[ 3.5, 3.6, 3.6, 3.7,3.8,3.6]
GPA_avg=(GPA_hist[0] + GPA_hist[1] + GPA_hist[2] + GPA_hist[3])/4
credit_avg=(3 * len(credit_hrs))

class_list={"COMP 163": 3,
#adding and updating my classes and their respectable credits
"MATH 110": 3,
"ENG 100": 3,
"HIS 106": 3,
"Eng 111": 1,
"Freshman Studies 101": 1
}

#Simply updating my skills,hobbies, and entertainment system
Current_Skills={'Time management', 'CSS', 'Problem solving', 'HTML', 'Python basics'}
Learning_Goals={'Data structures', 'Web design', 'JavaScript', 'Git', 'Public speaking'}
Career_Interests= {'Software development', 'Game development', 'Web development', 'Enviornmental science'}
Hobbies_had={"Gaming", "Coding", "Reading", "Swimming", "Music"}
Entertain_backlog={"One Piece", "Marvel", "DC", "Horror Films", "Sleep"}

#Adding the correct professor names to it
professors_dictionary={
   "COMP 163": "Prof. Rhodes",
   "MATH 110": "Dr. Johnson",
  "ENG 100": "Prof. Harper",
  "HIS 106": "Prof. Devoe",
  "Eng 111": "Prof. Parrish",
  "Freshman Studies 101": "Prof. Barrow"

}



#Adding the correct classroom names to it
Course_dictionary={
"COMP 163": "Gibbs 337",
"MATH 110": "Marteena 216",
"ENG 100": "ONLINE",
"HIS 106": "ONLINE",
"Eng 111": "McNair 240",
"Freshman Studies 101": "ONLINE"
}



#Updating how much I monthy spend of books,Food,Etertainment,Transportation monthly
Monthly_budget={

"Food":120,
"Entertainment": 50,
"Books": 25,
"Transportation": 50
}



#Showing my relaistic study hour sfor my classes
Study_hrs={
"Programming": 5,
"Math": 3,
"English": 1,
"History": 2,
"Engineering": 1,
"College Success": 1


}

#Just updating my name and my,my roomates, and advisors "numbers"
Contact_dictionary= {"Chase": "704-555-0199",
"Roommate": "336-555- 7821",
"Academic Advisor": "336-334-5000"}



#adding extra to the study_avg due to more classes being added
study_avg= Study_hrs["Programming"] + Study_hrs["Math"] + Study_hrs["English"] + Study_hrs["History"] + Study_hrs["Engineering"] + Study_hrs["College Success"]




budgit_added= Monthly_budget["Food"] + Monthly_budget["Entertainment"] + Monthly_budget["Books"] + Monthly_budget["Transportation"]
#wanted to use a namedtuple to be creative, but using tuple=("","","","")
Emergency= namedtuple("Mom",["Name","Number"])
Emergency_tuple= Emergency("Angela Parker (Mom)","704-555-0199")
Home= namedtuple("Street",["address","state","AreaCode"])
Home_address= Home("456 Oak Street", "Fort Mill", "SC 28202")
SocialMedia= namedtuple("Media",["Followers","PlatNums"])
Social_Tuple= SocialMedia("55","2")
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
#simply updating the indexing base don the correct classes with extra prints for the 2 extra classes
print(f"{course_list[0]} - {class_list['COMP 163']} credits - {professors_dictionary['COMP 163']} - {Course_dictionary['COMP 163']}")
print(f"{course_list[1]} - {class_list['MATH 110']} credits - {professors_dictionary['MATH 110']} - {Course_dictionary['MATH 110']}")
print(f"{course_list[2]} - {class_list['ENG 100']} credits - {professors_dictionary['ENG 100']} - {Course_dictionary['ENG 100']}")
print(f"{course_list[3]} - {class_list['HIS 106']} credits - {professors_dictionary['HIS 106']} - {Course_dictionary['HIS 106']}")
print(f"{course_list[4]} - {class_list['Eng 111']} credits - {professors_dictionary['Eng 111']} - {Course_dictionary['Eng 111']}")
print(f"{course_list[5]} - {class_list['Freshman Studies 101']} credits - {professors_dictionary['Freshman Studies 101']} - {Course_dictionary['Freshman Studies 101']}")
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

#AI CITATION: ON THURSDAY SEPTERMBER 18th, I aksed Ai what was the issue with my code, stating:"Im getting an error in my code saying theres an "Unmatched: [" can you find it?" where it found my error!
