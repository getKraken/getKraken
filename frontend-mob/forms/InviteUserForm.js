import React from 'react';
import SubmitButton from '../components/SubmitButton'

class InviteUserForm extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      username : ''
    }
  }
  setInputValue(property,val) {
    val = val.trim();
    if (val.length > 64){
      return;
    }
    this.setState({
      [property] : val
    })
  }
  
  render(){
    return (
      <div className="InviteUserForm">
        <form>
            <label for='username'>Username:</label>
            <input type='text' id='username'></input>
          
            <SubmitButton></SubmitButton>
        </form>
      </div>
    );
  }

}

export default InviteUserForm;