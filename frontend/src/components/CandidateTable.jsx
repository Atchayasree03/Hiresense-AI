import { useNavigate } from "react-router-dom";
function CandidateTable({
  candidates,
  onShortlist
}) {
const navigate = useNavigate();
const getMatchLabel = (score) => {
  if (score >= 60)
    return "Excellent";

  if (score >= 40)
    return "Good";

  return "Weak";
};
  return (
    <div className="bg-white rounded-xl shadow-lg p-4 mt-8 overflow-x-auto">

      <table className="w-full border-collapse">

        <thead>
          <tr className="bg-gray-100">

            <th className="p-3 text-left">
              Rank
            </th>

            <th className="p-3 text-left">
              Candidate ID
            </th>

            <th className="p-3 text-left">
              Headline
            </th>

            <th className="p-3 text-left">
              Match Score
            </th>

            <th className="p-3 text-left">
              Skills
            </th>

            <th className="p-3 text-left">
              Email
            </th>

            <th className="p-3 text-left">
              Contact
            </th>

            <th className="p-3 text-left">
              Actions
            </th>

          </tr>
        </thead>

        <tbody>

          {candidates.map((candidate, index) => (

            <tr
              key={candidate.candidate_id}
              className="border-b"
            >

              <td className="p-3">
                #{index + 1}
              </td>

              <td className="p-3">
                {candidate.candidate_id}
              </td>

              <td className="p-3">
                {candidate.headline}
              </td>

              <td className="p-3 font-bold text-green-600">
                <div>
  <div>
    {candidate.final_score}
  </div>

  <div className="text-xs">
    {getMatchLabel(
      candidate.final_score
    )}
  </div>
</div>
              </td>

              <td className="p-3">
                <div className="flex flex-wrap gap-1">

                    {candidate.matched_skills?.map((skill, idx) => (
                    <span
                        key={idx}
                        className="bg-blue-100 px-2 py-1 rounded text-sm"
                    >
                        {skill}
                    </span>
                    ))}

                </div>
                </td>

              <td className="p-3 text-gray-500">
                N/A
              </td>

              <td className="p-3 text-gray-500">
                N/A
              </td>

              <td className="p-3">

                <div className="flex flex-col gap-2">

                    <button
                        onClick={() =>
                          navigate(`/candidate/${candidate.candidate_id}`, {
                              state: {
                                  rankedCandidate: candidate
                              }
                          })
                      }

                        className="bg-blue-600 text-white px-3 py-2 rounded"
                      >
                        View Details
                      </button>

                    <button
                    onClick={() =>
                        onShortlist(candidate)
                    }
                    className="bg-green-600 text-white px-3 py-2 rounded"
                    >
                    ⭐ Shortlist
                    </button>

                </div>

                </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}


export default CandidateTable;