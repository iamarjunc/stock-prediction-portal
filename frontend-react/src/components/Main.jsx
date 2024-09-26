import React from 'react'
import Button from './Button'

const Main = () => {
  return (
    <>
      <div className='container'>
        <div className="p-5 text-center bg-light-dark rounded">
          <h1 className='text-light'>Stock Prediction Portal</h1>
          <p className='text-light lead'>
            Our platform leverages the power of Django and React to provide cutting-edge stock market predictions. Whether you're a seasoned investor or just getting started, our user-friendly interface and advanced algorithms will help you make informed decisions in the fast-paced world of stock trading. Stay ahead of the market with real-time data, accurate predictions, and personalized insights designed to help you maximize your investments.
          </p>
          <Button text ='Login' class="btn-outline-info" url="/login"/>
        </div>
      </div>
    </>
  )
}

export default Main