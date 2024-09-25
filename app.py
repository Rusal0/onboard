import streamlit as st
from datetime import datetime, timedelta

# Onboarding Data with contact persons
onboarding_plan = {
    "Week 1": {
        "Day 1": {
            "Morning": [
                ("Welcome Breakfast with the Team", "John Doe"),
                ("Introduction to the Company Culture and Values", "Jane Smith"),
                ("Overview of the Localization Department", "Emily Johnson")
            ],
            "Afternoon": [
                ("Office Tour and Meet Key Stakeholders", "Michael Brown"),
                ("Introduction to the Onboarding Buddy (a peer mentor)", "Chris Davis"),
                ("Setting up Workstation and Tools", "Patricia Garcia")
            ]
        },
        "Day 2": {
            "Morning": [
                ("Deep Dive into the Job Description and Expectations", "Robert Martinez"),
                ("Interactive Workshop: Role-Playing Key Responsibilities", "Linda Robinson")
            ],
            "Afternoon": [
                ("Meeting with Direct Supervisor to Discuss Performance Metrics", "David Clark"),
                ("Collaborative Session: Setting Personal Goals for the First 30 Days", "Barbara Rodriguez")
            ]
        },
        "Day 3": {
            "Morning": [
                ("Hands-On Training: Project Management Software", "James Lewis"),
                ("Interactive Webinar: Localization Workflow Tools", "Mary Lee")
            ],
            "Afternoon": [
                ("Case Study Review: Successful Past Projects", "William Walker"),
                ("Q&A Session with IT Support for Troubleshooting", "Lisa Hall")
            ]
        },
        "Day 4": {
            "Morning": [
                ("Client Portfolio Overview: Key Clients and Projects", "Mark Allen"),
                ("Interactive Session: Understanding Client Requirements", "Nancy Young")
            ],
            "Afternoon": [
                ("Workshop: Developing Client-Specific Strategies", "Steven King"),
                ("Role-Playing: Mock Client Meetings", "Karen Wright")
            ]
        },
        "Day 5": {
            "Morning": [
                ("Team Building Activities", "Brian Scott"),
                ("Networking Lunch with Cross-Functional Teams", "Sandra Green")
            ],
            "Afternoon": [
                ("Feedback Session: First Week Review with Onboarding Buddy", "Kevin Adams"),
                ("Planning for the Upcoming Week", "Megan Baker")
            ]
        }
    },
    "Week 2": {
        "Day 6": {
            "Morning": [
                ("Workshop: Understanding Revenue and Profit Growth", "Michael Brown"),
                ("Interactive Budgeting Exercise", "James Lewis")
            ],
            "Afternoon": [
                ("Case Study: Financial Reporting and Forecasting", "Linda Robinson"),
                ("Meeting with Finance Team for Q&A", "Barbara Rodriguez")
            ]
        },
        "Day 7": {
            "Morning": [
                ("Interactive Session: Workflow Management Best Practices", "Emily Johnson"),
                ("Simulation: Managing a Complex Localization Project", "David Clark")
            ],
            "Afternoon": [
                ("Workshop: Continuous Improvement Strategies", "Patricia Garcia"),
                ("Collaborative Session: Identifying Operational Bottlenecks", "Chris Davis")
            ]
        },
        "Day 8": {
            "Morning": [
                ("Interactive Workshop: Client Communication and Consultancy", "John Doe"),
                ("Role-Playing: Client Interaction Scenarios", "Jane Smith")
            ],
            "Afternoon": [
                ("Case Study: Successful Client Management", "Michael Brown"),
                ("Meeting with Sales Team for Collaboration Strategies", "Emily Johnson")
            ]
        },
        "Day 9": {
            "Morning": [
                ("Training: KPI Management and Reporting", "James Lewis"),
                ("Interactive Session: Using Data to Drive Decisions", "David Clark")
            ],
            "Afternoon": [
                ("Collaborative Workshop: Developing a KPI Dashboard", "Patricia Garcia"),
                ("Review Session with Direct Supervisor", "Chris Davis")
            ]
        },
        "Day 10": {
            "Morning": [
                ("One-on-One Feedback Session with Onboarding Buddy", "John Doe"),
                ("Team Feedback Session: Sharing Insights and Improvements", "Jane Smith")
            ],
            "Afternoon": [
                ("Personal Reflection and Goal Adjustment", "Michael Brown"),
                ("Planning for the Upcoming Week", "Emily Johnson")
            ]
        }
    },
    "Week 3": {
        "Day 11": {
            "Morning": [
                ("Leadership Workshop: Leading Project Managers", "Linda Robinson"),
                ("Role-Playing: Leadership Scenarios", "Barbara Rodriguez")
            ],
            "Afternoon": [
                ("Mentorship Session with Senior Leaders", "David Clark"),
                ("Collaborative Session: Developing Leadership Skills", "Patricia Garcia")
            ]
        },
        "Day 12": {
            "Morning": [
                ("Interactive Session: Best Practices in Global Partnership", "Chris Davis"),
                ("Case Study: Successful Global Collaborations", "John Doe")
            ],
            "Afternoon": [
                ("Workshop: Leveraging Global Resources", "Jane Smith"),
                ("Networking Session with International Teams", "Michael Brown")
            ]
        },
        "Day 13": {
            "Morning": [
                ("Interactive Workshop: Advanced Client Strategies", "Emily Johnson"),
                ("Role-Playing: Handling Difficult Client Situations", "James Lewis")
            ],
            "Afternoon": [
                ("Meeting with Key Clients for Introduction", "David Clark"),
                ("Collaborative Session: Developing Client-Specific Plans", "Patricia Garcia")
            ]
        },
        "Day 14": {
            "Morning": [
                ("Training: Advanced Continuous Improvement Techniques", "Chris Davis"),
                ("Simulation: Implementing Improvement Strategies", "John Doe")
            ],
            "Afternoon": [
                ("Workshop: Identifying and Solving Operational Issues", "Jane Smith"),
                ("Feedback Session with Direct Supervisor", "Michael Brown")
            ]
        },
        "Day 15": {
            "Morning": [
                ("One-on-One Feedback Session with Onboarding Buddy", "Emily Johnson"),
                ("Team Feedback Session: Sharing Insights and Improvements", "James Lewis")
            ],
            "Afternoon": [
                ("Personal Reflection and Goal Adjustment", "David Clark"),
                ("Planning for the Upcoming Week", "Patricia Garcia")
            ]
        }
    },
    "Week 4": {
        "Day 16": {
            "Morning": [
                ("Review of All Tools, Processes, and Strategies", "Chris Davis"),
                ("Interactive Q&A Session with Key Stakeholders", "John Doe")
            ],
            "Afternoon": [
                ("Final Adjustments to Personal Goals and Plans", "Jane Smith"),
                ("Collaborative Session: Finalizing Client-Specific Strategies", "Michael Brown")
            ]
        },
        "Day 17": {
            "Morning": [
                ("Workshop: Advanced Communication Skills", "Emily Johnson"),
                ("Role-Playing: Risk Analysis and Decision-Making", "James Lewis")
            ],
            "Afternoon": [
                ("Mentorship Session: Soft Skills Development", "David Clark"),
                ("Collaborative Session: Peer Feedback and Improvement", "Patricia Garcia")
            ]
        },
        "Day 18": {
            "Morning": [
                ("Full-Day Simulation: Managing a Live Localization Project", "Chris Davis"),
                ("Real-Time Feedback from Team and Stakeholders", "John Doe")
            ]
        },
        "Day 19": {
            "Morning": [
                ("Final Review with Direct Supervisor and Onboarding Buddy", "Jane Smith"),
                ("Adjusting Strategies Based on Feedback", "Michael Brown")
            ],
            "Afternoon": [
                ("Collaborative Session: Ensuring Readiness for Going Live", "Emily Johnson"),
                ("Team Meeting: Final Preparations", "James Lewis")
            ]
        },
        "Day 20": {
            "Morning": [
                ("Officially Taking Over Responsibilities", "David Clark"),
                ("Support Available from Onboarding Buddy and Team", "Patricia Garcia")
            ],
            "Afternoon": [
                ("Continuous Monitoring and Feedback", "Chris Davis"),
                ("Celebratory Team Event", "John Doe")
            ]
        }
    }
}

def display_day_plan(week, day, start_date):
    morning_activities = onboarding_plan[week][day].get("Morning", [])
    afternoon_activities = onboarding_plan[week][day].get("Afternoon", [])

    total_days = (int(week.split()[-1]) - 1) * 5 + (int(day.split()[-1]) - 1)
    current_date = start_date + timedelta(days=total_days)

    morning_text = "\n".join([f"{activity[0]} (Contact: {activity[1]})" for activity in morning_activities])
    afternoon_text = "\n".join([f"{activity[0]} (Contact: {activity[1]})" for activity in afternoon_activities])

    st.write(f"**Date:** {current_date.strftime('%Y-%m-%d')}")
    st.write(f"**Morning:**\n{morning_text}")
    st.write(f"**Afternoon:**\n{afternoon_text}")
    st.write("\n---\n")

def main():
    st.title("Onboarding Plan")

    # Get user input
    full_name = st.text_input("Enter your full name")
    start_date_str = st.text_input("Enter start date (YYYY-MM-DD)")

    if full_name and start_date_str:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

            st.write(f"\n## Welcome Onboard {full_name}!\n")

            for week in onboarding_plan.keys():
                st.write(f"### {week}")
                for day in onboarding_plan[week].keys():
                    st.write(f"**{day}**")
                    display_day_plan(week, day, start_date)

        except ValueError:
            st.error("Please enter a valid date in YYYY-MM-DD format")

if __name__ == "__main__":
    main()
