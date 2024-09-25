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
                {
                    "activity": "Introduction to the Company Culture and Values",
                    "contact": "Jane Smith",
                    "description": "An insightful session to understand the core values that drive our organization and shape our work culture."
                },
                {
                    "activity": "Overview of the Localization Department",
                    "contact": "Emily Johnson",
                    "description": "A comprehensive overview of the Localization Department's structure, objectives, and ongoing projects."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Office Tour and Meet Key Stakeholders",
                    "contact": "Michael Brown",
                    "description": "A guided tour of the office to familiarize you with the environment and meet key stakeholders."
                },
                {
                    "activity": "Introduction to the Onboarding Buddy (a peer mentor)",
                    "contact": "Chris Davis",
                    "description": "Meet your onboarding buddy who will guide you through the initial phase of your onboarding journey."
                },
                {
                    "activity": "Setting up Workstation and Tools",
                    "contact": "Patricia Garcia",
                    "description": "Assistance in setting up your workstation, tools, and necessary software for your role."
                }
            ]
        },
        "Day 2": {
            "Morning": [
                {
                    "activity": "Deep Dive into the Job Description and Expectations",
                    "contact": "Robert Martinez",
                    "description": "An in-depth discussion about your role and expectations to set you up for success."
                },
                {
                    "activity": "Interactive Workshop: Role-Playing Key Responsibilities",
                    "contact": "Linda Robinson",
                    "description": "A hands-on workshop where you can practice your key responsibilities through role-playing scenarios."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Meeting with Direct Supervisor to Discuss Performance Metrics",
                    "contact": "David Clark",
                    "description": "Discuss your performance metrics and how success will be measured in your role."
                },
                {
                    "activity": "Collaborative Session: Setting Personal Goals for the First 30 Days",
                    "contact": "Barbara Rodriguez",
                    "description": "Work together to set realistic and achievable personal goals for your first month."
                }
            ]
        },
        "Day 3": {
            "Morning": [
                {
                    "activity": "Hands-On Training: Project Management Software",
                    "contact": "James Lewis",
                    "description": "Training on the project management software that will be used in your role."
                },
                {
                    "activity": "Interactive Webinar: Localization Workflow Tools",
                    "contact": "Mary Lee",
                    "description": "A webinar focusing on the tools used in localization workflows."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Case Study Review: Successful Past Projects",
                    "contact": "William Walker",
                    "description": "Review successful past projects to understand best practices."
                },
                {
                    "activity": "Q&A Session with IT Support for Troubleshooting",
                    "contact": "Lisa Hall",
                    "description": "An opportunity to ask IT support any questions regarding your tools and systems."
                }
            ]
        },
        "Day 4": {
            "Morning": [
                {
                    "activity": "Client Portfolio Overview: Key Clients and Projects",
                    "contact": "Mark Allen",
                    "description": "An overview of key clients and projects you will be working on."
                },
                {
                    "activity": "Interactive Session: Understanding Client Requirements",
                    "contact": "Nancy Young",
                    "description": "An interactive session to dive deep into understanding client needs."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Workshop: Developing Client-Specific Strategies",
                    "contact": "Steven King",
                    "description": "Collaborative workshop to develop strategies tailored to specific clients."
                },
                {
                    "activity": "Role-Playing: Mock Client Meetings",
                    "contact": "Karen Wright",
                    "description": "Practice your client meeting skills in a role-playing format."
                }
            ]
        },
        "Day 5": {
            "Morning": [
                {
                    "activity": "Team Building Activities",
                    "contact": "Brian Scott",
                    "description": "Engaging activities designed to build relationships within the team."
                },
                {
                    "activity": "Networking Lunch with Cross-Functional Teams",
                    "contact": "Sandra Green",
                    "description": "A lunch session to network with members from different teams."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Feedback Session: First Week Review with Onboarding Buddy",
                    "contact": "Kevin Adams",
                    "description": "Reflect on your first week and discuss feedback with your onboarding buddy."
                },
                {
                    "activity": "Planning for the Upcoming Week",
                    "contact": "Megan Baker",
                    "description": "Set goals and plans for your second week."
                }
            ]
        }
    },
    "Week 2": {
        "Day 6": {
            "Morning": [
                {
                    "activity": "Workshop: Understanding Revenue and Profit Growth",
                    "contact": "Michael Brown",
                    "description": "A workshop to understand the financial aspects of the business."
                },
                {
                    "activity": "Interactive Budgeting Exercise",
                    "contact": "James Lewis",
                    "description": "Hands-on exercise to learn budgeting skills."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Case Study: Financial Reporting and Forecasting",
                    "contact": "Linda Robinson",
                    "description": "Review case studies on financial reporting and forecasting."
                },
                {
                    "activity": "Meeting with Finance Team for Q&A",
                    "contact": "Barbara Rodriguez",
                    "description": "Ask questions and clarify financial processes with the finance team."
                }
            ]
        },
        "Day 7": {
            "Morning": [
                {
                    "activity": "Interactive Session: Workflow Management Best Practices",
                    "contact": "Emily Johnson",
                    "description": "Learn about best practices in managing workflows effectively."
                },
                {
                    "activity": "Simulation: Managing a Complex Localization Project",
                    "contact": "David Clark",
                    "description": "Participate in a simulation to practice managing localization projects."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Workshop: Continuous Improvement Strategies",
                    "contact": "Patricia Garcia",
                    "description": "Strategies to promote continuous improvement within teams."
                },
                {
                    "activity": "Collaborative Session: Identifying Operational Bottlenecks",
                    "contact": "Chris Davis",
                    "description": "Work together to identify and address operational bottlenecks."
                }
            ]
        },
        "Day 8": {
            "Morning": [
                {
                    "activity": "Interactive Workshop: Client Communication and Consultancy",
                    "contact": "John Doe",
                    "description": "Learn effective communication strategies with clients."
                },
                {
                    "activity": "Role-Playing: Client Interaction Scenarios",
                    "contact": "Jane Smith",
                    "description": "Practice client interactions through role-playing scenarios."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Case Study: Successful Client Management",
                    "contact": "Michael Brown",
                    "description": "Review successful client management strategies."
                },
                {
                    "activity": "Meeting with Sales Team for Collaboration Strategies",
                    "contact": "Emily Johnson",
                    "description": "Discuss collaboration strategies with the sales team."
                }
            ]
        },
        "Day 9": {
            "Morning": [
                {
                    "activity": "Training: KPI Management and Reporting",
                    "contact": "James Lewis",
                    "description": "Training on key performance indicators and how to report them."
                },
                {
                    "activity": "Interactive Session: Using Data to Drive Decisions",
                    "contact": "David Clark",
                    "description": "Learn how to leverage data for decision-making."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Collaborative Workshop: Developing a KPI Dashboard",
                    "contact": "Patricia Garcia",
                    "description": "Work together to create a dashboard for tracking KPIs."
                },
                {
                    "activity": "Review Session with Direct Supervisor",
                    "contact": "Chris Davis",
                    "description": "Review your progress and set future goals with your supervisor."
                }
            ]
        },
        "Day 10": {
            "Morning": [
                {
                    "activity": "One-on-One Feedback Session with Onboarding Buddy",
                    "contact": "John Doe",
                    "description": "Personal feedback session with your onboarding buddy."
                },
                {
                    "activity": "Team Feedback Session: Sharing Insights and Improvements",
                    "contact": "Jane Smith",
                    "description": "Collaborate with the team to share insights and improvements."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Networking Event: Meet Other Teams",
                    "contact": "Michael Brown",
                    "description": "An event to meet and network with other teams in the organization."
                },
                {
                    "activity": "Planning Session for the Next Month",
                    "contact": "Emily Johnson",
                    "description": "Set goals and plans for the upcoming month."
                }
            ]
        }
    },
    "Week 3": {
        "Day 11": {
            "Morning": [
                {
                    "activity": "Wrap-Up and Reflection on the First Two Weeks",
                    "contact": "Michael Brown",
                    "description": "Reflect on your experiences and prepare for the next phase."
                },
                {
                    "activity": "Introduction to Compliance and Regulations",
                    "contact": "Emily Johnson",
                    "description": "Learn about compliance and regulatory requirements relevant to your role."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Interactive Compliance Training",
                    "contact": "James Lewis",
                    "description": "Hands-on training on compliance protocols and procedures."
                },
                {
                    "activity": "Q&A Session with Compliance Team",
                    "contact": "David Clark",
                    "description": "Ask questions regarding compliance and regulations."
                }
            ]
        },
        "Day 12": {
            "Morning": [
                {
                    "activity": "Advanced Training: Software Tools for Localization",
                    "contact": "Linda Robinson",
                    "description": "Advanced training on the software tools used in localization."
                },
                {
                    "activity": "Hands-On Practice with Tools",
                    "contact": "Barbara Rodriguez",
                    "description": "Hands-on practice session using localization tools."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Team Project: Applying Tools in Real Scenarios",
                    "contact": "Chris Davis",
                    "description": "Work on a team project applying learned tools in real scenarios."
                },
                {
                    "activity": "Feedback and Review Session",
                    "contact": "Patricia Garcia",
                    "description": "Review your team project and receive feedback."
                }
            ]
        },
        "Day 13": {
            "Morning": [
                {
                    "activity": "Introduction to Project Lifecycle in Localization",
                    "contact": "Michael Brown",
                    "description": "Learn about the project lifecycle specific to localization projects."
                },
                {
                    "activity": "Case Study: Localization Project Management",
                    "contact": "Emily Johnson",
                    "description": "Review a case study focusing on project management in localization."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Workshop: Effective Time Management Strategies",
                    "contact": "James Lewis",
                    "description": "Learn strategies for effective time management in project work."
                },
                {
                    "activity": "Peer Review: Evaluating Project Proposals",
                    "contact": "David Clark",
                    "description": "Evaluate project proposals as a peer review exercise."
                }
            ]
        },
        "Day 14": {
            "Morning": [
                {
                    "activity": "Interactive Training: Cultural Sensitivity in Localization",
                    "contact": "Linda Robinson",
                    "description": "Training on the importance of cultural sensitivity in localization."
                },
                {
                    "activity": "Role-Playing: Navigating Cultural Differences",
                    "contact": "Barbara Rodriguez",
                    "description": "Practice navigating cultural differences through role-playing scenarios."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Feedback Session: Cultural Sensitivity Training",
                    "contact": "Chris Davis",
                    "description": "Provide feedback on the cultural sensitivity training."
                },
                {
                    "activity": "Planning for the Final Project",
                    "contact": "Patricia Garcia",
                    "description": "Plan your final project for the onboarding program."
                }
            ]
        },
        "Day 15": {
            "Morning": [
                {
                    "activity": "Project Kick-Off Meeting for Final Project",
                    "contact": "Michael Brown",
                    "description": "Kick-off meeting for your final project, outlining expectations and goals."
                },
                {
                    "activity": "Team Roles and Responsibilities Discussion",
                    "contact": "Emily Johnson",
                    "description": "Discuss roles and responsibilities within the project team."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Research Session: Gathering Necessary Information",
                    "contact": "James Lewis",
                    "description": "Conduct research to gather information for your final project."
                },
                {
                    "activity": "Preparation for Final Project Presentation",
                    "contact": "David Clark",
                    "description": "Begin preparation for presenting your final project."
                }
            ]
        }
    },
    "Week 4": {
        "Day 16": {
            "Morning": [
                {
                    "activity": "Final Project Work Session",
                    "contact": "Linda Robinson",
                    "description": "Dedicated time for working on your final project."
                },
                {
                    "activity": "Mentorship Meeting: Guidance on Final Project",
                    "contact": "Barbara Rodriguez",
                    "description": "Meet with your mentor for guidance on your final project."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Mock Presentations: Practice Your Project Pitch",
                    "contact": "Chris Davis",
                    "description": "Practice presenting your final project in a mock setting."
                },
                {
                    "activity": "Feedback Session: Peer Review of Projects",
                    "contact": "Patricia Garcia",
                    "description": "Provide and receive feedback on project presentations."
                }
            ]
        },
        "Day 17": {
            "Morning": [
                {
                    "activity": "Final Project Presentation Day",
                    "contact": "Michael Brown",
                    "description": "Present your final project to the team and receive feedback."
                },
                {
                    "activity": "Q&A Session: Discussing Feedback and Next Steps",
                    "contact": "Emily Johnson",
                    "description": "Discuss feedback received during presentations and outline next steps."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Celebration: Success of Final Projects",
                    "contact": "James Lewis",
                    "description": "Celebrate the success of your final project and onboarding journey."
                },
                {
                    "activity": "Wrap-Up Meeting: Final Thoughts and Reflections",
                    "contact": "David Clark",
                    "description": "A wrap-up meeting to share final thoughts and reflections on your onboarding experience."
                }
            ]
        },
        "Day 18": {
            "Morning": [
                {
                    "activity": "Follow-Up: Continuous Learning Opportunities",
                    "contact": "Linda Robinson",
                    "description": "Learn about continuous learning opportunities available within the organization."
                },
                {
                    "activity": "Networking Session: Connecting with Alumni",
                    "contact": "Barbara Rodriguez",
                    "description": "Connect with alumni and learn from their experiences."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Goal Setting for the Next 90 Days",
                    "contact": "Chris Davis",
                    "description": "Set personal and professional goals for the next 90 days."
                },
                {
                    "activity": "Feedback Survey: Improving the Onboarding Experience",
                    "contact": "Patricia Garcia",
                    "description": "Complete a survey to provide feedback on your onboarding experience."
                }
            ]
        },
        "Day 19": {
            "Morning": [
                {
                    "activity": "Team Integration: Joining Regular Meetings",
                    "contact": "Michael Brown",
                    "description": "Start joining regular team meetings to integrate into the team."
                },
                {
                    "activity": "Shadowing: Observing Experienced Team Members",
                    "contact": "Emily Johnson",
                    "description": "Shadow experienced team members to learn from their expertise."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Project Involvement: Engaging in Ongoing Projects",
                    "contact": "James Lewis",
                    "description": "Engage in ongoing projects to apply your learning."
                },
                {
                    "activity": "Feedback Loop: Continuous Improvement Discussions",
                    "contact": "David Clark",
                    "description": "Participate in discussions focused on continuous improvement."
                }
            ]
        },
        "Day 20": {
            "Morning": [
                {
                    "activity": "Celebration: Completion of the Onboarding Program",
                    "contact": "Linda Robinson",
                    "description": "Celebrate the completion of your onboarding program with the team."
                },
                {
                    "activity": "Final Reflections and Moving Forward",
                    "contact": "Barbara Rodriguez",
                    "description": "Reflect on your onboarding experience and look forward to your future contributions."
                }
            ],
            "Afternoon": [
                {
                    "activity": "Networking: Building Your Internal Network",
                    "contact": "Chris Davis",
                    "description": "Focus on building your internal network within the organization."
                },
                {
                    "activity": "Final Wrap-Up: Key Takeaways and Closing",
                    "contact": "Patricia Garcia",
                    "description": "Wrap up your onboarding experience with key takeaways and closing thoughts."
                }
            ]
        }
    }
}

def display_day_plan(week, day, start_date):
    morning_activities = onboarding_plan[week][day].get("Morning", [])
    afternoon_activities = onboarding_plan[week][day].get("Afternoon", [])

    total_days = (int(week.split()[-1]) - 1) * 5 + (int(day.split()[-1]) - 1)
    current_date = start_date + timedelta(days=total_days)

    st.write(f"**Date: {current_date.strftime('%Y-%m-%d')} - {week} {day}**")
    st.write("### Morning Activities:")
    for activity in morning_activities:
        st.write(f"- **Activity:** {activity['activity']}")
        st.write(f"  - **Contact:** {activity['contact']}")
        st.write(f"  - **Description:** {activity['description']}")

    st.write("### Afternoon Activities:")
    for activity in afternoon_activities:
        st.write(f"- **Activity:** {activity['activity']}")
        st.write(f"  - **Contact:** {activity['contact']}")
        st.write(f"  - **Description:** {activity['description']}")


def main():
    st.title("30-Day Onboarding Plan")
    start_date = st.date_input("Select Start Date", value=datetime.today())

    week_choice = st.selectbox("Select Week", options=list(onboarding_plan.keys()))
    day_choice = st.selectbox("Select Day", options=list(onboarding_plan[week_choice].keys()))

    display_day_plan(week_choice, day_choice, start_date)


if __name__ == "__main__":
    main()
