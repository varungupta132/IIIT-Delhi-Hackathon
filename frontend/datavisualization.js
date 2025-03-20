import React, { useEffect, useState } from 'react';
import { getAggregatedData } from '../services/api';

const DataVisualization = () => {
  const [data, setData] = useState({ employees: [], projects: [], tasks: [] });

  useEffect(() => {
    getAggregatedData().then((response) => {
      setData(response.data);
    });
  }, []);

  return (
    <div>
      <h2>Employees</h2>
      <ul>
        {data.employees.map((emp) => (
          <li key={emp[0]}>{emp[1]} - {emp[2]} - ${emp[3]}</li>
        ))}
      </ul>
      <h2>Projects</h2>
      <ul>
        {data.projects.map((proj) => (
          <li key={proj[0]}>{proj[1]} - {proj[2]} to {proj[3]}</li>
        ))}
      </ul>
      <h2>Tasks</h2>
      <ul>
        {data.tasks.map((task) => (
          <li key={task[0]}>{task[1]} - {task[2]}</li>
        ))}
      </ul>
    </div>
  );
};

export default DataVisualization;