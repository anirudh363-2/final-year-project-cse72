import React, { useState, useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faArrowLeft, faHome
} from "@fortawesome/free-solid-svg-icons";
import { Link } from "react-router-dom";
import ErrorPage from "../components/ErrorPage";
import LoadingScreen from "../components/LoadingScreen";

const OtherDetails = () => {
  const [otherDetails, setOtherDetails] = useState([]);
  const [error, setError] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  // Fetch data on mount
  useEffect(() => {
    fetchDetails();
  }, []);

  const fetchDetails = async () => {
    setIsLoading(true);

    try {
      const response = await fetch("/api/other-details");
      if (!response.ok) throw new Error("Failed to fetch data.");
      const data = await response.json();
      console.log(data);
      setOtherDetails(data);
      setTimeout(() => {
        setIsLoading(false);
      }, 800);
    } catch (error) {
      console.error("Error fetching data:", error.message);
    }
  };


  return (
    <div className="table-container">
      <div className="sidebar">
        <Link to="/data">
          <div className="back-arrow">
            <FontAwesomeIcon icon={faArrowLeft} />
          </div>
        </Link>
        <Link to="/">
                  <div className="home-button">
                    <FontAwesomeIcon icon={faHome} />
                  </div>
                </Link>
      </div>
      <h2 className="table-heading">OTHER DETAILS <span className="read-only">(read-only)</span></h2>
      <table className="table">
        <thead>
          <tr>
            <th>S.No.</th>
            <th>Room Capacity</th>
            <th>Available Timeslots</th>
          </tr>
        </thead>
        <tbody>
          {otherDetails.map((detail, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{detail.roomCapacity}</td>
              <td>
              {[...detail.timeSlots]
                  .sort((a, b) => {
                    const order = { "9AM": 1, "12PM": 2, "3PM": 3 };
                    return order[a] - order[b];
                  }).map((timeSlot, index) => (
                    <span key={index} className="course-tag">
                    <ul className="styled-list">
                      <li>{timeSlot}</li>
                    </ul>
                  </span>
                ))}
              </td>
            </tr>
          ))}
        </tbody>
      </table>


      <div className="table-blue-circle"></div>
      <div className="table-diagonal-square"></div>

      {error && <ErrorPage />}
      {isLoading && <LoadingScreen />}
    </div>
  );
};

export default OtherDetails;
