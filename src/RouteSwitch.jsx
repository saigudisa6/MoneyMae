import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './Home';
import InputPage from './InputPages/InputPage';
// import Header from './Header';

function RouteSwitch(){
    return(
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home/>} />
                <Route path="/input" element={<InputPage/>} />
            </Routes>
        </BrowserRouter>
    )
}

export default RouteSwitch;