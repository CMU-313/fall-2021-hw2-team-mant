from django.views import View
from django.shortcuts import render

class DashboardListView(View):

    def get(self, request, *args, **kwargs):
        candidate_data = [
            ["Teddy Liang", "2.93", "320", "1", "Java, C++, Python"],
            ["Nicholas Clark", "3.87", "280", "2.5", "Python"],
            ["Megna Kokkalera", "2.64", "270", "3", "Python, SQL"],
            ["Anagha Srikumar", "0.66", "700", "1", "Java, C, Ruby"],
            ["Michael Hilton", "2.77", "210", "2", "Java, C++, Python"],
            ["Rohan Padhye", "2.61", "420", "3", "Ruby, C, Python"],
            ["Victor Huang", "3.84", "840", "2.5", "Java, C++"],
            ["Bob Jones", "3.46", "870", "2.5", "Java, C++, Python"],
            ["Dave Scott", "1.17", "870", "3.5", "SQL"],
            ["John Smith", "1.98", "720", "0", "C"],
        ]

        reviewer_data = [
            ["Nathan Zhu", "6.7", "7.4", "5.0"],
            ["Shawn Noronha", "8.4", "3.5", "8.6"],
            ["Sebastian Andreu", "2.9", "9.5", "4.4"],
            ["Vishal Saikrishnan", "6.6", "3.7", "1.3"],
            ["Oscar Wilcox", "7.3", "7.1", "8.1"],
            ["Casper Wong", "4.6", "8.9", "3.5"],
        ]

        average_gpa = 0
        average_gre = 0
        average_work_experience = 0
        common_skills = {}
        
        for candidate in candidate_data:
            average_gpa += float(candidate[1])
            average_gre += float(candidate[2])
            average_work_experience += float(candidate[3])
            for skill in candidate[4].split(', '):
                if skill in common_skills:
                    common_skills[skill] += 1
                else:
                    common_skills[skill] = 1

        average_tech_score = 0
        average_essay_score = 0
        average_interview_score = 0

        for reviewer in reviewer_data:
            average_tech_score += float(reviewer[1])
            average_essay_score += float(reviewer[2])
            average_interview_score += float(reviewer[3])

        average_gpa /= len(candidate_data)
        average_gre /= len(candidate_data)
        average_work_experience /= len(candidate_data)
        average_gpa = round(average_gpa, 2)
        average_gre = round(average_gre, 2)
        average_work_experience = round(average_work_experience, 2)

        average_tech_score /= len(reviewer_data)
        average_essay_score /= len(reviewer_data)
        average_interview_score /= len(reviewer_data)
        average_tech_score = round(average_tech_score, 2)
        average_essay_score = round(average_essay_score, 2)
        average_interview_score = round(average_interview_score, 2)

        most_common_skills = []
        for val in sorted(common_skills.values(), reverse=True):
            for key in common_skills.keys():
                if common_skills[key] == val:
                    skill = []
                    skill.append(key)
                    skill.append(common_skills[key])
                    most_common_skills.append(skill)
            if len(most_common_skills) >= 3:
                break

        context = {}

        context["candidate_data"] = candidate_data
        context["reviewer_data"] = reviewer_data
        context["average_gpa"] = average_gpa
        context["average_gre"] = average_gre
        context["average_work_experience"] = average_work_experience
        context["average_tech_score"] = average_tech_score
        context["average_essay_score"] = average_essay_score
        context["average_interview_score"] = average_interview_score
        context["most_common_skills"] = most_common_skills

        return render(request, "test.html", context)