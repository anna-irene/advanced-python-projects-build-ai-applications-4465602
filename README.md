>  This is a fork of [Advanced python projects : Build AI applications-4465602](https://github.com/honeypadre/advanced-python-projects-build-ai-applications-4465602).  
> I made improvements to the file `begin/temp/CH_1_NLP_Chatbot.py` as part of my learning from the LinkedIn course:  
> **“Advanced Python Projects: Build AI Applications” by [Priya Mohan](https://www.linkedin.com/learning/instructors/priya-mohan)**.  
>  See [Chatbot with Sentiment Analysis](#chatbot-with-sentiment-analysis) below for details.



# Advanced Python Projects: Build AI Applications
This is the repository for the LinkedIn Learning course `Advanced Python Projects: Build AI Applications`. The full course is available from [LinkedIn Learning][lil-course-url].

![lil-thumbnail-url]

Python is a versatile programming language that is widely used in a variety of industries, including data science, artificial intelligence, web development, and more. As the demand for Python developers continues to grow, having a portfolio of Python projects can significantly increase your job prospects and marketability. This course with instructor Priya Mohan is designed to equip you with the skills and knowledge needed to create a portfolio of Python-based applications and tools that can be showcased to employers or used to bring your own ideas to life. It’s ideal for anyone looking to enhance their Python knowledge by completing hands-on projects or for those seeking to create interesting solutions from scratch for fun.

This course is integrated with GitHub Codespaces, an instant cloud developer environment that offers all the functionality of your favorite IDE without the need for any local machine setup. With GitHub Codespaces, you can get hands-on practice from any machine, at any time—all while using a tool that you’ll likely encounter in the workplace. Check out the “Using GitHub Codespaces with this course” video to learn how to get started.

## Instructions
All of the course files are stored in the main branch. There are 2 folders in the main branch called "Begin" and "Finish". The Start folder contains semi-completed code files you can start working on while watching the LinkedIn Learning course. The Finish folder contains completed code files. The naming convention is `CHAPTER_#_ProjectName`. As an example, the first project is labeled "CH_1_NLP_ChatBot".

Happy Coding!

### Instructor

Priya Mohan

Management Consultant, KPMG

Please follow me on LinkedIn: https://www.linkedin.com/in/priya123mohan

[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/advanced-python-projects-build-ai-applications
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D560DAQHIPR3VAGQGiQ/learning-public-crop_675_1200/0/1713466120470?e=2147483647&v=beta&t=on84QImWhMSkQjBq4E8OiW9BuJeJ7vP_Np1ZmCkhtzo


---

## Chatbot with Sentiment Analysis

This is a simple terminal-based chatbot that uses sentiment analysis to understand and respond to user emotions. Built with Python and [TextBlob](https://textblob.readthedocs.io/en/dev/), it simulates empathetic responses based on the mood of the message.

---

## My Contributions

**Modified File**: `begin/temp/CH_1_NLP_Chatbot.py`  
**Original Version**: `finish/temp/CH_1_NLP_Chatbot.py`

###  Enhancements:
- Added a user-friendly **exit option** to allow quitting with “bye”, “exit”, or “quit”.
- Implemented **empty input handling** so the chatbot prompts the user instead of staying silent.
- Included **manual sentiment override** using predefined positive/negative keyword lists for more accurate emotional responses.

  
## Sample Interaction
bash
```
ChatBot: Hi, how can I help you?
You: I'm hurt
ChatBot: I'm sorry to hear that. What can I do to help? 😔
Sentiment score: -1.0

You: Actually I'm feeling awesome now!
ChatBot: That's great to hear! 😊
Sentiment score: 1.0
```
These changes were made while following the course  
**“Advanced Python Projects: Build AI Applications” by [Priya Mohan](https://www.linkedin.com/learning/instructors/priya-mohan)** on LinkedIn Learning.



