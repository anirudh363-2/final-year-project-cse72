import React, { useState, useEffect } from 'react';

export default function Courses() {
  const [courses, setCourses] = useState([]); 
  const [error, setError] = useState(null);

  const getCourses = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/courses');
      if (!response.ok) {
        throw new Error('Error fetching courses');
      }
      const data = await response.json();
      setCourses(data);
      setError(null); 
    } catch (err) {
      setError({ error: err.message });
    }
  };

  useEffect(() => {
    getCourses(); 
  }, []);

  return (
    <div className='courses'>
      <table className="table">
        <thead>
          <tr>
            <th>Course Code</th>
            <th>Course Name</th>
            <th>Student Count</th>
          </tr>
        </thead>
        <tbody>
          {courses.map((course, index) => (
            <tr key={index}>
              <td>{course.course_code}</td>
              <td>{course.course_name}</td>
              <td>{course.student_count}</td>
            </tr>
          ))}
        </tbody>
      </table>
      {error && <div className="error">{error.error}</div>}
    </div>
  );
}
