import { useState } from "react";
// import axios from "axios";
import './input.css';

function InputPage(){
    const [carPay, setCarPay] = useState('');
    const [studentPay, setStudentPay] = useState('');
    const [creditScore, setCreditScore] = useState('');
    const [income, setIncome] = useState('');
    const [cardPay, setCardPay] = useState('');
    const [downPay, setDownPay] = useState('');
    const [id, setID] = useState('');

    const [formData, setFormData] = useState({
        id1:'',
        carPay1:'',
        studentPay1:'',
        creditScore1:'',
        income1:'',
        cardPay1:'',
        downPay1:'',
      });
    
  
    const handleCarPayChange = (e) => {
      setCarPay(e.target.value);
      setFormData({ ...formData, carPay1: e.target.value });
    };
  
    const handleStudentPayChange = (e) => {
      setStudentPay(e.target.value);
      setFormData({ ...formData, studentPay1: e.target.value });
    };

    const handleCreditScoreChange = (e) => {
        setCreditScore(e.target.value);
        setFormData({ ...formData, creditScore1: e.target.value });
    };

    const handleIncomeChange = (e) => {
        setIncome(e.target.value);
        setFormData({ ...formData, income1: e.target.value });
    };

    const handleCardPayChange = (e) => {
        setCardPay(e.target.value);
        setFormData({ ...formData, cardPay1: e.target.value });
    };

    const handleDownPayChange = (e) => {
        setDownPay(e.target.value);
        setFormData({ ...formData, downPay1: e.target.value });
    };

    const handleIDChange = (e) => {
        setID(e.target.value);
        setFormData({ ...formData, id1: e.target.value });
    };

    // const [profileData, setProfileData] = useState(null);
      
  
    const handleSubmit = async (e) => {
      e.preventDefault(); // Prevent the form from automatically submitting
    //   console.log(id);
    //   console.log(carPay);
    //   console.log(cardPay);
    //   console.log(studentPay);
    //   console.log(income);
    //   console.log(creditScore);
    //   console.log(downPay);
      // You can access the values of 'name', 'email', and 'password' here and perform further actions, such as API requests or validation.
      console.log(formData);
      
    //   try {
    //     const response = await fetch('http://127.0.0.1:5000/submit', {
    //       mode: 'no-cors',
    //       method: 'POST',
    //       headers: {
    //         'Content-Type': 'application/json',
    //       },
    //       body: JSON.stringify(formData),
    //     });
    //     console.log(response);
  
    //     if (response.ok) {
    //       console.log('Form data submitted successfully');
    //     } else {
    //       console.error('Form data submission failed');
    //     }
    //   } catch (error) {
    //     console.error('Error:', error);
    //   }
    };
  
    return (
      <div className="input-container">
        <h1>Enter your information...</h1>
        <form>
          <label>
            Id:
            <input name="id" type="number" value={id} onChange={handleIDChange} />
          </label>
          <br />
          <label>
            Car Payments (monthly):
            <input name="carPay" value={carPay} onChange={handleCarPayChange} />
          </label>
          <br />
          <label>
            Student Loan Payments (monthly):
            <input value={studentPay} onChange={handleStudentPayChange} />
          </label>
          <br />
          <label>
            Credit Score:
            <input type="number" value={creditScore} onChange={handleCreditScoreChange} />
          </label>
          <br />
          <label>
            Income Monthly:
            <input value={income} onChange={handleIncomeChange} />
          </label>
          <br />
          <label>
            Credit Card payments (monthly):
            <input value={cardPay} onChange={handleCardPayChange} />
          </label>
          <br />
          <label>
            Ideal Down Payment:
            <input value={downPay} onChange={handleDownPayChange} />
          </label>
          <button onClick={handleSubmit}>Submit</button>
        </form>
      </div>
    );
}

export default InputPage;