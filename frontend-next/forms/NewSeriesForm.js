import React from 'react';
import InputField from '../components/InputField'
import SubmitButton from '../components/SubmitButton'



class NewSeriesForm extends React.Component {

  constructor(props){
    super(props)
    this.state = {
      title : '',
      numberOfParticipants : 0,
      //participants (how to get the participants)
      disableButton : false
    }
  }
  setInputValue(property, val) {
    // val = val.trim();
    if(val.length > 64){
      return;
    }
    this.setState({
      [property] : val
    })
    
  }
  
  async makeNewSeries(){
    if (! this.state.title){
      return;
    }
    this.setState({
      disableButton : true
    })
    try {
      fetch(base + '/api/v1/series', {
        method : "POST",
        header : {
          "Accept" : "application/json",
          "Content-Type" : "application/json",  
        },
        body: JSON.stringify({
            title : this.state.title,
            numberOfParticipants : this.state.numberOfParticipants,
          })
      });

    } catch(e) {
      console.error(e)
    }
  }
  
  render(){
    return (
      <div className="newSeriesForm">
        <InputField
          type = 'title'
          placeholder = 'Title'
          value = {this.state.title ? this.state.title : ''}
          onChange = {(val) => this.setInputValue('title',val)}
        />
        <SubmitButton
          disabled = {this.state.disableButton}
          onClick= {() => this.makeNewSeries()}
          text = "Create New Series"
        />
      </div>
    );
  }
}

export default NewSeriesForm;
