const shortlistCandidate = () => {

  const shortlisted =
    JSON.parse(
      localStorage.getItem(
        "shortlisted"
      ) || "[]"
    );

  shortlisted.push(candidate);

  localStorage.setItem(
    "shortlisted",
    JSON.stringify(shortlisted)
  );

  alert(
    "Candidate Shortlisted"
  );
};
function CandidateModal({ candidate, onClose }) {
  if (!candidate) return null;

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white w-[800px] max-h-[90vh] overflow-y-auto rounded-xl p-6">

        <div className="flex justify-between items-center">
          <h2 className="text-2xl font-bold">
            Candidate Profile
          </h2>

          <button
            onClick={onClose}
            className="text-red-500 font-bold"
          >
            X
          </button>
        </div>

        <div className="mt-4">
          <h3 className="font-bold text-lg">
            {candidate.headline}
          </h3>

          <p>
            Candidate ID: {candidate.candidate_id}
          </p>
        </div>

        <div className="mt-6">
          <h4 className="font-semibold">
            Matched Skills
          </h4>

          <div className="flex flex-wrap gap-2 mt-2">
            {candidate.matched_skills?.map((skill, index) => (
              <span
                key={index}
                className="bg-blue-100 px-3 py-1 rounded-full"
              >
                {skill}
              </span>
            ))}
          </div>
        </div>

        <div className="mt-6">
          <h4 className="font-semibold">
            AI Summary
          </h4>

          <p className="mt-2 text-gray-700">
            {candidate.ai_summary}
          </p>
        </div>

        <div className="mt-6">
          <h4 className="font-semibold">
            Contact Information
          </h4>

          <div className="bg-gray-100 p-4 rounded mt-2">
            <p>Email: Not Available</p>
            <p>Phone: Not Available</p>
            <p>LinkedIn: Not Available</p>
          </div>
          <div className="mt-6 flex gap-3">
            <div className="mt-5">

  <h3 className="font-bold mb-2">
    Recruiter Notes
  </h3>

  <textarea
    rows={4}
    placeholder="Add notes..."
    className="w-full border rounded p-3"
  />

</div>

  <button
    className="bg-green-600 text-white px-4 py-2 rounded"
    onClick={() =>
      alert("Candidate Shortlisted")
    }
  >
    ⭐ Shortlist
  </button>

  <button
    className="bg-blue-600 text-white px-4 py-2 rounded"
    onClick={() =>
      alert("Interview Scheduled")
    }
  >
    📅 Schedule Interview
  </button>

</div>
        </div>

      </div>
    </div>
  );
}

export default CandidateModal;