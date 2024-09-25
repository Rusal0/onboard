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
        # More days can be added here...
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
        # More days can be added here...
    },
    # Additional weeks can be added here...
}

def display_day_plan(week, day, start_date):
    morning_activities = onboarding_plan[week][day].get("Morning", [])
    afternoon_activities = onboarding_plan[week][day].get("Afternoon", [])

    total_days = (int(week.split()[-1]) - 1) * 5 + (int(day.split()[-1]) - 1)
    current_date = start_date + timedelta(days=total_days)

    # Join morning activities with line breaks between each
    morning_text = "\n".join([f"- {activity[0]} (Contact: {activity[1]})" for activity in morning_activities])
    # Join afternoon activities with line breaks between each
    afternoon_text = "\n".join([f"- {activity[0]} (Contact: {activity[1]})" for activity in afternoon_activities])

    st.write(f"**Date:** {current_date.strftime('%Y-%m-%d')}")
    st.markdown(f"**Morning:**\n{morning_text}")
    st.markdown(f"**Afternoon:**\n{afternoon_text}")
    st.markdown("---")  # Adds a horizontal rule for separation

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
