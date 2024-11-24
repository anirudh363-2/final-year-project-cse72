import React, { useState, useEffect } from 'react';

export default function Rooms() {
  const [rooms, setRooms] = useState([]); 
  const [error, setError] = useState(null);

  const getRooms = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/rooms');
      if (!response.ok) {
        throw new Error('Error fetching rooms');
      }
      const data = await response.json();
      setRooms(data);
      setError(null); 
    } catch (err) {
      setError({ error: err.message });
    }
  };

  useEffect(() => {
    getRooms(); 
  }, []);
  return (
    <div className='rooms'>
      <table className="table">
        <thead>
          <tr>
            <th>Room Number</th>
            <th>Capacity</th>
            <th>Availability</th>
          </tr>
        </thead>
        <tbody>
          {rooms.map((room, index) => (
            <tr key={index}>
              <td>{room.room_number}</td>
              <td>{room.capacity}</td>
              {room.available ? <span class="material-symbols-outlined">check_circle</span> : <span class="material-symbols-outlined">cancel</span>}
            </tr>
          ))}
        </tbody>
      </table>
      {error && <div className="error">{error.error}</div>}
    </div>
  )
}
