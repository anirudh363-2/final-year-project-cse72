import React, { useState } from "react";

const EditCourseForm = ({ onEditCourse, setShowForm, currentCourse }) => {
  // Initialize state with the current course data
  const [courseData, setCourseData] = useState(currentCourse);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (courseData.name.trim()) {
      onEditCourse(courseData); // Pass the updated course object
    } else {
      alert("Course name cannot be empty!");
    }
  };

  return (
    <div className="add-edit-form-container">
      <h2 className="form-heading">Edit Course</h2>
      <form onSubmit={handleSubmit} className="add-edit-form">
        <div className="input-group">
          <label htmlFor="courseName" className="form-label">
            Course Name:
          </label>
          <input
            type="text"
            id="courseName"
            placeholder="Enter course name"
            value={courseData.name}
            onChange={(e) =>
              setCourseData({ ...courseData, name: e.target.value }) // Update name property
            }
            className="form-input"
          />
        </div>
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

export default EditCourseForm;
