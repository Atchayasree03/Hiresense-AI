function CandidateCard({
  candidate,
  rank,
  onViewDetails
}) {
  return (
    <div className="bg-white rounded-xl shadow-lg p-6 border">
      <div className="flex justify-between">
        <h2 className="text-xl font-bold text-gray-800">
          Rank #{rank}
        </h2>

        <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full">
          {candidate.final_score}
        </span>
      </div>

      <h3 className="mt-3 text-lg font-semibold">
        {candidate.headline}
      </h3>

      <p className="text-gray-600">
        Candidate ID: {candidate.candidate_id}
      </p>

      <div className="grid grid-cols-3 gap-3 mt-4">
        <div className="bg-blue-50 p-3 rounded">
          <p className="text-sm">Semantic</p>
          <p className="font-bold">
            {candidate.semantic_score}
          </p>
        </div>

        <div className="bg-purple-50 p-3 rounded">
          <p className="text-sm">Career</p>
          <p className="font-bold">
            {candidate.career_score}
          </p>
        </div>

        <div className="bg-orange-50 p-3 rounded">
          <p className="text-sm">Behavior</p>
          <p className="font-bold">
            {candidate.behavior_score}
          </p>
        </div>
      </div>

      <div className="mt-4">
        <h4 className="font-semibold">
          Matched Skills
        </h4>

        <div className="flex flex-wrap gap-2 mt-2">
          {candidate.matched_skills?.map((skill, index) => (
            <span
              key={index}
              className="bg-indigo-100 text-indigo-700 px-3 py-1 rounded-full"
            >
              {skill}
            </span>
          ))}
        </div>
      </div>

      {candidate.ai_summary && (
        <div className="mt-4 bg-gray-50 p-4 rounded">
          <h4 className="font-semibold">
            AI Summary
          </h4>

          <p className="text-gray-700 mt-2">
            {candidate.ai_summary}
          </p>
        </div>
      )}
      <div className="mt-4 flex gap-2">
        <button
          onClick={() => onViewDetails(candidate)}
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          View Details
        </button>
      </div>
    </div>
  );
}

export default CandidateCard;