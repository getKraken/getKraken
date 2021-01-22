import React from 'react';
import InputField from '../components/InputField'
import SubmitButton from '../components/SubmitButton'

class NewEventForm extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      description : '',
      host : '',
      disableButton : false
    }
  }
  setInputValue(property, val) {
    // val = val.trim()
    if(val.length > 144) {
      return
    }
    this.setState({
      [property] : val
    })
  }

  async makeNewEvent(){
    if(! this.state.description){
      return;
    }
    this.setState({
      disableButton : true
    })

    try{
      fetch(base + '/api/v1/event', {
        method : "POST",
        header : {
          "Accept" : "application/json",
          "Content-Type" : "application/json",
        },
        body: JSON.stringify({
          description : this.state.description,
          host : this.state.host
        })
      })
    }catch(e) {
      console.error(e)
    }
  }
  render(){
    return (
      <div className="newEventForm">
        <InputField
        
          type = 'text'
          placeholder = 'Description'
          value = {this.state.description ? this.state.description : ''}
          onChange = {(val) => this.setInputValue('description', val)}
        />
        <SubmitButton
          disabled = {this.state.disableButton}
          onClick = {() => this.makeNewEvent()}
          text = "Add New Event"
        />
        
      </div>
    );
  }
}

export default NewEventForm;