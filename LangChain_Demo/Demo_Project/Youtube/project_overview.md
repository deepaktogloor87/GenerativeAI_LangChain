# 🎥 YouTube RAG Chat App (LangChain + Transcript API)

An AI-powered application that allows users to **chat with any YouTube video** using a Retrieval-Augmented Generation (RAG) pipeline.

Instead of watching long videos, users can **ask questions and get precise answers instantly**.

---

## 🚀 Features

- 🔗 Input any YouTube video URL
- 📜 Automatically fetch transcript using `youtube-transcript-api`
- ✂️ Smart text chunking with LangChain
- 🧠 Embedding-based semantic search
- 🗄️ Vector storage (FAISS / Chroma)
- 💬 Natural language Q&A over video content
- ❌ Handles "Not discussed in video" cases
- ⚡ Extensible with memory, streaming, and hybrid search

---

## 🧠 Architecture Overview
![arc_diagram](../Youtube/mermaid-diagram%20(1).png)


---

## 🏗️ Tech Stack

- **LangChain** → Orchestration
- **YouTube Transcript API** → Data source
- **Sentence Transformers / OpenAI Embeddings** → Embeddings
- **FAISS / ChromaDB** → Vector storage
- **OpenAI / LLM** → Answer generation
- **Python** → Core backend

---

## 📦 Installation

```bash
pip install langchain youtube-transcript-api faiss-cpu sentence-transformers openai

# 🎥 YouTube RAG Chat App — Phase-by-Phase Implementation Guide

This guide walks you through **building the system step-by-step**, with clear goals, tasks, and expected outputs for each phase.

---

# 🧠 High-Level Flow
YouTube → Transcript → Chunking → Embeddings → Vector DB
User Query → Retrieval → LLM → Answer


---

# 🚀 Phase 0: Project Setup

## 🎯 Goal
Prepare environment and dependencies

## 📦 Install Dependencies

```bash
pip install langchain youtube-transcript-api faiss-cpu sentence-transformers openai

project/
│── main.py
│── config.py
│── requirements.txt
│
├── src/
│   ├── input/
│   ├── processing/
│   ├── retrieval/
│   ├── llm/
│   ├── agent/
│
└── utils/

# 🔹 Phase 1: Input Handling (YouTube Transcript)
🎯 Goal

Extract transcript from YouTube video

🛠 Steps
Accept YouTube URL
Extract video ID
Fetch transcript using API

🔹 Phase 2: Data Processing (Cleaning + Chunking)
🎯 Goal

Convert transcript into structured chunks

🛠 Steps
Merge transcript text
Preserve timestamps
Split into chunks using LangChain

🔹 Phase 3: Embeddings + Vector Database
🎯 Goal

Convert text into vectors and store for retrieval

🛠 Steps
Load embedding model
Convert chunks → embeddings
Store in FAISS

🔹 Phase 4: Query Processing + Retrieval
🎯 Goal

Find relevant chunks based on user query

🛠 Steps
Convert query → embedding
Perform similarity search
Retrieve Top-K chunks

🔹 Phase 5: RAG (LLM Integration)
🎯 Goal

Generate final answer using retrieved context

🛠 Steps
Combine retrieved chunks
Create prompt
Send to LLM

🔹 Phase 6: Decision Engine
🎯 Goal

Validate if answer is relevant

🛠 Steps
Check similarity score
Apply threshold
Decide response

🔹 Phase 7: Main Agent (Orchestration)
🎯 Goal

Connect all components

🧪 Phase 8: Run the App

# Future enhancement plan
✅ Convert this into **LangChain LCEL (latest standard)**  
✅ Add **real OpenAI integration (production ready)**  
✅ Build **UI + deploy on HuggingFace / Vercel**  
✅ Add **timestamps + clickable video player** 🎯