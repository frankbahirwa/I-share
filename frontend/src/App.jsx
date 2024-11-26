import { useState, useEffect } from 'react';
import Loader from './components/loader';

function App() {
  const [showLoader, setShowLoader] = useState(true); // Tracks whether to show the loader

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowLoader(false); // Hide the loader after 4 seconds
    }, 2000);

    return () => clearTimeout(timer); // Cleanup the timeout when the component unmounts
  }, []);

  return (
    <>
      {showLoader ? <Loader /> : <div>after loader</div>}
    </>
  );
}

export default App;
