import { useState } from "react";
import CandidateCard from "../components/CandidateCard";
import { rankCandidates } from "../services/api";

function Dashboard() {
  const [jd, setJd] = useState("");
  const [candidates, setCandidates] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    try {
      setLoading(true);

      const data = await rankCandidates(jd);

      setCandidates(data.candidates.slice(0, 5));
    } catch (error) {
      console.error(error);
      alert("Error fetching candidates");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <div className="max-w-7xl mx-auto p-10">

        <h1 className="text-6xl font-bold text-center mb-4">
          AI Candidate Ranking System
        </h1>

        <p className="text-center text-slate-400 mb-10">
          Semantic Candidate Discovery using AI + FAISS
        </p>

        <div className="bg-slate-900 p-6 rounded-2xl shadow-xl">

          <textarea
            className="w-full h-64 bg-slate-800 text-white p-4 rounded-xl border border-slate-700"
            placeholder="Paste Job Description Here..."
            value={jd}
            onChange={(e) => setJd(e.target.value)}
          />

          <div className="flex justify-center mt-6">
            <button
              onClick={handleAnalyze}
              className="bg-blue-600 hover:bg-blue-700 px-8 py-3 rounded-xl font-semibold"
            >
              Analyze Candidates
            </button>
          </div>
        </div>

        {loading && (
          <div className="text-center mt-10">
            <h2 className="text-2xl animate-pulse">
              🔍 Analyzing Candidates...
            </h2>
          </div>
        )}

        {candidates.length > 0 && (
          <div className="mt-12">
            <h2 className="text-4xl font-bold mb-8">
              Top Candidates
            </h2>

            <div className="grid grid-cols-1 gap-6">
              {candidates.map((candidate, index) => (
                <CandidateCard
                  key={candidate.candidate_id}
                  candidate={candidate}
                  rank={index + 1}
                />
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Dashboard;