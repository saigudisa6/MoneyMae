// import React from "react";
import NavBar from './NavBar';
import Greeting from './Greeting';
import './header.css';

function Header(){
    return (
    <>
        <div className="header">
        <NavBar />
        <Greeting />
        </div>
    </>
    )
}

export default Header;