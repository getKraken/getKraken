import React from 'react';
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';
import '../styles/LonginForm';
class LonginForm extends React.Component {
  constructor(props){
    super(props);
    this.state={
      email:'',
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
      email:'',
      password:'',
      buttonDisabled:false
    })
  }

  async doSignUp(){
    if(!this.state.email){
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
          'Content-Type':'application/json'
        },
        body:JSON.stringify({
          email:this.state.email,
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
      <div className="signUpPage">
        Log in 
        <InputField
          type= 'email'
          placeholder='Email'
          value={this.state.email ? this.state.email : ''}
          onChange={(val)=> this.setInputValue('email',val)}
        />
        <InputField
          type= 'password'
          placeholder='Password'
          value={this.state.password ? this.state.password : ''}
          onChange={(val)=> this.setInputValue('password',val)}
        />

        <SubmitButton
          text = 'Login'
          disabled = {this.state.buttonDisabled}
          onClick={()=> this.doSignUp()}
        />
      </div>
    );
  }

}

export default LonginForm;