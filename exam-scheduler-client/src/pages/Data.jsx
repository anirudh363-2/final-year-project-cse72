import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faUserGraduate,
  faDoorOpen,
  faBookOpen,
  faChalkboardTeacher,
  faEllipsisH,
  faCalendarAlt,
  faArrowRight,
  faArrowLeft,
} from "@fortawesome/free-solid-svg-icons";
import { Link } from "react-router-dom";
import home from "../assets/home.jpg";

export default function Data() {
  return (
    <>
    <div>
          <Link to="/">
            <div className="back-arrow">
              <FontAwesomeIcon icon={faArrowLeft} className="main-icon" />
            </div>
          </Link>
        </div>
      <div className="dashboard">
        <h1 className="dashboard-title">Database Management Dashboard</h1>
        

        <div className="dashboard-container">
          <div className="dashboard-card">
            <div className="icon">
              <FontAwesomeIcon
                icon={faChalkboardTeacher}
                className="main-icon"
              />
            </div>
            <p>FACULTY</p>
            <Link to="/faculty">
              <div className="arrow">
                <FontAwesomeIcon icon={faArrowRight} className="right-icon" />
              </div>
            </Link>
          </div>

          <div className="dashboard-card">
            <div className="icon">
              <FontAwesomeIcon icon={faUserGraduate} className="main-icon" />
            </div>
            <p>STUDENTS</p>
            <Link to="/students">
              <div className="arrow">
                <FontAwesomeIcon icon={faArrowRight} className="right-icon" />
              </div>
            </Link>
          </div>

          <div className="dashboard-card timetable">
            <div className="icon">
              <FontAwesomeIcon icon={faCalendarAlt} className="main-icon" />
            </div>
            <p>TIMETABLES</p>
            <Link to="/timetables">
              <div className="arrow">
                <FontAwesomeIcon icon={faArrowRight} className="right-icon" />
              </div>
            </Link>
          </div>

          <div className="dashboard-card courses">
            <div className="icon">
              <FontAwesomeIcon icon={faBookOpen} className="main-icon" />
            </div>
            <p>COURSES</p>
            <Link to="/courses">
              <div className="arrow">
                <FontAwesomeIcon icon={faArrowRight} className="right-icon" />
              </div>
            </Link>
          </div>

          <div className="dashboard-card">
            <div className="icon">
              <FontAwesomeIcon icon={faDoorOpen} className="main-icon" />
            </div>
            <p>ROOMS</p>
            <Link to="/rooms">
              <div className="arrow">
                <FontAwesomeIcon icon={faArrowRight} className="right-icon" />
              </div>
            </Link>
          </div>

          <div className="dashboard-card">
            <div className="icon">
              <FontAwesomeIcon icon={faEllipsisH} className="main-icon" />
            </div>
            <p>OTHER DETAILS</p>
            <Link to="/other-details">
              <div className="arrow">
                <FontAwesomeIcon icon={faArrowRight} className="right-icon" />
              </div>
            </Link>
          </div>
        </div>
      </div>
      <div className="dashboard-glass-panel"></div>
      <img src={home} alt="Workspace" className="dashboard-image" />
    </>
  );
}
