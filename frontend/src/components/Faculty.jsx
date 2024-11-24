import React, { useState, useEffect } from 'react';

export default function Faculty() {
  const [faculty, setFaculty] = useState([]); 
  const [error, setError] = useState(null);

  const getFaculty = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/faculty');
      if (!response.ok) {
        throw new Error('Error fetching faculty');
      }
      const data = await response.json();
      setFaculty(data);
      setError(null); 
    } catch (err) {
      setError({ error: err.message });
    }
  };

  useEffect(() => {
    getFaculty(); 
  }, []);

  return (
    <div className='faculty'>
      <table className="table">
        <thead>
          <tr>
            <th>Faculty ID</th>
            <th>Faculty Name</th>
          </tr>
        </thead>
        <tbody>
          {faculty.map((fac, index) => (
            <tr key={index}>
              <td>{fac.faculty_id}</td>
              <td>{fac.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
      {error && <div className="error">{error.error}</div>}
    </div>
  );
}
