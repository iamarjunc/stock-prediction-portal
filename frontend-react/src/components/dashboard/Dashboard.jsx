import React,{useEffect} from 'react'
import axios from 'axios'
import axiosInstance from '../../AxiosInstance'

const Dashboard = () => {

  useEffect(() => {
    const fetchProtectedData = async () => {
      try{
        const response = await axiosInstance.get('/protected-view/');
        console.log("Success", response.data);
      }
      catch(error){
        console.error("Error fetching Data: ",error);
      }
    }
    fetchProtectedData();
  },[])

  return (
    <div>dashboard</div>
  )
}

export default Dashboard