Manual Testing Script and Documentation

1. Navigate to the Dashboard Tab once you have reached the home page of Mayan EDMS
2. You will see two buttons; one for Candidates and one for Reviewers
3. To review candidate data, access the table by clicking on the Candidates tab, then clicking on the Candidate Data tab
4. To review a summary of the Candidate data and statistics, click on the Candidate Statistics tab
5. You should find that the average GPA among candidates is 2.59
6. To review reviewer data, acess the table by clicking on the Reviwers tab, then clicking on the Reviewer Data tab
7. To review a summary of the Reviewer statistics, click ont he Reviwer Statistics tab
8. You should find that the average techincal score given is 6.08, the average essay score given is 6.68, and then average inteview score given is 5.15
9. Try adding another candidate by adding an element to the candidate_data (found in dashboard/views.py) in the form of a list describing [name, gpa, gre score, years of work experience, skills] 
10. Also try adding another reviewer by adding an element to the reviewer_data (found in dashboard/views.py) in the form of a list describing [name, average tech score, average essay score, average interview score] 
11. These changes should be present in the candidate and reviewer sections when the website is reran, also effecting the average scores reported.
