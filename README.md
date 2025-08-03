# Educational RAG Chatbot with Django Admin & Discord Interface

## Overview
This project implements a **Retrieval-Augmented Generation (RAG)** chatbot system tailored for education. Students interact with course materials via a **Discord bot**, while educators manage content and enrollments through a **Django-based admin panel**.

The chatbot answers student queries by retrieving relevant course documents uploaded by educators and generating responses using **Gemini Flash 2.0**.

---

## Key Features

### For Students (Discord bot)
- Enroll in courses with simple commands
- Ask course-related questions answered by AI using educator-uploaded content
- Change active courses anytime
- View current enrollment status and available courses

### For Educators (Django Admin)
- Upload and manage course documents (PDFs, texts)
- Manage courses and metadata
- View and optionally manage student enrollments
- Access limited admin features based on roles

### For Admins (Django Admin)
- Full data and user management
- Assign educator roles and permissions
- System configuration and monitoring

---

## Technology Stack

| Layer              | Technology                          | Purpose                                      |
|--------------------|-----------------------------------|----------------------------------------------|
| Chat Interface     | Discord Bot (`discord.py`)          | Student interaction via chat commands        |
| Backend Framework  | Django + Django REST Framework      | User, course, enrollment management & admin |
| Auth & Roles       | Django Groups & Permissions         | Separate admin and educator access levels    |
| Document Storage   | Django FileField                    | Store PDFs and course-related documents      |
| Document Processing| PyMuPDF or pdfplumber               | Extract and chunk text from PDFs              |
| Embeddings        | `sentence-transformers` (local model) | Convert text chunks & queries to vectors      |
| Vector Database    | Chroma (Docker container)           | Store and search vectorized documents         |
| LLM Generation    | Gemini Flash 2.0 (via Google AI Studio/Colab) | Generate answers from retrieved context        |
| Containerization   | Docker + Docker Compose             | Run backend and vector DB locally              |

---

## User & Educator Flow

### Student Flow (Discord)
1. Join Discord server and interact with the bot  
2. Use `!enroll <course_code>` to enroll in a course  
3. Ask questions via `!ask <question>`, bot responds using course materials  
4. Switch courses with `!change_course <course_code>`  
5. Check active course with `!my_course`  
6. View available courses with `!courses`  

### Educator Flow (Django Admin)
1. Login to Django admin panel  
2. Create and manage courses  
3. Upload course documents  
4. Optionally manage student enrollments  
5. Assign or invite educators, manage permissions  
6. Upload triggers embedding and vector DB updates (background task)  

---

## Discord Commands

| Command                  | Description                          | Example                 |
|--------------------------|------------------------------------|-------------------------|
| `!enroll <course_code>`  | Enroll in a course                  | `!enroll 345EQ`         |
| `!ask <question>`        | Ask question related to active course | `!ask What is binary search?` |
| `!change_course <course_code>` | Change active course            | `!change_course TQAF4`  |
| `!my_course`             | Show active enrolled course         | `!my_course`            |
| `!courses`               | List all available courses           | `!courses`              |
| `!help`                  | Show help text with commands         | `!help`                 |

---

## Summary
This scalable, modular educational chatbot system combines:

- A student-friendly **Discord interface** for conversational Q&A  
- A robust **Django admin backend** empowering educators with easy content management  
- Advanced **RAG architecture** integrating embeddings, vector search (Chroma), and large language models (Gemini)  
- **Role-based access control** distinguishing admins and educators for secure management  

---
