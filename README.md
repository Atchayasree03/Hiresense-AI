#CLONE THE REPOSITORY
git clone https://github.com/Atchayasree03/Hiresense-AI.git

#FRONTEND
cd Hiresense-AI
cd frontend
npm create vite@latest
npm install
npm run dev

#BACKEND
cd Hiresense-AI
cd backend
venv\Scripts\activate
pip install fastapi uvicorn pandas numpy sentence-transformers faiss-cpu scikit-learn tqdm python-dotenv pydantic python-multipart
uvicorn api:app --reload

Wait until you see :

INFO:     Will watch for changes in these directories: ['C:\\Users\\DHARSAN\\Documents\\AI hackathon\\AI hackathon\\redrob-ai api version\\backend']
Loading weights: 100%|█████████████████████████████████████████████████████████████| 103/103 [00:00<00:00, 4318.75it/s]
Loading Candidates: 100000it [00:08, 11698.56it/s]
Loading weights: 100%|█████████████████████████████████████████████████████████████| 103/103 [00:00<00:00, 4364.26it/s]
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [17476] using StatReload
Loading weights: 100%|█████████████████████████████████████████████████████████████| 103/103 [00:00<00:00, 3835.65it/s]
Loading Candidates: 100000it [00:09, 10523.81it/s]
Loading weights: 100%|█████████████████████████████████████████████████████████████| 103/103 [00:00<00:00, 4132.32it/s]
INFO:     Started server process [19008]
INFO:     Waiting for application startup.
INFO:     Application startup complete.


Then open http://localhost:5173/
Paste JD and Analyze Candidate

No need to generate any file and embeddings using Python scripts
