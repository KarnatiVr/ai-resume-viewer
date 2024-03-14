# AI-resume-viewer


**Description**:  
This application allows users to upload their resume files and receive feedback on them using the Gemini model. Users can submit their resume files in pdf format and receive personalized feedback based on the content of their resumes.

The application integrates the Gemini model to provide feedback on resumes, offering suggestions for improvement, highlighting strengths, and identifying areas for development. It aims to assist users in enhancing their resumes to better showcase their skills and experiences.

**Features**:  
- Resume Upload: Users can upload their resume files through the web interface.
- Gemini Integration: The application integrates the Gemini model to analyze resumes and provide feedback.
- Feedback Generation: ChatGPT generates personalized feedback based on the content of the uploaded resumes.
- User-Friendly Interface: The application offers a simple and intuitive interface for users to upload their resumes and view feedback.

**Prerequisites**:  

Docker - if not installed click [here](https://docs.docker.com/engine/install/) to install.  
GIT - if not installed click [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install.  
Code editor of your choice.

**Clone the Repo**:
```
# SSH
git clone git@github.com:KarnatiVr/ai-resume-viewer.git

#HTTPS
git clone https://github.com/KarnatiVr/ai-resume-viewer.git

```
**Start the Docker Daemon**

**Run these commands**:  
```
cd lean-technologies

#run this command in the project root directory && build the Image
docker compose build

#run these containers
docker compose up

```

**Open the terminal inside the app container in docker**:


