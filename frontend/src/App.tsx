
import { useEffect, useState } from 'react';
import './App.css'
import { api } from './libs/axios';
function App() {
  const [datas, setdata] = useState("")


  useEffect(() => {

    try {
      navigator.geolocation.getCurrentPosition(
        (success) => {
          console.log(success.coords.latitude);
          console.log(success)
          const lati = success.coords.latitude
          const longi = success.coords.longitude

          api.post('/user/location', { lati, longi })
          .then((response)=>{
            setdata(response.data.data.address)
          })
          .catch((error)=>{
            console.log(error.message);
            
          })
        }
      )
    } catch (error) {
      console.log(error.message);
    }
    try {

    } catch (error) {
      console.log(error.message);

    }

  }, [])
  return (
    <>
      <div>
        <h1>
          location tester
        </h1>
        <h2>address is {datas}</h2>
        
        {/* {res} */}
      </div>
    </>
  )
}

export default App

