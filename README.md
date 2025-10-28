# LangGraph + LangChain Transcription Fast Api

This app transcribes audio/video files into text using **OpenAI Whisper** and orchestrates tasks via **LangGraph**.

---

## 🚀 Features

- Upload audio/video file (`.mp3`, `.mp4`, `.wav`, etc.)
- Auto audio extraction for videos
- Transcription via Whisper API
- Optional summarization via ChatGPT
- Outputs `.txt` file saved locally
- Built with FastAPI + LangGraph

---

## 🧰 Setup

```bash
git clone <repo-url>
cd langgraph_transcriber
cp .env.example .env
pip install -r requirements.txt
```
