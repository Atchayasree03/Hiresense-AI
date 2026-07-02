import { useEffect, useState } from "react";
import API from "../services/api";
import {
    useParams,
    useNavigate,
    useLocation
} from "react-router-dom";
function CandidateDetails() {

    const { id } = useParams();
    const navigate = useNavigate();
    const location = useLocation();

    const rankedCandidate =
        location.state?.rankedCandidate;
    const [candidate, setCandidate] = useState(null);

    useEffect(() => {
        loadCandidate();
    }, []);

    async function loadCandidate() {

        try {

            const response = await API.get(`/candidate/${id}`);

            setCandidate({
              ...response.data,
              ...rankedCandidate
          });

        }

        catch(err){
            console.log(err);
        }

    }

    if(!candidate){
        return <div className="p-10 text-xl">Loading...</div>;
    }

    return (

<div className="min-h-screen bg-slate-100 p-8">

<button
onClick={() => navigate("/")}
className="bg-blue-600 text-white px-5 py-2 rounded mb-8"
>
← Back to Candidates
</button>

<div className="bg-white rounded-xl shadow-lg p-8">

<h1 className="text-4xl font-bold">
{candidate.profile.headline}
</h1>

<p className="text-gray-500 mt-2">
Candidate ID : {candidate.candidate_id}
</p>

<div className="grid grid-cols-4 gap-4 mt-8">

<div className="bg-blue-50 p-4 rounded">

<h3 className="font-bold">
Location
</h3>

<p>{candidate.profile.location}</p>

</div>

<div className="bg-green-50 p-4 rounded">

<h3 className="font-bold">
Experience
</h3>

<p>
{candidate.profile?.years_of_experience || "Not Available"} Years
</p>

</div>

<div className="bg-yellow-50 p-4 rounded">

<h3 className="font-bold">
Current Company
</h3>

<p>
{candidate.profile.current_company || "Not Available"}
</p>

</div>

<div className="bg-purple-50 p-4 rounded">

<h3 className="font-bold">
Current Role
</h3>

<p>
{candidate.profile.current_title || "Not Available"}
</p>

</div>

</div>

<div className="mt-10">

<h2 className="text-2xl font-bold mb-3">
Professional Summary
</h2>

<div className="bg-gray-100 p-5 rounded-lg">

{candidate.profile.summary}

</div>

</div>

<div className="mt-10">

<h2 className="text-2xl font-bold mb-4">
Skills
</h2>

<div className="flex flex-wrap gap-3">

{candidate.skills.map((skill,index)=>(

<div
key={index}
className="bg-blue-100 px-4 py-2 rounded-full"
>

{skill.name}

</div>

))}

</div>

</div>

<div className="mt-10">

  <div className="mt-10">

<h2 className="text-2xl font-bold mb-5">
AI Match Analysis
</h2>

<div className="grid grid-cols-4 gap-4">

<div className="bg-blue-100 p-4 rounded">
<b>Final Score</b>
<p>{candidate.match_score}</p>
</div>

<div className="bg-green-100 p-4 rounded">
<b>Semantic</b>
<p>{candidate.semantic_score}</p>
</div>

<div className="bg-yellow-100 p-4 rounded">
<b>Career</b>
<p>{candidate.career_score}</p>
</div>

<div className="bg-purple-100 p-4 rounded">
<b>Behavior</b>
<p>{candidate.behavior_score}</p>
</div>

</div>

</div>

<div className="mt-10">

<h2 className="text-2xl font-bold mb-4">
Matched Skills (This is not only by keyword matching.AI analyze entire career history,projects and returns these skills.This also include which they didn't mention in their skills section)
</h2>

<div className="flex flex-wrap gap-3">

{candidate.matched_skills?.map((skill,index)=>(

<div
key={index}
className="bg-green-200 px-4 py-2 rounded-full"
>

{skill}

</div>

))}

</div>

</div>

<div className="mt-10">

<h2 className="text-2xl font-bold mb-4">
Why this Candidate?
</h2>

<ul className="list-disc ml-8">

{candidate.reasons?.map((r,index)=>(

<li key={index}>{r}</li>

))}

</ul>

</div>

<div className="mt-10">

<h2 className="text-2xl font-bold mb-4">
AI Summary
</h2>

<div className="bg-blue-50 p-5 rounded-lg">

{candidate.ai_summary}

</div>

</div>

<div className="mt-10">

{/* <h2 className="text-2xl font-bold mb-4">
Company Fit
</h2>

<div className="bg-gray-100 p-5 rounded">

<p>

<b>Company Type :</b>

{candidate.company_type}

</p>

<p className="mt-3">

{candidate.company_reason}

</p>

</div> */}

</div>

<h2 className="text-2xl font-bold mb-5">
Career History
</h2>

{candidate.career_history.map((job,index)=>(

<div
key={index}
className="border rounded-lg p-5 mb-5"
>

<h3 className="text-xl font-bold">

{job.title}

</h3>

<p className="text-gray-500">

{job.company}

</p>

<p>

{job.start_date} → {job.end_date || "Present"}

</p>

<p>

Industry : {job.industry}

</p>

<p className="mt-3">

{job.description}

</p>

</div>

))}

</div>

<div className="mt-10">

<h2 className="text-2xl font-bold mb-5">
Education
</h2>

{candidate.education.map((edu,index)=>(

<div
key={index}
className="border rounded-lg p-5 mb-4"
>

<h3 className="font-bold">

{edu.institution}

</h3>

<p>

{edu.degree}

</p>

<p>

{edu.field_of_study}

</p>

<p>

Grade : {edu.grade}

</p>

</div>

))}

</div>

<div className="mt-10">

<h2 className="text-2xl font-bold mb-5">
Languages
</h2>

<div className="flex gap-3 flex-wrap">

{candidate.languages.map((lang,index)=>(

<div
key={index}
className="bg-green-100 px-4 py-2 rounded-full"
>

{lang.language}

</div>

))}

</div>

</div>

<div className="mt-10">

<h2 className="text-2xl font-bold mb-5">
Certifications
</h2>

{candidate.certifications?.length===0?

<p>No Certifications</p>

:

candidate.certifications.map((cert,index)=>(

<div
key={index}
className="border rounded p-4 mb-3"
>

<h3>

{cert.name}

</h3>

<p>

{cert.issuer}

</p>

</div>

))

}

</div>

<div className="mt-10">

<h2 className="text-2xl font-bold mb-5">
Redrob Signals
</h2>

<div className="grid grid-cols-3 gap-4">

<div className="bg-gray-100 p-4 rounded">

Open To Work

<br/>

<b>

{candidate.redrob_signals.open_to_work_flag?"Yes":"No"}

</b>

</div>

<div className="bg-gray-100 p-4 rounded">

Recruiter Response

<br/>

<b>

{candidate.redrob_signals.recruiter_response_rate}

</b>

</div>

<div className="bg-gray-100 p-4 rounded">

Profile Score

<br/>

<b>

{candidate.redrob_signals.profile_completeness_score}

</b>

</div>

<div className="bg-gray-100 p-4 rounded">

    Expected Salary

    <br/>

    <b>

    {candidate.redrob_signals?.expected_salary_range_inr_lpa ? (
        <>
            ₹ {candidate.redrob_signals.expected_salary_range_inr_lpa.min}
            {" - "}
            ₹ {candidate.redrob_signals.expected_salary_range_inr_lpa.max} LPA
        </>
    ) : (
        "Not Available"
    )}

    </b>

</div>

<div className="bg-gray-100 p-4 rounded">

Notice Period

<br/>

<b>

{candidate.redrob_signals.notice_period_days} Days

</b>

</div>

<div className="bg-gray-100 p-4 rounded">

Interview Completion

<br/>

<b>

{candidate.redrob_signals.interview_completion_rate}

</b>

</div>

</div>

</div>

<div className="flex gap-5 mt-12">

<button className="bg-green-600 text-white px-6 py-3 rounded-lg">
⭐ Shortlist
</button>

<button className="bg-blue-600 text-white px-6 py-3 rounded-lg">
📅 Schedule Interview
</button>

<button className="bg-purple-600 text-white px-6 py-3 rounded-lg">
💾 Save Candidate
</button>

</div>

</div>

</div>

);

}

export default CandidateDetails;