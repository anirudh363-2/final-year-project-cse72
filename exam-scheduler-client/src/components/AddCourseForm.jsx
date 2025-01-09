import React, { useState } from "react";

const AddCourseForm = ({ onAddCourse, setShowForm }) => {
    const [courseData, setCourseData] = useState({ name: "" });


    const handleSubmit = (e) => {
        e.preventDefault();
        if (courseData.name.trim()) {
          onAddCourse(courseData); // Pass the entire object
          setCourseData({ name: "" }); // Reset the form field
        } else {
          alert("Course name cannot be empty!");
        }
      };

      return (
        <div className="add-edit-form-container">
          <h2 className="form-heading">Add Course</h2>
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
                  setCourseData({ ...courseData, name: e.target.value }) // Update the name property
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
                Add Course
              </button>
            </div>
          </form>
        </div>
      );
};

export default AddCourseForm;
