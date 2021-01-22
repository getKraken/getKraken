import React, {useState} from 'react';
import Axios from 'axios';

function RegForm () {
  const [usernameReg, setUsernameReg] = useState('')
  const [passwordReg, setPasswordReg] = useState('')
    return (
      <div className="regForm">
        <h1>Create an account</h1>
        <label>First Name: <input type="text" id="firstName"/></label>
        <label>Last Name: 
          <input type="text" id="lastName"
            onChange={(e)=>{
              setUsernameReg(e.target.value);
            }}
          />
        
        </label>           
        <label>Email: 
          <input type="text" id="email"
            onChange={(e)=>{
              setPasswordReg(e.target.value);
            }}
          />
        </label>        
        <label>Password: <input type="text" id="password"/></label>
      </div>
    );

}

export default RegForm;