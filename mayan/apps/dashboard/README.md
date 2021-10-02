Manual Testing Script and Documentation

1. Navigate to the Dashboard Tab once you have reached the home page of Mayan EDMS
2. You will see two buttons; one for Candidates and one for Reviewers
3. To review candidate data, access the table by clicking on the Candidates tab, then clicking on the Candidate Data tab
4. To review a summary of the Candidate data and statistics, click on the Candidate Statistics tab
5. There you should find a button that says 'Click for Graph'. If you click on this button, you should should see the graph load in your same tab. To go back, hit the back button on your browser.
6. Under the button, you should find that the average GPA among candidates is 2.59
7. To review reviewer data, acess the table by clicking on the Reviwers tab, then clicking on the Reviewer Data tab
8. To review a summary of the Reviewer statistics, click on the Reviwer Statistics tab
9. You should find that the average techincal score given is 6.08, the average essay score given is 6.68, and then average inteview score given is 5.15
10. Try adding another candidate by adding an element to the candidate_data (found in dashboard/views.py) in the form of a list describing [name, gpa, gre score, years of work experience, skills] 
11. Also try adding another reviewer by adding an element to the reviewer_data (found in dashboard/views.py) in the form of a list describing [name, average tech score, average essay score, average interview score] 
12. These changes should be present in the candidate and reviewer sections when the website is reran, also effecting the average scores reported.
