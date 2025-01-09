import React, { useState, useEffect } from "react";

const EditStudentForm = ({ onEditStudent, setShowForm, currentStudent, courses }) => {
  // Initialize state with the current faculty data
  const [studentData, setStudentData] = useState(currentStudent);

  useEffect(() => {
    // Ensure the form starts with the current faculty data
    setStudentData(currentStudent);
  }, [currentStudent]);

  // Handle checkbox changes for course
  const handleCourseChange = (course) => {
    setStudentData((prevData) => {
      const updatedCourses = prevData.courses.includes(course)
        ? prevData.courses.filter((c) => c !== course) // Remove course
        : [...prevData.courses, course]; // Add course

      return { ...prevData, courses: updatedCourses};
    });
  };


  const handleSubmit = (e) => {
    e.preventDefault();
    if (studentData.name.trim() && studentData.rollNumber.trim()) {
      // Ensure courses is always an array before submitting
      const sanitizedData = {
        ...studentData,
        courses: Array.isArray(studentData.courses)
          ? studentData.courses
          : [],
      };

      onEditStudent(sanitizedData); // Pass sanitized data to parent
      setStudentData({ name: "", rollNumber: "", courses: [] }); // Reset form fields
    } else {
      alert("Student name and roll number cannot be empty!");
    }
  };

  return (
    <div className="add-edit-form-container">
      <h2 className="form-heading">Add Student</h2>
      <form onSubmit={handleSubmit} className="add-edit-form">
        {/* Student Name Input */}
        <div className="input-group">
          <label htmlFor="StudentName" className="form-label">
            Student Name:
          </label>
          <input
            type="text"
            id="studentName"
            placeholder="Enter student name"
            value={studentData.name}
            onChange={(e) =>
              setStudentData({ ...studentData, name: e.target.value })
            }
            className="form-input"
          />
        </div>

        <div className="input-group">
          <label htmlFor="StudentRollNumber" className="form-label">
            Student Roll Number:
          </label>
          <input
            type="text"
            id="studentRollNumber"
            placeholder="Enter student roll number"
            value={studentData.rollNumber}
            onChange={(e) =>
              setStudentData({ ...studentData, rollNumber: e.target.value })
            }
            className="form-input"
          />
        </div>

        {/* Student Courses Checkboxes */}
        <div className="input-group">
          <label className="form-label">Student Courses:</label>
          <div className="checkbox-group">
            {courses.map((course) => (
              <div className="custom-checkbox-container" key={course._id}>
                <input
                  type="checkbox"
                  id={course._id}
                  checked={studentData.courses.includes(course)}
                  onChange={() => handleCourseChange(course)}
                  className="custom-checkbox"
                />
                <label htmlFor={course._id} className="custom-checkbox-label">
                  {course}
                </label>
              </div>
            ))}
          </div>
        </div>

        {/* Form Buttons */}
        <div className="form-buttons">
          <button
            type="button"
            className="cancel"
            onClick={() => setShowForm(false)}
          >
            Cancel
          </button>
          <button type="submit" className="create-button">
            Save Changes
          </button>
        </div>
      </form>
    </div>
  );
};

export default EditStudentForm;
