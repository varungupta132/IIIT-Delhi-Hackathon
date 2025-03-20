import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

export const addEmployee = (data) => {
  return axios.post(`${API_BASE_URL}/add-employee`, data);
};

export const getAggregatedData = () => {
  return axios.get(`${API_BASE_URL}/aggregate-data`);
};