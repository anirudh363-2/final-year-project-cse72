import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faXmarkCircle } from "@fortawesome/free-solid-svg-icons";


const TimetableDisplay = ({ name, data, closePopup }) => {


  return (
    <div className="table-popup-overlay">
      <div className="table-popup-content">
        <button onClick={closePopup} className="close-button">
          <FontAwesomeIcon icon={faXmarkCircle} />
        </button>
        <h2>{name} Method Details</h2>

        <div className="tables-container">
          {/* Display Exams Table */}
          <h3>Exams</h3>
          <table className="data-table">
            <thead>
              <tr>
                <th>Course</th>
                <th>Date</th>
                <th>Faculty</th>
                <th>Time</th>
              </tr>
            </thead>
            <tbody>
              {data.exams.map((exam, index) => (
                <tr key={index}>
                  <td>{exam.course}</td>
                  <td>{exam.date}</td>
                  <td>{exam.faculty}</td>
                  <td>{exam.time}</td>
                </tr>
              ))}
            </tbody>
          </table>

          {/* Display Students Table */}
          <h3>Students</h3>
          <table className="data-table last-table">
            <thead>
              <tr>
                <th>Date</th>
                <th>Room</th>
                <th>Student</th>
                <th>Time</th>
              </tr>
            </thead>
            <tbody>
              {data.students.map((student, index) => (
                <tr key={index}>
                  <td>{student.date}</td>
                  <td>{student.room}</td>
                  <td>{student.student}</td>
                  <td>{student.time}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <br />
        </div>
      </div>
    </div>
  );
};

export default TimetableDisplay;