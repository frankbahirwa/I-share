import { useState, useEffect } from 'react';
import Loader from '../components/loader'
import Landing from '../components/landing/main'
import { BrowserRouter as Router , Routes , Route} from 'react-router-dom'


const Routing = () =>{    

    const [showLoader, setShowLoader] = useState(true); // Tracks whether to show the loader

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowLoader(false); // Hide the loader after 4 seconds
    }, 2000);

    return () => clearTimeout(timer); // Cleanup the timeout when the component unmounts
  }, []);


    return(
    <>    
    <Router>
      <Routes>
        <Route path='/' element={showLoader ? <Loader /> : <Landing />}></Route>
      </Routes>
    </Router>
    </>
    )
}

export default Routing;