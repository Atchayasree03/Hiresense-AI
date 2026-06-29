import { useEffect, useState } from "react";

function Shortlisted() {

  const [candidates,
  setCandidates] =
  useState([]);

  useEffect(() => {

    const data =
      JSON.parse(
        localStorage.getItem(
          "shortlisted"
        ) || "[]"
      );

    setCandidates(data);

  }, []);

  return (

    <div className="p-8">

      <h1 className="text-3xl font-bold mb-6">
        Shortlisted Candidates
      </h1>

      {candidates.map(c => (

        <div
          key={c.candidate_id}
          className="bg-white p-4 rounded shadow mb-4"
        >

          <h2>
            {c.headline}
          </h2>

          <p>
            {c.candidate_id}
          </p>

        </div>

      ))}

    </div>

  );
}

export default Shortlisted;