import React from 'react';
import { Link } from 'react-router-dom';

export default function Sidbar() {
  return (
    <div className="sidebar">
        <div className="back-arrow"> <Link href="/HTML/start_page.html">&#x2190;</Link></div>
        <br />
        <Link href="/HTML/start_page.html"><h2 className="logo">CHRONO</h2></Link>
        <ul>
            <li><Link to={"/faculty"}><span>📂</span>FACULTY</Link></li>
            <li><Link href="/HTML/room_slots.html"><span>📂</span>ROOM SLOTS</Link></li>
            <li><Link href="/HTML/courses.html"><span>📂</span>COURSES</Link></li>
            <li><Link href="/HTML/timetables.html"><span>📂</span>TIMETABLES</Link></li>
        </ul>
    </div>
  )
}
