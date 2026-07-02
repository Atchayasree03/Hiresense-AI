import { useState } from "react";
import API from "./services/api";
import CandidateModal from "./components/CandidateModal";
import CandidateTable from "./components/CandidateTable";
import { saveAs } from "file-saver";
import { Routes, Route } from "react-router-dom";
import CandidateDetails from "./pages/CandidateDetails";
function App() {
  const [jd, setJd] = useState("");
  const [candidates, setCandidates] = useState([]);
  const [loading, setLoading] = useState(false);
  const [shortlisted, setShortlisted] = useState([]);
  const analyzeCandidates = async () => {
    try {
      setLoading(true);

      const response = await API.post("/rank", {
        jd,
      });

      setCandidates(response.data.candidates);
    } catch (error) {
      console.error(error);
      alert("Failed to rank candidates");
    } finally {
      setLoading(false);
    }
  };

  const exportCSV = () => {

  const rows = candidates.map((c, index) => {

    const reasoning =
      `${c.headline}. ` +
      `Matched Skills: ${c.matched_skills.join(", ")}.`;

    return `"${c.candidate_id}",${index + 1},${(
      c.match_score / 100
    ).toFixed(3)},"${reasoning}"`;

  });

  const csv =
    `candidate_id,rank,score,reasoning\n${rows.join("\n")}`;

  const blob = new Blob(
    [csv],
    {
      type: "text/csv;charset=utf-8;"
    }
  );

  saveAs(blob, "submission.csv");
};
  const shortlistCandidate = (candidate) => {
  setShortlisted((prev) => {
    if (
      prev.find(
        (c) =>
          c.candidate_id === candidate.candidate_id
      )
    ) {
      return prev;
    }

    return [...prev, candidate];
  });
};

  const avgScore =
    candidates.length > 0
      ? (
          candidates.reduce(
            (sum, c) => sum + c.match_score,
            0
          ) / candidates.length
        ).toFixed(2)
      : 0;

  const excellentMatches =
    candidates.filter(
      (c) => c.match_score >= 60
    ).length;

    return (
  <Routes>

    <Route
      path="/"
      element={
        <div className="min-h-screen bg-slate-100 p-8">
          <div className="max-w-7xl mx-auto">

            <h1 className="text-5xl font-bold text-center mb-8">
              Redrob AI Talent Intelligence
            </h1>

            <div className="bg-white rounded-xl shadow-lg p-6">

              <textarea
                rows={10}
                value={jd}
                onChange={(e) => setJd(e.target.value)}
                placeholder="Paste Job Description..."
                className="w-full border rounded-lg p-4"
              />

              <div className="flex gap-4 mt-4">

                <button
                  onClick={analyzeCandidates}
                  className="bg-blue-600 text-white px-8 py-3 rounded-lg"
                >
                  {loading
                    ? "Analyzing..."
                    : "Analyze Candidates"}
                </button>

                {candidates.length > 0 && (
                  <button
                    onClick={exportCSV}
                    className="bg-purple-600 text-white px-6 py-3 rounded-lg"
                  >
                    Export CSV
                  </button>
                )}

              </div>

            </div>

            {candidates.length > 0 && (
              <>
                <div className="grid grid-cols-4 gap-4 mt-8"> 
                </div>

                <CandidateTable
                    candidates={candidates}
                    onShortlist={shortlistCandidate}
                />

              </>
            )}

          </div>
        </div>
      }
    />

    <Route
      path="/candidate/:id"
      element={<CandidateDetails />}
    />

  </Routes>
);

 
}

export default App;