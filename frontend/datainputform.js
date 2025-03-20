import React, { useState } from 'react';
import { addEmployee } from '../services/api';

const DataInputForm = () => {
  const [formData, setFormData] = useState({ name: '', department: '', salary: '' });

  const handleSubmit = async (e) => {
    e.preventDefault();
    await addEmployee(formData);
    alert('Data submitted!');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Name" value={formData.name} onChange={(e) => setFormData({ ...formData, name: e.target.value })} />
      <input type="text" placeholder="Department" value={formData.department} onChange={(e) => setFormData({ ...formData, department: e.target.value })} />
      <input type="number" placeholder="Salary" value={formData.salary} onChange={(e) => setFormData({ ...formData, salary: e.target.value })} />
      <button type="submit">Submit</button>
    </form>
  );
};

export default DataInputForm;