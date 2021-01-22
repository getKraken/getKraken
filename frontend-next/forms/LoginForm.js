// import Router from 'next/dist/next-server/lib/router/router';
import React from 'react';
import InputField from '../components/InputField';
import SubmitButton from '../components/SubmitButton';
import axios from 'axios';
// import '../styles/LonginForm';
import Router from 'next/router';
class LoginForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
      buttonDisabled: false,
      isAuthenticated: false
    }
  }

  setInputValue(proprety, val) {
    val = val.trim();
    if (val.length > 64) {
      return;
    }
    this.setState({
      [proprety]: val
    })
  }

  resetForm() {
    this.setState({
      username: '',
      password: '',
      buttonDisabled: false
    })
  }

  async doSignUp() {
    if (!this.state.username) {
      return;
    }
    if (!this.state.password) {
      return;
    }
    this.setState({
      buttonDisabled: true
    })
    const url = "https://get-kraken.herokuapp.com/api/v1/token/";
    const response = await axios.post(url, { username: this.state.username, password: this.state.password });
    localStorage.setItem('kraken-access-token', response.data.access);
    localStorage.setItem('kraken-refresh-token', response.data.refresh);
    Router.push('/all-series');
  }


  render() {
    return (
      <div className="signUpPage">
        Log in
        <InputField
          type='text'
          placeholder='username'
          value={this.state.username ? this.state.username : ''}
          onChange={(val) => this.setInputValue('username', val)}
        />
        <InputField
          type='password'
          placeholder='Password'
          value={this.state.password ? this.state.password : ''}
          onChange={(val) => this.setInputValue('password', val)}
        />

        <SubmitButton
          text='Login'
          disabled={this.state.buttonDisabled}
          onClick={() => this.doSignUp()}
        />
      </div>
    );
  }

}

export default LoginForm;