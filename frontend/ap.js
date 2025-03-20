import React, { useState } from 'react';
import DataInputForm from './components/DataInputForm';
import DataVisualization from './components/DataVisualization';
import './styles/App.css';

function App() {
  const [data, setData] = useState({ employees: [], projects: [], tasks: [] });

  return (
    <div className="App">
      <h1>Unified Data Aggregation System</h1>
      <DataInputForm />
      <DataVisualization data={data} />
    </div>
  );
}

export default App;