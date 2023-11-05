import { useCallback } from 'react';
import Graphs from './Graphs';
import Header from './Header';
import Quote from './Quote';
import { useNavigate } from 'react-router-dom';


function Home(){
    const navigate = useNavigate();

    const navigateToNewRoute = useCallback(() => {
        navigate('/input');
    },[]);

    return(
        <>
            <Header/>
            <Quote />  
            <Graphs />
            <div className='button-container'>
                <button onClick={navigateToNewRoute}>
                    See if you qualify!
                </button>
            </div>
        </>
        
    )
}

export default Home;