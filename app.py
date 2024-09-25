import numpy as np
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
                {"activity": "Introduction to the Company Culture and Values", 
                 "contact": "Jane Smith", 
                 "description": "In this session, you will gain insights into our company culture and core values that drive our mission and daily operations. We will explore what makes our organization unique, including our commitment to teamwork, innovation, and customer service excellence. You will learn about our vision, guiding principles, and how we foster an inclusive and supportive environment. This introduction is essential for understanding how your role aligns with our organizational goals and how you can contribute to our shared values."},
                {"activity": "Overview of the Localization Department", 
                "contact": "Emily Johnson", 
                "description": "In this session, you will receive a comprehensive overview of the Localization Department, including its structure, key functions, and strategic importance within the organization. We will discuss the team’s primary objectives, such as enhancing global customer experience, ensuring brand consistency across languages, and supporting international market expansion. You will also be introduced to the tools, processes, and best practices we employ to manage localization projects effectively. This overview will help you understand your role within the department and how you can contribute to our mission of delivering high-quality localized content."}
            ],
            "Afternoon": [
                {"activity": "Office Tour and Meet Key Stakeholders", 
                "contact": "Michael Brown", 
                "description": "Join us for an engaging office tour where you will explore our workspace and learn about the various departments that make up our organization. This is a great opportunity to familiarize yourself with our facilities and resources. During the tour, you will also meet key stakeholders from different teams, including leadership and cross-functional partners. This introduction will help you understand how each department collaborates to achieve our organizational goals and provide insights into the broader context of your role within the company. Building these connections early on will enhance your integration into the team."},
                {"activity": "Introduction to the Onboarding Buddy (a peer mentor)", 
                "contact": "Chris Davis", 
                "description": "In this session, you will be introduced to your Onboarding Buddy, a peer mentor assigned to support you during your transition into the organization. Your buddy will be a valuable resource for answering questions, providing guidance, and sharing insights about company culture and processes. This relationship aims to help you acclimate more quickly and feel comfortable in your new role. Throughout your onboarding journey, your buddy will check in regularly, offer assistance with navigating the workplace, and ensure you have the support you need to succeed."},
                {"activity": "Setting up Workstation and Tools", 
                "contact": "Patricia Garcia", 
                "description": "During this session, you will receive guidance on setting up your workstation and accessing the tools and software necessary for your role. We will walk you through the equipment provided, including your computer, phone, and any other devices, ensuring you know how to configure and personalize them to your preferences. Additionally, you will learn about key software applications and platforms used by our team, including collaboration tools, project management systems, and communication channels. This setup will ensure you are fully equipped to begin your work effectively and efficiently from day one."},
            ]
        },
        "Day 2": {
            "Morning": [
                {"activity": "Deep Dive into the Job Description and Expectations", 
                "contact": "Robert Martinez", 
                "description": "In this session, we will take a detailed look at your job description and the expectations for your role within the organization. We will discuss the key responsibilities, performance metrics, and deliverables associated with your position, ensuring you have a clear understanding of what success looks like. This is also an opportunity to clarify any questions you may have regarding your role and to align on priorities and goals with your manager. By the end of this session, you will have a comprehensive understanding of how your contributions will impact the team and the organization as a whole."},
                {"activity": "Interactive Workshop: Role-Playing Key Responsibilities", 
                "contact": "Linda Robinson", 
                "description": "Participate in an engaging interactive workshop designed to help you understand and practice your key responsibilities through role-playing scenarios. This hands-on experience will allow you to simulate real-life situations you may encounter in your role, fostering a deeper understanding of how to handle various challenges and tasks effectively. You will collaborate with peers and mentors, receiving feedback and tips to enhance your skills. This workshop aims to build your confidence, improve problem-solving abilities, and ensure you are well-prepared for your responsibilities in a supportive and collaborative environment."}
            ],
            "Afternoon": [
                {"activity": "Meeting with Direct Supervisor to Discuss Performance Metrics", 
                "contact": "David Clark", 
                "description": "In this important meeting, you will sit down with your direct supervisor to review and discuss the performance metrics that will guide your success in this role. Together, you will outline the key performance indicators (KPIs) specific to your position, set initial goals, and clarify expectations for your contributions. This is an excellent opportunity to ask questions, seek guidance on how to achieve your targets, and ensure alignment on priorities. By establishing clear performance metrics early on, you will be better equipped to measure your progress and adapt your approach as needed throughout your onboarding journey."},
                {"activity": "Collaborative Session: Setting Personal Goals for the First 30 Days", 
                "contact": "Barbara Rodriguez", 
                "description": "Join us for a collaborative session focused on setting your personal goals for the first 30 days in your new role. During this workshop, you will work alongside your supervisor and peers to identify specific, measurable, achievable, relevant, and time-bound (SMART) goals that align with your job responsibilities and the team’s objectives. This session will encourage open discussion about your aspirations, challenges, and priorities, allowing you to create a tailored roadmap for your initial month. By establishing clear goals, you will enhance your focus and motivation, paving the way for a successful start in your new position."}
            ]
        },
        "Day 3": {
            "Morning": [
                {"activity": "Hands-On Training: Project Management Software", 
                "contact": "James Lewis", 
                "description": "In this interactive training session, you will gain practical experience using our project management software, a crucial tool for tracking progress, collaborating with team members, and managing tasks effectively. During the hands-on training, you will learn how to navigate the software's features, create and assign tasks, set deadlines, and monitor project timelines. You’ll also explore best practices for utilizing the software to enhance your productivity and communication within the team. This training will equip you with the skills needed to manage your projects efficiently and collaborate seamlessly with your colleagues from day one."},
                {"activity": "Interactive Webinar: Localization Workflow Tools", 
                "contact": "Mary Lee", 
                "description": "Join us for an interactive webinar focused on the localization workflow tools that are essential for your role. In this session, you will be introduced to the various software and platforms used to manage localization projects effectively, including translation management systems, quality assurance tools, and collaboration platforms. Through demonstrations and real-life examples, you will learn how these tools streamline processes, enhance communication, and improve project outcomes. This webinar will also include a Q&A segment where you can ask questions and discuss best practices with experienced team members, ensuring you feel confident in utilizing these tools as part of your daily workflow."}
            ],
            "Afternoon": [
                {"activity": "Case Study Review: Successful Past Projects", 
                "contact": "William Walker", 
                "description": "In this engaging session, we will review case studies of successful past projects completed by the Localization Department. You will gain insights into the strategies and best practices that contributed to these projects' achievements, as well as the challenges encountered and lessons learned. This review will highlight key elements such as stakeholder collaboration, effective use of localization tools, and adherence to timelines and budgets. By analyzing these real-world examples, you will better understand the department’s workflow and how you can apply these lessons to your own projects, fostering a culture of continuous improvement and innovation."},
                {"activity": "Q&A Session with IT Support for Troubleshooting", 
                "contact": "Lisa Hall", 
                "description": "Join us for an informative Q&A session with our IT Support team, designed to address any technical questions or troubleshooting issues you may encounter as you settle into your new role. During this session, you will have the opportunity to ask questions about software, hardware, and other technology-related topics relevant to your work. The IT team will share tips on common issues and best practices for maintaining efficient technology use. This collaborative session aims to ensure you feel supported and equipped to handle any technical challenges, helping you navigate your tools with confidence and ease."}
            ]
        },
        "Day 4": {
            "Morning": [
                {"activity": "Client Portfolio Overview: Key Clients and Projects", 
                "contact": "Mark Allen", 
                "description": "In this session, you will receive an overview of our client portfolio, highlighting key clients and significant projects that our Localization Department has undertaken. We will discuss the unique needs and expectations of each client, the strategies we employed to meet those needs, and the outcomes of these collaborations. This overview will provide you with context on our client relationships and the importance of delivering high-quality localized content. Understanding our clients’ goals and past project successes will equip you with valuable insights as you begin to engage with our clients and contribute to ongoing projects."},
                {"activity": "Interactive Session: Understanding Client Requirements", 
                "contact": "Nancy Young", 
                "description": "This session will provide an interactive exploration into the nuances of gathering and interpreting client requirements, a critical component for ensuring project alignment and successful localization outcomes. You will engage in real-time scenarios and exercises that simulate direct client communication, requirement extraction, and scope clarification. The session will cover key areas such as managing client expectations, understanding source content complexity, localization quality benchmarks, and regional customization needs. By leveraging these exercises, you will gain proficiency in defining deliverables, setting clear localization objectives, and mitigating scope creep—all of which are vital for ensuring high client satisfaction and project success."}
            ],
            "Afternoon": [
                {"activity": "Workshop: Developing Client-Specific Strategies", 
                "contact": "Steven King", 
                "description": "In this hands-on workshop, you will collaborate with team members to develop tailored strategies for our key clients based on their unique needs and project goals. This session will guide you through the process of analyzing client profiles, identifying specific localization challenges, and brainstorming innovative solutions. You will learn how to leverage client feedback, market insights, and industry trends to create effective strategies that enhance client satisfaction and project outcomes. By the end of the workshop, you will have practical experience in crafting strategies that align with client expectations and ensure successful collaboration."},
                {"activity": "Role-Playing: Mock Client Meetings", 
                "contact": "Karen Wright", 
                "description": "In this interactive session, you will engage in role-playing exercises that simulate real client meetings. This activity is designed to help you practice key skills such as presenting project proposals, discussing client requirements, and managing expectations. You will have the opportunity to take on different roles—either as the client or the service provider—to gain diverse perspectives on the interaction process. Feedback will be provided by peers and facilitators, focusing on effective communication techniques, active listening, and building rapport. This hands-on experience will boost your confidence and prepare you for successful client interactions in your role."}
            ]
        },
        "Day 5": {
            "Morning": [
                {"activity": "Team Building Activities", 
                "contact": "Brian Scott", 
                "description": "Join us for a series of engaging team-building activities designed to foster collaboration, trust, and camaraderie among team members. These activities will provide an opportunity for you to connect with your colleagues in a fun and relaxed environment, promoting open communication and teamwork. Through a mix of problem-solving challenges, icebreakers, and collaborative exercises, you will build relationships and gain insights into each team member’s strengths and working styles. These experiences will not only enhance team dynamics but also help you feel more integrated into the team, setting a positive tone for your collaboration moving forward."},
                {"activity": "Networking Lunch with Cross-Functional Teams", 
                "contact": "Sandra Green", 
                "description": "Join us for a networking lunch that brings together members from various cross-functional teams. This informal gathering provides a unique opportunity to meet colleagues from different departments, share insights about their roles, and discuss collaborative projects. You will engage in meaningful conversations that can foster relationships, encourage knowledge sharing, and open up avenues for future collaboration. This event aims to enhance your understanding of how different teams contribute to the organization’s success and help you build a supportive professional network within the company."}
            ],
            "Afternoon": [
                {"activity": "Feedback Session: First Week Review with Onboarding Buddy", 
                "contact": "Kevin Adams", 
                "description": "In this session, you will meet with your Onboarding Buddy to reflect on your first week in the organization. This feedback session is designed to provide you with constructive insights regarding your experiences, challenges, and successes during your initial days. Your buddy will share observations, offer guidance, and address any questions you may have as you acclimate to your new role. Additionally, this session is an opportunity for you to express your thoughts on the onboarding process, ensuring that you feel supported and empowered as you move forward in your journey with the company."},
                {"activity": "Planning for the Upcoming Week", 
                "contact": "Megan Baker", 
                "description": "In this session, you will work collaboratively with your supervisor and team members to outline your objectives and priorities for the upcoming week. This planning activity will involve reviewing your current projects, setting actionable goals, and identifying key tasks that align with your role and team objectives. You will have the opportunity to discuss any challenges you anticipate and seek advice on strategies to overcome them. By the end of this session, you will have a clear roadmap for the week ahead, ensuring you stay focused and productive as you continue to integrate into your new role."}
            ]
        }
    },
    "Week 2": {
        "Day 6": {
            "Morning": [
                {"activity": "Workshop: Understanding Revenue and Profit Growth", 
                "contact": "Michael Brown", 
                "description": "This interactive workshop is designed to deepen your understanding of revenue and profit growth within our organization. You will explore key concepts related to financial performance, including the drivers of revenue, cost management, and profit margins. Through case studies and group discussions, we will analyze how effective strategies and decision-making can impact our financial success. Additionally, you will learn about our organization’s specific revenue goals and profit objectives, enabling you to see how your role contributes to the overall financial health of the company. By the end of this workshop, you will be equipped with valuable insights and tools to support our growth initiatives."},
                {"activity": "Interactive Budgeting Exercise", 
                "contact": "James Lewis", 
                "description": "Join us for an engaging interactive budgeting exercise that will help you understand the fundamentals of budgeting within our organization. In this session, you will work in teams to develop a mock budget based on given financial scenarios and organizational objectives. You will learn how to allocate resources effectively, prioritize spending, and make data-driven decisions that align with our strategic goals. This hands-on experience will enhance your understanding of the budgeting process and highlight the importance of financial planning in achieving revenue and profit growth. By the end of the exercise, you will have practical insights that you can apply in your role."}
            ],
            "Afternoon": [
                {"activity": "Case Study: Financial Reporting and Forecasting", 
                "contact": "Linda Robinson", 
                "description": "In this session, we will delve into a detailed case study focused on financial reporting and forecasting practices within our organization. You will analyze real-world financial reports, examining key metrics and performance indicators that drive business decisions. This interactive discussion will highlight the importance of accurate reporting and effective forecasting in achieving our financial goals. You will also explore the methodologies used for budget forecasting and how they impact strategic planning. By the end of this case study review, you will gain valuable insights into the role of financial analysis in guiding our organization’s growth and operational efficiency."},
                {"activity": "Meeting with Finance Team for Q&A", 
                "contact": "Barbara Rodriguez", 
                "description": "Join us for an interactive Q&A session with our Finance Team, designed to provide you with insights into the financial processes and practices that support our organization. During this meeting, you will have the opportunity to ask questions about financial reporting, budgeting, forecasting, and other key financial topics relevant to your role. The Finance Team will share their expertise, clarify any financial concepts, and discuss how their work impacts various departments within the organization. This session aims to enhance your understanding of our financial framework and foster collaboration between teams, ensuring you feel confident in navigating financial discussions in your role."}
            ]
        },
        "Day 7": {
            "Morning": [
                {"activity": "Interactive Session: Workflow Management Best Practices", 
                "contact": "Emily Johnson", 
                "description": "In this interactive session, you will explore workflow management best practices essential for enhancing productivity and efficiency in your role. Through collaborative discussions and practical exercises, you will learn about effective techniques for prioritizing tasks, streamlining processes, and managing project timelines. We will also cover tools and software that facilitate workflow management, enabling you to leverage technology to optimize your daily activities. By the end of this session, you will have actionable strategies to implement in your work, fostering a more organized and efficient approach to your projects."},
                {"activity": "Simulation: Managing a Complex Localization Project", 
                "contact": "David Clark", 
                "description": "In this hands-on simulation, you will experience the dynamics of managing a complex localization project from start to finish. You will work in teams to navigate various challenges, such as resource allocation, timeline management, and client communication. This exercise will simulate real-world scenarios, including unforeseen obstacles and shifting priorities, allowing you to apply your problem-solving skills in a controlled environment. Through guided discussions and feedback, you will learn best practices for coordinating localization efforts, ensuring quality control, and achieving project goals. By the end of the simulation, you will gain valuable insights into the intricacies of project management within the localization field."}
            ],
            "Afternoon": [
                {"activity": "Workshop: Continuous Improvement Strategies", 
                "contact": "Patricia Garcia", 
                "description": "Join us for a dynamic workshop focused on continuous improvement strategies that can enhance operational efficiency and effectiveness within our organization. This session will cover essential methodologies, such as Lean and Six Sigma, and provide practical tools for identifying areas for improvement in processes, workflows, and team performance. Through group activities and real-world case studies, you will learn how to implement feedback loops, measure outcomes, and foster a culture of ongoing development. By the end of the workshop, you will be equipped with actionable strategies to drive continuous improvement in your role, contributing to our overall organizational success."},
                {"activity": "Collaborative Session: Identifying Operational Bottlenecks", 
                "contact": "Chris Davis", 
                "description": "In this collaborative session, you will work alongside your colleagues to identify and analyze operational bottlenecks that may hinder workflow efficiency and productivity within our organization. Using brainstorming techniques and process mapping, you will examine current workflows, discuss pain points, and pinpoint areas where delays or obstacles occur. This interactive discussion will not only enhance your understanding of the operational landscape but also empower you to contribute ideas for potential solutions and improvements. By the end of the session, you will gain insights into effective strategies for streamlining processes and enhancing overall operational performance."}
            ]
        },
        "Day 8": {
            "Morning": [
                {"activity": "Interactive Workshop: Client Communication and Consultancy", 
                "contact": "John Doe", 
                "description": "Join us for an engaging workshop focused on enhancing your client communication and consultancy skills. This interactive session will cover essential techniques for effective client engagement, including active listening, needs assessment, and relationship-building strategies. You will participate in role-playing exercises that simulate client interactions, allowing you to practice conveying information clearly and addressing client concerns effectively. Additionally, we will explore best practices for providing consultancy services, ensuring you can offer valuable insights and solutions tailored to client needs. By the end of the workshop, you will feel more confident in your ability to communicate with clients and navigate consultancy scenarios successfully."},
                {"activity": "Role-Playing: Client Interaction Scenarios", 
                "contact": "Jane Smith", 
                "description": "In this interactive session, you will engage in role-playing exercises designed to simulate various client interaction scenarios you may encounter in your role. You will have the opportunity to take on different roles—either as the client or the service provider—to practice key skills such as effective communication, conflict resolution, and relationship management. Each scenario will focus on real-world situations, allowing you to apply strategies for addressing client needs, managing expectations, and delivering excellent service. Feedback will be provided by facilitators and peers, helping you refine your approach and build confidence in your client interactions. By the end of this session, you will be better prepared to navigate diverse client scenarios with professionalism and poise."}
            ],
            "Afternoon": [
                {"activity": "Case Study: Successful Client Management", 
                "contact": "Michael Brown", 
                "description": "In this session, we will examine a detailed case study showcasing successful client management strategies employed by our organization. You will analyze the factors that contributed to the success of a specific client relationship, including effective communication, proactive problem-solving, and tailored service delivery. This discussion will highlight best practices and lessons learned, emphasizing the importance of understanding client needs and building long-term partnerships. By reviewing this case study, you will gain valuable insights into the dynamics of client management and how to apply these strategies to your own work, ultimately enhancing client satisfaction and fostering successful collaborations."},
                {"activity": "Meeting with Sales Team for Collaboration Strategies", 
                "contact": "Emily Johnson", 
                "description": "Join us for a collaborative meeting with the Sales Team to discuss strategies for enhancing cooperation between departments. This session will focus on understanding the Sales Team’s objectives, challenges, and insights into client needs. You will explore how your role can support their efforts and contribute to achieving shared goals. The meeting will also cover best practices for communication and coordination, ensuring that both teams are aligned in their approaches to client engagement and service delivery. By the end of this session, you will have actionable strategies for effective collaboration, fostering a stronger partnership between the Localization and Sales Teams."}
            ]
        },
        "Day 9": {
            "Morning": [
                {"activity": "Training: KPI Management and Reporting", 
                "contact": "James Lewis", 
                "description": "In this training session, you will learn the fundamentals of Key Performance Indicator (KPI) management and reporting within our organization. We will cover the importance of KPIs in measuring success, tracking performance, and guiding decision-making processes. You will gain insights into how to select relevant KPIs, set measurable targets, and interpret data to assess progress against objectives. Additionally, we will explore best practices for reporting KPIs to stakeholders, ensuring that you can effectively communicate performance insights. By the end of this training, you will be equipped with the knowledge and tools necessary to manage KPIs and contribute to our organization’s strategic goals."},
                {"activity": "Interactive Session: Using Data to Drive Decisions", 
                "contact": "David Clark", 
                "description": "In this engaging session, you will explore how to leverage data effectively to inform and drive decision-making within your role. Through hands-on activities and group discussions, you will learn how to identify relevant data sources, analyze data trends, and interpret insights to make informed choices. We will cover various data analysis tools and techniques, demonstrating how to apply these methods to real-world scenarios. By the end of this session, you will gain confidence in using data to support your recommendations and strategies, ultimately enhancing your ability to contribute to our organization’s goals."}
            ],
            "Afternoon": [
                {"activity": "Collaborative Workshop: Developing a KPI Dashboard", 
                "contact": "Patricia Garcia", 
                "description": "Join us for a hands-on workshop where you will collaborate with your peers to design and develop a Key Performance Indicator (KPI) dashboard tailored to our organizational needs. In this session, you will learn about the key elements of an effective KPI dashboard, including data visualization techniques, metric selection, and user experience considerations. Working in teams, you will brainstorm and create mock-up dashboards that highlight critical performance metrics relevant to your roles. By the end of this workshop, you will have practical experience in dashboard development and a deeper understanding of how to utilize dashboards for tracking performance and informing decision-making within the organization."},
                {"activity": "Review Session with Direct Supervisor", 
                "contact": "Chris Davis", 
                "description": "In this one-on-one review session, you will meet with your direct supervisor to discuss your progress during the onboarding process. This is an opportunity to reflect on your experiences, clarify expectations, and assess how well you are adapting to your role. Your supervisor will provide constructive feedback on your performance thus far, highlight areas of strength, and identify opportunities for improvement. Additionally, you will have the chance to set short-term and long-term goals, ensuring alignment with the team's objectives. By the end of this session, you will gain valuable insights and a clear plan to enhance your performance moving forward."}
            ]
        },
        "Day 10": {
            "Morning": [
                {"activity": "One-on-One Feedback Session with Onboarding Buddy", 
                "contact": "John Doe", 
                "description": "In this personalized feedback session, you will meet with your Onboarding Buddy to discuss your experiences during the onboarding process. This informal meeting provides a safe space to share your thoughts, ask questions, and receive constructive feedback on your integration into the organization. Your buddy will offer insights based on their observations, helping you identify strengths and areas for growth. Additionally, this session is an opportunity to discuss any challenges you’ve faced and strategize on how to overcome them. By the end of this session, you will have a clearer understanding of your progress and actionable steps to enhance your onboarding experience."},
                {"activity": "Team Feedback Session: Sharing Insights and Improvements", 
                "contact": "Jane Smith", 
                "description": "Join us for a collaborative team feedback session where you will have the opportunity to share insights and discuss potential improvements related to the onboarding process. This open forum encourages all team members to reflect on their experiences, highlight successful strategies, and identify areas for enhancement. Through structured discussions and group activities, you will collectively brainstorm ideas to optimize the onboarding journey for future hires. By the end of this session, you will not only contribute to improving the onboarding experience but also foster a culture of open communication and continuous improvement within the team."}
            ],
            "Afternoon": [
                {"activity": "Personal Reflection and Goal Adjustment", 
                "contact": "Michael Brown", 
                "description": "In this session, you will take time to reflect on your onboarding experience and evaluate your progress toward the goals you’ve set. This structured reflection will involve assessing your achievements, identifying any challenges you’ve encountered, and considering what you’ve learned throughout the onboarding process. Based on your reflections, you will have the opportunity to adjust your goals to ensure they align with your personal and professional development aspirations. This session is designed to help you gain clarity on your objectives and create a tailored action plan for the upcoming weeks, fostering a proactive approach to your growth within the organization."},
                {"activity": "Planning for the Upcoming Week", 
                "contact": "Emily Johnson", 
                "description": "In this session, you will engage in planning activities to set clear objectives and priorities for the upcoming week. Together with your peers and onboarding buddy, you will outline key tasks, identify resources needed, and establish timelines to ensure a productive week ahead. This collaborative planning process will encourage you to align your goals with team objectives, allowing for better focus and efficiency. You will also discuss any potential challenges you might face and brainstorm strategies to overcome them. By the end of this session, you will leave with a well-structured plan that sets you up for success as you continue your onboarding journey."}
            ]
        }
    },
    "Week 3": {
        "Day 11": {
            "Morning": [
                {"activity": "Leadership Workshop: Leading Project Managers", 
                "contact": "Linda Robinson", 
                "description": "Join us for an engaging leadership workshop focused on developing the skills necessary to effectively lead project managers within our organization. In this interactive session, you will explore key leadership principles, such as fostering collaboration, motivating teams, and navigating challenges specific to project management. Through case studies, group discussions, and role-playing exercises, you will gain insights into best practices for empowering project managers to achieve their goals and drive successful project outcomes. This workshop will also provide you with tools for effective communication, conflict resolution, and performance management, equipping you to create a positive and productive work environment. By the end of the workshop, you will be better prepared to lead project managers and contribute to the overall success of our projects."},
                {"activity": "Role-Playing: Leadership Scenarios", 
                "contact": "Barbara Rodriguez", 
                "description": "In this interactive session, you will engage in role-playing exercises that simulate various leadership scenarios you may encounter in your role. By taking on different leadership positions, you will practice essential skills such as decision-making, conflict resolution, and team motivation. Each scenario will present unique challenges, allowing you to explore different leadership styles and approaches. Feedback will be provided by facilitators and peers, helping you refine your leadership techniques and enhance your ability to navigate complex situations effectively. By the end of this session, you will have practical experience and greater confidence in your leadership capabilities."}
            ],
            "Afternoon": [
                {"activity": "Mentorship Session with Senior Leaders", 
                "contact": "David Clark", 
                "description": "Join us for a valuable mentorship session where you will have the opportunity to engage with senior leaders within our organization. This session is designed to facilitate open dialogue, allowing you to gain insights from their experiences, challenges, and successes. You will have the chance to ask questions about career development, leadership strategies, and the organization’s vision. This interactive discussion will provide you with mentorship and guidance, helping you to understand the skills and attributes necessary for success in your role and future opportunities. By the end of this session, you will have established connections with senior leaders and gained valuable perspectives to inform your career path."},
                {"activity": "Collaborative Session: Developing Leadership Skills", 
                "contact": "Patricia Garcia", 
                "description": "In this interactive session, you will work alongside your peers to explore and develop essential leadership skills critical for success in your roles. Through group discussions, exercises, and case studies, you will identify key leadership competencies such as effective communication, team motivation, conflict resolution, and strategic thinking. This collaborative environment encourages sharing insights and experiences, fostering a rich learning experience. You will also create a personal development plan outlining specific leadership skills you wish to enhance, along with actionable steps to achieve your goals. By the end of this session, you will have a clearer understanding of your leadership style and the tools necessary for continued growth within the organization."}
            ]
        },
        "Day 12": {
            "Morning": [
                {"activity": "Interactive Session: Best Practices in Global Partnership", 
                "contact": "Chris Davis", 
                "description": "Join us for an engaging interactive session focused on best practices for cultivating and maintaining successful global partnerships. In this session, you will learn about the key elements that contribute to effective collaboration across diverse cultures and regions, including communication strategies, relationship management, and cultural sensitivity. Through case studies and group activities, you will explore real-world examples of successful global partnerships and identify actionable strategies for building trust and fostering collaboration. Participants will also have the opportunity to share their experiences and insights, enhancing the collective knowledge of the group. By the end of this session, you will be equipped with practical tools and strategies to strengthen global partnerships and drive successful outcomes."},
                {"activity": "Case Study: Successful Partnerships", 
                "contact": "John Doe", 
                "description": "In this session, we will analyze a detailed case study highlighting successful global collaborations undertaken by our organization or industry peers. You will explore the strategies, frameworks, and practices that contributed to these collaborations, examining the challenges faced and how they were overcome. This discussion will cover critical elements such as cross-cultural communication, shared goals, and effective project management. By reviewing these real-world examples, you will gain valuable insights into what makes global partnerships successful and how to apply these lessons to your own work. By the end of the session, you will be better equipped to navigate and contribute to global collaborations within our organization."}
            ],
            "Afternoon": [
                {"activity": "Workshop: Creating and Managing Partnerships", 
                "contact": "Jane Smith", 
                "description": "This interactive workshop focuses on the critical components of partnership development and management. Participants will learn how to identify potential partners, negotiate terms, and foster long-term relationships. The session will include practical exercises, group discussions, and case studies to illustrate best practices in partnership management."},
                {"activity": "Networking Event with Global Partners", 
                "contact": "Michael Brown", 
                "description": "Join us for a unique opportunity to network with our global partners. This session is designed to facilitate meaningful connections, allowing you to engage in discussions, share insights, and explore potential collaborations. You'll have the chance to learn from experienced partners and establish valuable relationships that can enhance your professional journey."}
            ]
        },
        "Day 13": {
            "Morning": [
                {"activity": "Training: Effective Stakeholder Management", 
                "contact": "James Lewis", 
                "description": "This training session is designed to equip participants with essential skills and strategies for effectively managing stakeholders. Understanding stakeholder needs and expectations is crucial for project success and organizational growth."},
                {"activity": "Simulation: Stakeholder Engagement Scenarios", 
                "contact": "Emily Johnson", 
                "description": "Implementing Improvement Strategies: In this hands-on simulation, you will engage in a realistic scenario that challenges you to implement improvement strategies within a simulated work environment. Working in teams, you will be presented with a set of operational challenges that require innovative solutions and effective application of continuous improvement techniques. Throughout the simulation, you will analyze data, identify areas for enhancement, and develop actionable strategies to optimize processes. This interactive experience will allow you to practice decision-making, collaboration, and problem-solving skills in a controlled setting. By the end of the simulation, you will gain valuable insights into the complexities of implementing improvement strategies and the impact they can have on organizational success."}
            ],
            "Afternoon": [
                {"activity": "Case Study: Stakeholder Management Successes", 
                "contact": "David Clark", 
                "description": "Identifying and Solving Operational Issues: Join us for an engaging workshop focused on identifying and solving operational issues within our organization. In this interactive session, you will learn to recognize common operational challenges and apply problem-solving techniques to address them effectively. Through group discussions, real-world case studies, and hands-on activities, you will collaborate with your peers to analyze operational workflows, pinpoint inefficiencies, and develop actionable solutions. This workshop will also emphasize the importance of data analysis and holder feedback in identifying issues and measuring the impact of proposed solutions. By the end of this session, you will be equipped with practical skills and strategies to enhance operational efficiency and drive continuous improvement within your team."},
                {"activity": "Meeting with Stakeholders for Feedback", "contact": "Patricia Garcia", "description": "Gather feedback from stakeholders."},
            ]
        },
        "Day 14": {
            "Morning": [
                {"activity": "Training: Risk Management Strategies", 
                "contact": "Linda Robinson", 
                "description": "In this comprehensive training session, you will delve into advanced techniques for continuous improvement that drive efficiency and innovation within the organization. This workshop will cover methodologies such as Lean, Six Sigma, and Agile, equipping you with tools and frameworks to identify areas for improvement and implement effective solutions. Through interactive exercises, case studies, and group discussions, you will learn how to analyze processes, eliminate waste, and enhance quality in your work. Participants will also have the opportunity to collaborate on real-world scenarios, applying the techniques learned to develop actionable improvement plans. By the end of this training, you will be better prepared to foster a culture of continuous improvement and contribute to the organization’s ongoing success."},
                {"activity": "Workshop: Creating a Risk Management Plan", 
                "contact": "Barbara Rodriguez", 
                "description": "This workshop is designed to provide participants with the knowledge and tools necessary to create an effective risk management plan. Participants will learn how to identify potential risks, assess their impact, and develop strategies to mitigate them."}
            ],
            "Afternoon": [
                {"activity": "Collaborative Session: Identifying Potential Risks", 
                "contact": "Chris Davis", 
                "description": "By the end of this session, you will be equipped with practical skills and strategies to enhance operational efficiency and drive continuous improvement within your team."},
                {"activity": "Feedback Session: Learning from Past Projects", 
                "contact": "John Doe", 
                "description": "In this important feedback session, you will meet one-on-one with your direct supervisor to discuss your performance, progress, and experiences during the onboarding process. This session will provide an opportunity to receive constructive feedback on your contributions and clarify any expectations moving forward. You will also have the chance to share your thoughts on your onboarding experience, ask questions, and discuss any challenges you may have faced. This collaborative discussion aims to foster open communication and ensure that you feel supported in your role. By the end of this session, you will have actionable insights to guide your development and enhance your contributions to the team."}
            ]
        },
        "Day 15": {
            "Morning": [
                {"activity": "Team Building: Collaboration and Communication", 
                "contact": "Jane Smith", 
                "description": "Engage in team-building activities to foster collaboration."},
                {"activity": "Networking Lunch with Leadership Team", 
                "contact": "Michael Brown", 
                "description": "Join us for a special networking lunch with the leadership team, providing you with a unique opportunity to connect with key decision-makers in the organization. This informal setting encourages open conversations, allowing you to engage with leaders, ask questions, and gain insights into the company’s vision and goals."}
            ],
            "Afternoon": [
                {"activity": "Reflection Session: Third Week Review", 
                "contact": "James Lewis", 
                "description": "In this session, you will take time to reflect on your experiences during the onboarding process and assess your progress towards the goals you set at the beginning. This reflective practice will allow you to evaluate what has worked well, identify areas for improvement, and consider any challenges you've faced. You will also have the opportunity to adjust your personal and professional goals based on your insights and the feedback received from your supervisor and onboarding buddy. This session emphasizes the importance of self-awareness and adaptability in your career development. By the end of this session, you will have a refined set of goals that align with your learning journey and a clearer path forward in your role."},
                {"activity": "Planning for the Final Week", 
                "contact": "Emily Johnson", 
                "description": "In this session, you will collaboratively strategize and outline your objectives for the upcoming week, focusing on priorities and actionable tasks that align with your role and responsibilities. You will reflect on your experiences so far and incorporate feedback received from your supervisor and team members to create a clear and structured plan. This planning session will encourage you to set realistic goals, identify potential challenges, and allocate time effectively to ensure a productive week ahead. By the end of this session, you will leave with a concrete plan that enhances your focus, supports your ongoing development, and facilitates smoother integration into your team."}
            ]
        }
    },
    "Week 4": {
        "Day 16": {
            "Morning": [
                {"activity": "Final Review of Onboarding Goals", 
                "contact": "David Clark", 
                "description": "In this comprehensive review session, you will revisit the tools, processes, and strategies introduced during your onboarding. This interactive session aims to consolidate your understanding of how each element contributes to your role and the organization’s objectives. You will have the opportunity to ask questions, clarify any uncertainties, and discuss how these tools can be effectively utilized in your day-to-day tasks. Participants will engage in group discussions to share experiences and best practices, fostering a collaborative learning environment. By the end of this session, you will feel more confident in navigating the resources available to you and applying the strategies learned to enhance your performance and productivity."},
                {"activity": "One-on-One with Supervisor to Discuss Progress", 
                "contact": "Patricia Garcia", 
                "description": "Discussion with your supervisor about your progress."}
            ],
            "Afternoon": [
                {"activity": "Training: Advanced Project Management Techniques", 
                "contact": "Chris Davis", 
                "description": "In this collaborative session, you will work with your colleagues to finalize strategies tailored specifically for our key clients. Building on the insights gathered in previous meetings and workshops, this interactive session will focus on refining and solidifying the approaches that best meet client needs and objectives. You will engage in group discussions to address any outstanding challenges, brainstorm innovative solutions, and ensure alignment with overall organizational goals. Participants will collaborate to develop comprehensive, actionable plans that enhance client satisfaction and drive successful outcomes. By the end of this session, you will have a clear and strategic framework ready to implement, fostering stronger client relationships and contributing to our success."},
                {"activity": "Collaborative Workshop: Finalizing Project Plans", 
                "contact": "John Doe", 
                "description": "In this collaborative session, you will engage with your peers to share constructive feedback and identify opportunities for improvement in both individual and team performance. This open forum encourages honest dialogue and fosters a supportive atmosphere where everyone can share insights on challenges faced and strategies for overcoming them. Participants will discuss their experiences, exchange ideas, and provide feedback on each other's work, focusing on key areas for growth. By the end of this session, you will have gained valuable perspectives that can enhance your skills and contribute to a culture of continuous improvement within the team."}
            ]
        },
        "Day 17": {
            "Morning": [
                {"activity": "Workshop: Presentation Skills for Project Leaders", 
                "contact": "Jane Smith", 
                "description": "Workshop to enhance your presentation skills."},
                {"activity": "Role-Playing: Presenting to Stakeholders",
                "contact": "Michael Brown", 
                "description": "Join us for an interactive workshop designed to enhance your advanced communication skills, essential for effective collaboration and relationship-building within the organization. In this session, you will explore various communication techniques, including active listening, persuasive messaging, and non-verbal cues. Through role-playing exercises, group discussions, and real-world scenarios, you will practice these skills in a supportive environment, gaining valuable feedback from peers and facilitators. This workshop will also cover strategies for navigating difficult conversations and fostering open dialogue with clients and team members. By the end of this workshop, you will feel more confident in your ability to communicate effectively and impactfully in diverse situations."}
            ],
            "Afternoon": [
                {"activity": "Feedback Session: Practice Presentations", 
                "contact": "James Lewis", 
                "description": "In this engaging role-playing session, you will simulate real-world scenarios that require risk analysis and effective decision-making skills. Participants will be assigned various roles that reflect different stakeholders, allowing you to explore diverse perspectives and the complexities involved in risk management. Through guided exercises, you will assess potential risks, weigh options, and make decisions based on data and stakeholder input. This interactive approach will enhance your critical thinking and problem-solving abilities, providing practical experience in navigating uncertainty and making informed choices. By the end of this session, you will have a deeper understanding of the decision-making process and the importance of thorough risk analysis in achieving successful outcomes."},
                {"activity": "Networking with Team Members", "contact": "Emily Johnson", "description": "Opportunity to network with team members."}
            ]
        },
        "Day 18": {
            "Morning": [
                {"activity": "Training: Conflict Resolution Strategies", 
                "contact": "David Clark", 
                "description": "Learn effective conflict resolution strategies."},
                {"activity": "Case Study: Resolving Conflicts in Teams", 
                "contact": "Patricia Garcia", 
                "description": "Analyze case studies on conflict resolution."}
            ],
            "Afternoon": [
                {"activity": "Workshop: Building a Positive Team Culture", 
                "contact": "Chris Davis", 
                "description": "Workshop on fostering a positive team culture."},
                {"activity": "Final Q&A Session with Leadership", 
                "contact": "John Doe", 
                "description": "In this essential final review session, you will meet with your direct supervisor and onboarding buddy to reflect on your onboarding journey and assess your progress. This collaborative discussion will focus on your achievements, areas for growth, and the feedback you've received throughout the onboarding process. You will have the opportunity to ask questions, clarify expectations, and outline your development plan moving forward. Together, you will discuss any adjustments needed to your goals and strategies to ensure continued success in your role. By the end of this session, you will have a clear understanding of your next steps, a renewed sense of direction, and the support needed to thrive in your position."}
            ]
        },
        "Day 19": {
            "Morning": [
                {"activity": "Interactive Session: Preparing for Go-Live", 
                "contact": "Jane Smith", 
                "description": "In this collaborative session, you will work alongside your team to assess and ensure all preparations are in place for the upcoming project launch. This interactive discussion will focus on key areas such as resource allocation, timeline adherence, quality assurance, and risk management. You will engage in group exercises to identify any potential gaps or challenges and develop contingency plans to address them. By leveraging collective insights and experiences, this session aims to foster a proactive approach to problem-solving and collaboration. By the end of this session, you will feel confident in the team’s readiness to go live, with a clear understanding of roles, responsibilities, and next steps for a successful launch."},
                {"activity": "Mock Go-Live Exercise", 
                "contact": "Michael Brown", 
                "description": "Participate in a mock go-live exercise."}
            ],
            "Afternoon": [
                {"activity": "Reflection and Celebration of Onboarding Journey", 
                "contact": "James Lewis", 
                "description": "Reflect on your journey and celebrate achievements."},
                {"activity": "Feedback Session: Onboarding Experience", 
                "contact": "Emily Johnson", 
                "description": "In this session, you will learn about the various support mechanisms available to you through your onboarding buddy and the broader team. Your onboarding buddy will serve as your primary resource for guidance, offering insights into the company culture, processes, and best practices to help you navigate your new role. Additionally, the team will be encouraged to foster an open environment where questions and collaboration are welcomed"}
            ]
        },
        "Day 20": {
            "Morning": [
                {"activity": "Final Check-in with Onboarding Buddy", 
                "contact": "David Clark", 
                "description": "Final check-in with your onboarding buddy."},
                {"activity": "Set Future Development Goals", 
                "contact": "Patricia Garcia", 
                "description": "Set personal and professional development goals."}
            ],
            "Afternoon": [
                {"activity": "Wrap-Up Meeting with Leadership Team", 
                "contact": "Chris Davis", 
                "description": "Final meeting with the leadership team."},
                {"activity": "Celebration of Completion of Onboarding Program", 
                "contact": "John Doe", 
                "description": "Join us for a celebratory team event to commemorate the successful completion of your onboarding journey and to foster team bonding! This informal gathering will provide an opportunity to connect with your colleagues, share experiences, and celebrate achievements. Activities may include team-building games, recognition of contributions, and light refreshments, creating a relaxed atmosphere for networking and relationship-building. This event not only marks a significant milestone in your onboarding but also strengthens the team spirit and encourages a sense of belonging within the organization. By the end of this event, you will feel more integrated into the team and ready to contribute to our collective success."}
            ]
        }
    }
}



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
    st.title("Program Manager Onboarding plan")
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
