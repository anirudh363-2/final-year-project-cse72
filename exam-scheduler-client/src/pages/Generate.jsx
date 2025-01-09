import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowLeft, faCalendarAlt, faXmarkCircle } from '@fortawesome/free-solid-svg-icons'; 
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css'; 

import LoadingScreen from '../components/LoadingScreen';
import ErrorPage from '../components/ErrorPage';

const Generate = () => {
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);
  const [timetableName, setTimetableName] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(false);
  const [timetableData, setTimetableData] = useState({});
  const [isModalOpen, setIsModalOpen] = useState(false); // Modal visibility state
  const [formError, setFormError] = useState(""); // To store validation error message

  const formatDate = (date) => {
    return date ? date.toISOString().split('T')[0] : null;
  };

  const handleClick = async () => {
    if (!startDate || !endDate || !timetableName) {
      setFormError("Please fill all the fields before submitting."); // Show error if fields are not filled
      return; // Prevent further execution if validation fails
    }

    setIsLoading(true);
    const data = {
      name: timetableName,
      start_date: formatDate(startDate),
      end_date: formatDate(endDate),
    };

    try {
      const response = await fetch('/api/timetables', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        const timetable = await response.json();
        console.log(timetable);
        setTimetableData(timetable);
        setIsModalOpen(true); // Open the modal on success
        setStartDate(null);
        setEndDate(null);
        setTimetableName('');
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
      } else {
        console.error("Failed to create timetable");
        setError(true);
      }
    } catch (error) {
      console.error("Error generating timetable:", error);
      setError(true);
    }
  };

  const closeModal = () => {
    setIsModalOpen(false); // Close the modal
  };

  return (
    <div className="generate-container">
      {/* Back Arrow */}
      <div className='nav-bar'>
        <Link to='/'>
          <div className="back-arrow">
            <FontAwesomeIcon icon={faArrowLeft} />
          </div>
        </Link>
      </div>

      {/* Shapes */}
      <div className="generate-diagonal-square"></div>
      <div className="generate-blue-circle"></div>

      {/* Heading */}
      <h1 className="generate-heading">GENERATE YOUR TIME TABLE</h1>

      {/* Input Fields */}
      <div className="input-group">
        <div className="input-box">
          <FontAwesomeIcon icon={faCalendarAlt} className="icon" />
          <DatePicker
            selected={startDate}
            onChange={(date) => setStartDate(date)}
            placeholderText="Start Date"
            className="custom-datepicker"
          />
        </div>
        <div className="input-box">
          <FontAwesomeIcon icon={faCalendarAlt} className="icon" />
          <DatePicker
            selected={endDate}
            onChange={(date) => setEndDate(date)}
            placeholderText="End Date"
            className="custom-datepicker"
          />
        </div>
      </div>

      <input
        type="text"
        placeholder="Enter the name of the timetable"
        className="timetable-name"
        value={timetableName}
        onChange={(e) => setTimetableName(e.target.value)}
      />

      {/* Show form error message if validation fails */}
      {formError && <p className="error-message">{formError}</p>}

      {/* Create Button */}
      <button onClick={handleClick} className="create-button">Generate</button>

      {isLoading && <LoadingScreen />}
      {error && <ErrorPage />}

      {/* Modal to display the timetable data */}
      {isModalOpen && (
        <div className="modal">
          <div className="modal-content">
            <button onClick={closeModal} className="close-button">
              <FontAwesomeIcon icon={faXmarkCircle} />
            </button>
            <h2>{timetableData.name} - Timetable Created</h2>
            <Link to={`/methods/${timetableData.name}`} state={{ timetableName: timetableData.name, id: timetableData.id }}>
              <button className="open-button">View Timetable</button>
            </Link>
          </div>
        </div>
      )}
    </div>
  );
};

export default Generate;
