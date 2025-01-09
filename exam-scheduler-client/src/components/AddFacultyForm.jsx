import React, { useState } from "react";

const AddFacultyForm = ({ onAddFaculty, setShowForm, timeSlots }) => {
  const [facultyData, setFacultyData] = useState({ name: "", availability: [] });

  



//   // Define the available time slots
//   const timeSlots = ["9AM", "12PM", "3PM"];

  // Handle checkbox changes for availability
  const handleAvailabilityChange = (timeSlot) => {
    setFacultyData((prevData) => {
      const updatedAvailability = prevData.availability.includes(timeSlot)
        ? prevData.availability.filter((time) => time !== timeSlot) // Remove time slot
        : [...prevData.availability, timeSlot]; // Add time slot

      return { ...prevData, availability: updatedAvailability };
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (facultyData.name.trim()) {
      // Ensure availability is always an array before submitting
      const sanitizedData = {
        ...facultyData,
        availability: Array.isArray(facultyData.availability)
          ? facultyData.availability
          : [],
      };

      onAddFaculty(sanitizedData); // Pass sanitized data to parent
      setFacultyData({ name: "", availability: [] }); // Reset form fields
    } else {
      alert("Faculty name cannot be empty!");
    }
  };

  return (
    <div className="add-edit-form-container">
      <h2 className="form-heading">Add Faculty</h2>
      <form onSubmit={handleSubmit} className="add-edit-form">
        {/* Faculty Name Input */}
        <div className="input-group">
          <label htmlFor="facultyName" className="form-label">
            Faculty Name:
          </label>
          <input
            type="text"
            id="facultyName"
            placeholder="Enter faculty name"
            value={facultyData.name}
            onChange={(e) =>
              setFacultyData({ ...facultyData, name: e.target.value })
            }
            className="form-input"
          />
        </div>

        {/* Faculty Availability Checkboxes */}
        <div className="input-group">
          <label className="form-label">Faculty Availability:</label>
          <div className="checkbox-group">
            {timeSlots.map((time) => (
              <div className="custom-checkbox-container" key={time}>
                <input
                  type="checkbox"
                  id={time}
                  checked={facultyData.availability.includes(time)}
                  onChange={() => handleAvailabilityChange(time)}
                  className="custom-checkbox"
                />
                <label htmlFor={time} className="custom-checkbox-label">
                  {time}
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
            Add Faculty
          </button>
        </div>
      </form>
    </div>
  );
};

export default AddFacultyForm;
