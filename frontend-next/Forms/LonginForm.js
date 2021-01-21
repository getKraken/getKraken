import React from 'react';
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';

class LonginForm extends React.Component {
  constructor(props){
    super(props);
    this.state={
      username:'',
      password:'',
      buttonDisabled: false,
      isAuthenticated: false
    }
  }

  setInputValue(proprety, val){
    val = val.trim();
    if(val.length > 12){
      return;
    }
    this.setState({
      [proprety]:val
    })
  }

  resetForm(){
    this.setState({
      username:'',
      password:'',
      buttonDisabled:false
    })
  }

  async doSinUp(){
    if(!this.state.username){
      return;
    }
    if(!this.state.password){
      return;
    }
    this.setState({
      buttonDisabled:true
    })
    try {
      let res = await fetch('https://reqres.in/api/login',{
        method:'POST',
        headers:{
          'Accept':'application/json',
          'Contnent-Type':'application/json'
        },
        body:JSON.stringify({
          username:this.state.username,
          password: this.state.password
        })

      });
      let result = await res.json();
      if(result && result.success){
        this.setState({
          isAuthenticated: true
        });
      }
      else if (result && result.success === false){
        this.resetForm();
        alert(result.msg);
      }
    }
    catch(e){
      console.log(e);
      this.resetForm();
    }
  }

  
  render(){
    return(
      <div className="singUpPage">
        Log in 
        <InputField
          type= 'text'
          placeholder='user'
        />
      </div>
    );
  }

}

export default LonginForm;