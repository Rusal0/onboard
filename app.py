import streamlit as st
from datetime import datetime, timedelta

# Onboarding Data with contact persons and descriptions
onboarding_plan = {
    "Week 1": {
        "Day 1": {
            "Morning": [
                {
                    "activity": "Welcome Breakfast with the Team",
                    "contact": "John Doe",
                    "description": "Join us for a welcome breakfast to kick off your onboarding experience! This informal gathering is designed to introduce you to your new team members and help you build connections in a relaxed setting. Enjoy delicious food while engaging in light conversations about your roles, interests, and shared goals. This event aims to foster teamwork and open communication, ensuring you feel welcomed and valued as part of our organization."
                },
                {"activity": "Introduction to the Company Culture and Values", "contact": "Jane Smith", "description": "An overview of the company culture and core values that guide our work."},
                {"activity": "Overview of the Localization Department", "contact": "Emily Johnson", "description": "Introduction to the Localization Department, its goals, and how it fits into the company."}
            ],
            "Afternoon": [
                {"activity": "Office Tour and Meet Key Stakeholders", "contact": "Michael Brown", "description": "A guided tour of the office to meet key stakeholders."},
                {"activity": "Introduction to the Onboarding Buddy (a peer mentor)", "contact": "Chris Davis", "description": "Meet your onboarding buddy who will guide you through the onboarding process."},
                {"activity": "Setting up Workstation and Tools", "contact": "Patricia Garcia", "description": "Assistance with setting up your workstation and tools for work."}
            ]
        },
        "Day 2": {
            "Morning": [
                {"activity": "Deep Dive into the Job Description and Expectations", "contact": "Robert Martinez", "description": "A detailed overview of your job description and performance expectations."},
                {"activity": "Interactive Workshop: Role-Playing Key Responsibilities", "contact": "Linda Robinson", "description": "Engage in role-playing scenarios to understand your key responsibilities."}
            ],
            "Afternoon": [
                {"activity": "Meeting with Direct Supervisor to Discuss Performance Metrics", "contact": "David Clark", "description": "Discussion with your supervisor on performance metrics and goals."},
                {"activity": "Collaborative Session: Setting Personal Goals for the First 30 Days", "contact": "Barbara Rodriguez", "description": "Set personal goals for your first 30 days in collaboration with your supervisor."}
            ]
        },
        "Day 3": {
            "Morning": [
                {"activity": "Hands-On Training: Project Management Software", "contact": "James Lewis", "description": "Training session on using the project management software."},
                {"activity": "Interactive Webinar: Localization Workflow Tools", "contact": "Mary Lee", "description": "Webinar on tools used in the localization workflow."}
            ],
            "Afternoon": [
                {"activity": "Case Study Review: Successful Past Projects", "contact": "William Walker", "description": "Review case studies of successful projects in the past."},
                {"activity": "Q&A Session with IT Support for Troubleshooting", "contact": "Lisa Hall", "description": "Q&A session with IT support to troubleshoot any technical issues."}
            ]
        },
        "Day 4": {
            "Morning": [
                {"activity": "Client Portfolio Overview: Key Clients and Projects", "contact": "Mark Allen", "description": "Overview of key clients and ongoing projects."},
                {"activity": "Interactive Session: Understanding Client Requirements", "contact": "Nancy Young", "description": "Interactive session on understanding client needs."}
            ],
            "Afternoon": [
                {"activity": "Workshop: Developing Client-Specific Strategies", "contact": "Steven King", "description": "Workshop on developing strategies tailored to specific clients."},
                {"activity": "Role-Playing: Mock Client Meetings", "contact": "Karen Wright", "description": "Role-play sessions to simulate client meetings."}
            ]
        },
        "Day 5": {
            "Morning": [
                {"activity": "Team Building Activities", "contact": "Brian Scott", "description": "Participate in team-building activities to foster connections."},
                {"activity": "Networking Lunch with Cross-Functional Teams", "contact": "Sandra Green", "description": "Lunch opportunity to network with teams from other departments."}
            ],
            "Afternoon": [
                {"activity": "Feedback Session: First Week Review with Onboarding Buddy", "contact": "Kevin Adams", "description": "Review your first week with your onboarding buddy."},
                {"activity": "Planning for the Upcoming Week", "contact": "Megan Baker", "description": "Planning and setting goals for the upcoming week."}
            ]
        }
    },
    "Week 2": {
        "Day 6": {
            "Morning": [
                {"activity": "Workshop: Understanding Revenue and Profit Growth", "contact": "Michael Brown", "description": "Workshop on understanding revenue streams and profit growth strategies."},
                {"activity": "Interactive Budgeting Exercise", "contact": "James Lewis", "description": "Hands-on budgeting exercise to learn financial planning."}
            ],
            "Afternoon": [
                {"activity": "Case Study: Financial Reporting and Forecasting", "contact": "Linda Robinson", "description": "Analysis of a case study focusing on financial reporting."},
                {"activity": "Meeting with Finance Team for Q&A", "contact": "Barbara Rodriguez", "description": "Q&A session with the finance team to clarify financial processes."}
            ]
        },
        "Day 7": {
            "Morning": [
                {"activity": "Interactive Session: Workflow Management Best Practices", "contact": "Emily Johnson", "description": "Learn best practices for managing workflows efficiently."},
                {"activity": "Simulation: Managing a Complex Localization Project", "contact": "David Clark", "description": "Simulation exercise on handling a complex project."}
            ],
            "Afternoon": [
                {"activity": "Workshop: Continuous Improvement Strategies", "contact": "Patricia Garcia", "description": "Workshop on strategies for continuous improvement."},
                {"activity": "Collaborative Session: Identifying Operational Bottlenecks", "contact": "Chris Davis", "description": "Collaborate to identify and solve operational issues."}
            ]
        },
        "Day 8": {
            "Morning": [
                {"activity": "Interactive Workshop: Client Communication and Consultancy", "contact": "John Doe", "description": "Workshop focusing on effective client communication."},
                {"activity": "Role-Playing: Client Interaction Scenarios", "contact": "Jane Smith", "description": "Role-playing exercises on client interactions."}
            ],
            "Afternoon": [
                {"activity": "Case Study: Successful Client Management", "contact": "Michael Brown", "description": "Analyze successful client management cases."},
                {"activity": "Meeting with Sales Team for Collaboration Strategies", "contact": "Emily Johnson", "description": "Discussion on collaboration strategies with the sales team."}
            ]
        },
        "Day 9": {
            "Morning": [
                {"activity": "Training: KPI Management and Reporting", "contact": "James Lewis", "description": "Training on how to manage and report on key performance indicators."},
                {"activity": "Interactive Session: Using Data to Drive Decisions", "contact": "David Clark", "description": "Learn to utilize data for informed decision-making."}
            ],
            "Afternoon": [
                {"activity": "Collaborative Workshop: Developing a KPI Dashboard", "contact": "Patricia Garcia", "description": "Create a KPI dashboard collaboratively."},
                {"activity": "Review Session with Direct Supervisor", "contact": "Chris Davis", "description": "Review your progress with your direct supervisor."}
            ]
        },
        "Day 10": {
            "Morning": [
                {"activity": "One-on-One Feedback Session with Onboarding Buddy", "contact": "John Doe", "description": "Feedback session with your onboarding buddy."},
                {"activity": "Team Feedback Session: Sharing Insights and Improvements", "contact": "Jane Smith", "description": "Team session to share insights and suggest improvements."}
            ],
            "Afternoon": [
                {"activity": "Personal Reflection and Goal Adjustment", "contact": "Michael Brown", "description": "Reflect on your first two weeks and adjust goals."},
                {"activity": "Planning for the Upcoming Week", "contact": "Emily Johnson", "description": "Set goals and plans for the next week."}
            ]
        }
    },
    "Week 3": {
        "Day 11": {
            "Morning": [
                {"activity": "Leadership Workshop: Leading Project Managers", "contact": "Linda Robinson", "description": "Workshop on leadership skills for project managers."},
                {"activity": "Role-Playing: Leadership Scenarios", "contact": "Barbara Rodriguez", "description": "Role-play various leadership scenarios."}
            ],
            "Afternoon": [
                {"activity": "Mentorship Session with Senior Leaders", "contact": "David Clark", "description": "Session with senior leaders to gain insights."},
                {"activity": "Collaborative Session: Developing Leadership Skills", "contact": "Patricia Garcia", "description": "Collaborative exercises to develop leadership skills."}
            ]
        },
        "Day 12": {
            "Morning": [
                {"activity": "Interactive Session: Best Practices in Global Partnership", "contact": "Chris Davis", "description": "Learn about best practices for global partnerships."},
                {"activity": "Case Study: Successful Partnerships", "contact": "John Doe", "description": "Analyze successful global partnerships."}
            ],
            "Afternoon": [
                {"activity": "Workshop: Creating and Managing Partnerships", "contact": "Jane Smith", "description": "Workshop on creating and managing partnerships."},
                {"activity": "Networking Event with Global Partners", "contact": "Michael Brown", "description": "Opportunity to network with global partners."}
            ]
        },
        "Day 13": {
            "Morning": [
                {"activity": "Training: Effective Stakeholder Management", "contact": "James Lewis", "description": "Training on managing stakeholders effectively."},
                {"activity": "Simulation: Stakeholder Engagement Scenarios", "contact": "Emily Johnson", "description": "Simulate scenarios for stakeholder engagement."}
            ],
            "Afternoon": [
                {"activity": "Case Study: Stakeholder Management Successes", "contact": "David Clark", "description": "Analyze case studies on successful stakeholder management."},
                {"activity": "Meeting with Stakeholders for Feedback", "contact": "Patricia Garcia", "description": "Gather feedback from stakeholders."}
            ]
        },
        "Day 14": {
            "Morning": [
                {"activity": "Training: Risk Management Strategies", "contact": "Linda Robinson", "description": "Learn strategies for managing risks."},
                {"activity": "Workshop: Creating a Risk Management Plan", "contact": "Barbara Rodriguez", "description": "Create a risk management plan for a project."}
            ],
            "Afternoon": [
                {"activity": "Collaborative Session: Identifying Potential Risks", "contact": "Chris Davis", "description": "Identify potential risks in current projects."},
                {"activity": "Feedback Session: Learning from Past Projects", "contact": "John Doe", "description": "Discuss lessons learned from past projects."}
            ]
        },
        "Day 15": {
            "Morning": [
                {"activity": "Team Building: Collaboration and Communication", "contact": "Jane Smith", "description": "Engage in team-building activities to foster collaboration."},
                {"activity": "Networking Lunch with Leadership Team", "contact": "Michael Brown", "description": "Lunch opportunity to network with the leadership team."}
            ],
            "Afternoon": [
                {"activity": "Reflection Session: Third Week Review", "contact": "James Lewis", "description": "Review your third week and reflect on learnings."},
                {"activity": "Planning for the Final Week", "contact": "Emily Johnson", "description": "Set goals for the final week of onboarding."}
            ]
        }
    },
    "Week 4": {
        "Day 16": {
            "Morning": [
                {"activity": "Final Review of Onboarding Goals", "contact": "David Clark", "description": "Review all onboarding goals and achievements."},
                {"activity": "One-on-One with Supervisor to Discuss Progress", "contact": "Patricia Garcia", "description": "Discussion with your supervisor about your progress."}
            ],
            "Afternoon": [
                {"activity": "Training: Advanced Project Management Techniques", "contact": "Chris Davis", "description": "Learn advanced project management techniques."},
                {"activity": "Collaborative Workshop: Finalizing Project Plans", "contact": "John Doe", "description": "Collaborate on finalizing project plans."}
            ]
        },
        "Day 17": {
            "Morning": [
                {"activity": "Workshop: Presentation Skills for Project Leaders", "contact": "Jane Smith", "description": "Workshop to enhance your presentation skills."},
                {"activity": "Role-Playing: Presenting to Stakeholders", "contact": "Michael Brown", "description": "Role-play sessions for presenting to stakeholders."}
            ],
            "Afternoon": [
                {"activity": "Feedback Session: Practice Presentations", "contact": "James Lewis", "description": "Practice your presentation and gather feedback."},
                {"activity": "Networking with Team Members", "contact": "Emily Johnson", "description": "Opportunity to network with team members."}
            ]
        },
        "Day 18": {
            "Morning": [
                {"activity": "Training: Conflict Resolution Strategies", "contact": "David Clark", "description": "Learn effective conflict resolution strategies."},
                {"activity": "Case Study: Resolving Conflicts in Teams", "contact": "Patricia Garcia", "description": "Analyze case studies on conflict resolution."}
            ],
            "Afternoon": [
                {"activity": "Workshop: Building a Positive Team Culture", "contact": "Chris Davis", "description": "Workshop on fostering a positive team culture."},
                {"activity": "Final Q&A Session with Leadership", "contact": "John Doe", "description": "Q&A session with leadership for final insights."}
            ]
        },
        "Day 19": {
            "Morning": [
                {"activity": "Interactive Session: Preparing for Go-Live", "contact": "Jane Smith", "description": "Prepare for go-live scenarios."},
                {"activity": "Mock Go-Live Exercise", "contact": "Michael Brown", "description": "Participate in a mock go-live exercise."}
            ],
            "Afternoon": [
                {"activity": "Reflection and Celebration of Onboarding Journey", "contact": "James Lewis", "description": "Reflect on your journey and celebrate achievements."},
                {"activity": "Feedback Session: Onboarding Experience", "contact": "Emily Johnson", "description": "Share your feedback on the onboarding experience."}
            ]
        },
        "Day 20": {
            "Morning": [
                {"activity": "Final Check-in with Onboarding Buddy", "contact": "David Clark", "description": "Final check-in with your onboarding buddy."},
                {"activity": "Set Future Development Goals", "contact": "Patricia Garcia", "description": "Set personal and professional development goals."}
            ],
            "Afternoon": [
                {"activity": "Wrap-Up Meeting with Leadership Team", "contact": "Chris Davis", "description": "Final meeting with the leadership team."},
                {"activity": "Celebration of Completion of Onboarding Program", "contact": "John Doe", "description": "Celebrate the completion of the onboarding program."}
            ]
        }
    }
}

def display_day_plan(week, day, start_date, user_name):
    morning_activities = onboarding_plan[week][day].get("Morning", [])
    afternoon_activities = onboarding_plan[week][day].get("Afternoon", [])

    total_days = (int(week.split()[-1]) - 1) * 5 + (int(day.split()[-1]) - 1)
    current_date = start_date + timedelta(days=total_days)

    st.write(f"**Onboarding Plan for {user_name} - {week} {day}**")
    st.write(f"**Date:** {current_date.strftime('%Y-%m-%d')}")

    st.write("### Morning Activities:")
    for activity in morning_activities:
        with st.expander(activity["activity"]):
            st.write(f"- **Contact:** {activity['contact']}")
            st.write(f"- **Description:** {activity['description']}")

    st.write("### Afternoon Activities:")
    for activity in afternoon_activities:
        with st.expander(activity["activity"]):
            st.write(f"- **Contact:** {activity['contact']}")
            st.write(f"- **Description:** {activity['description']}")


def main():
    st.title("30-Day Onboarding Plan")
    user_name = st.text_input("Enter your full name")
    start_date = st.date_input("Select Start Date", value=datetime.today())

    if user_name:
        week_choice = st.selectbox("Select Week", options=list(onboarding_plan.keys()))
        day_choice = st.selectbox("Select Day", options=list(onboarding_plan[week_choice].keys()))

        display_day_plan(week_choice, day_choice, start_date, user_name)
    else:
        st.warning("Please enter your full name to customize the onboarding plan.")


if __name__ == "__main__":
    main()
