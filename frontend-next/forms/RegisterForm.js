// import Router from 'next/dist/next-server/lib/router/router';
import React from 'react';
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';
// import '../styles/LonginForm';
import Router from 'next/router';
class RegisterForm extends React.Component {
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
    if(val.length > 64){
      return;
    }
    this.setState({
      [proprety]:val
    })
  }

  resetForm(){
    this.setState({
<<<<<<< HEAD
      username:'',
=======
      email:'',
>>>>>>> db2eac31176908f68250681c5e11ad67904a4577
      password:'',
      buttonDisabled:false
    })
  }

  async doSignUp(){
<<<<<<< HEAD
    if(!this.state.username){
=======
    if(!this.state.email){
>>>>>>> db2eac31176908f68250681c5e11ad67904a4577
      return;
    }
    if(!this.state.password){
      return;
    }
    this.setState({
      buttonDisabled:true
    })
    try {
<<<<<<< HEAD
      await fetch('https://get-kraken.herokuapp.com/accounts/login/',{
=======
      await fetch('http://get-kraken.herokuapp.com/api/v1/user/',{
>>>>>>> db2eac31176908f68250681c5e11ad67904a4577
        method:'POST',
        headers:{
          'Accept':'application/json',
          'Content-Type':'application/json'
        },
        body:JSON.stringify({
<<<<<<< HEAD
          username:this.state.username,
          password: this.state.password
        })

      })
        .then(data => {
          localStorage.setItem('access', data.access);
          localStorage.setItem('refresh', data.refresh);
        })
      Router.push('/all-series');
=======
          email:this.state.email,
          password: this.state.password
        })

      });
      Router.push('/series-list');
      // let result = await res.json();
      // if(result && result.success){
      //   this.setState({
      //     isAuthenticated: true
      //   });
      // }
      // else if (result && result.success === false){
      //   this.resetForm();
      //   alert(result.msg);
      // }
>>>>>>> db2eac31176908f68250681c5e11ad67904a4577
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
<<<<<<< HEAD
          type= 'text'
          placeholder='username'
          value={this.state.username ? this.state.username : ''}
          onChange={(val)=> this.setInputValue('username',val)}
=======
          type= 'email'
          placeholder='Email'
          value={this.state.email ? this.state.email : ''}
          onChange={(val)=> this.setInputValue('email',val)}
>>>>>>> db2eac31176908f68250681c5e11ad67904a4577
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

<<<<<<< HEAD
export default LoginForm;
=======
export default RegisterForm;
>>>>>>> db2eac31176908f68250681c5e11ad67904a4577
