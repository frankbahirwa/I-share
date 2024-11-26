import React, { useState, useEffect } from 'react';
import Logo from '../assets/images/logo.png';

const Loader = () => {
    const [activeDot, setActiveDot] = useState(0); // Tracks the currently active dot

    useEffect(() => {
        const numberOfDots = 3; // Total number of dots
        const duration = 2500; // Total animation duration (4 seconds)
        const intervalTime = duration / numberOfDots; // Time each dot stays active

        const interval = setInterval(() => {
            setActiveDot((prev) => (prev + 1) % numberOfDots); // Loop through dots
        }, intervalTime);

        // Cleanup interval when the component unmounts
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="flex flex-col h-screen justify-center items-center">
            <img src={Logo} alt="logo image" className="mb-6" />
            <div className="flex space-x-3 justify-center items-center">
                {[...Array(3)].map((_, index) => (
                    <div
                        key={index}
                        className={`rounded-full transition-all duration-500 ${
                            activeDot === index ? 'bg-red-400 w-7 h-7' : 'bg-red-200 w-5 h-5'
                        }`}
                    ></div>
                ))}
            </div>
        </div>
    );
};

export default Loader;
